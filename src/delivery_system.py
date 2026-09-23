import json
import math


def load_data(file_path):
    """Read and parse JSON data from a file."""

    with open(file_path, "r") as file:
        data = json.load(file)

    return data


def calculate_distance(location1, location2):
    """Calculate Euclidean distance between two points."""

    x1, y1 = location1
    x2, y2 = location2

    distance = math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2
    )

    return distance


def find_nearest_agent(warehouse_location, agents):
    """Find the agent nearest to the warehouse."""

    nearest_agent = None
    shortest_distance = float("inf")

    for agent_id, agent_location in agents.items():

        distance = calculate_distance(
            agent_location,
            warehouse_location
        )

        if distance < shortest_distance:
            shortest_distance = distance
            nearest_agent = agent_id

    return nearest_agent


def assign_packages(packages, agents, warehouses):
    """
    Assign each package to the nearest agent
    based on the agent's distance from the warehouse.
    """

    assignments = {}

    for package in packages:

        package_id = package["id"]
        warehouse_id = package["warehouse"]

        warehouse_location = warehouses[warehouse_id]

        nearest_agent = find_nearest_agent(
            warehouse_location,
            agents
        )

        assignments[package_id] = nearest_agent

    return assignments


def simulate_delivery(packages, assignments, agents, warehouses):
    """
    Simulate package delivery.

    Each agent travels from their current location
    to the warehouse and then from the warehouse
    to the package destination.
    """

    # Keep track of every agent's current location.
    current_locations = {}

    for agent_id, agent_location in agents.items():
        current_locations[agent_id] = agent_location[:]

    # Store results for every agent.
    agent_results = {}

    for agent_id in agents:
        agent_results[agent_id] = {
            "delivered": 0,
            "distance": 0.0
        }

    # Process packages in the order given in the JSON file.
    for package in packages:

        package_id = package["id"]
        warehouse_id = package["warehouse"]
        destination = package["destination"]

        agent_id = assignments[package_id]

        warehouse_location = warehouses[warehouse_id]

        # Agent travels from current location to warehouse.
        distance_to_warehouse = calculate_distance(
            current_locations[agent_id],
            warehouse_location
        )

        # Agent travels from warehouse to destination.
        distance_to_destination = calculate_distance(
            warehouse_location,
            destination
        )

        total_package_distance = (
            distance_to_warehouse +
            distance_to_destination
        )

        # Add distance to the agent's total.
        agent_results[agent_id]["distance"] += (
            total_package_distance
        )

        # Increase delivered package count.
        agent_results[agent_id]["delivered"] += 1

        # Agent is now at the destination.
        current_locations[agent_id] = destination[:]

    return agent_results


def generate_report(agent_results):
    """Generate the final delivery report."""

    report = {}

    best_agent = None
    best_efficiency = float("inf")

    for agent_id, result in agent_results.items():

        delivered = result["delivered"]
        distance = result["distance"]

        # Avoid division by zero for agents
        # who did not deliver any package.
        if delivered > 0:
            efficiency = distance / delivered
        else:
            efficiency = 0.0

        report[agent_id] = {
            "delivered": delivered,
            "distance": round(distance, 2),
            "efficiency": round(efficiency, 2)
        }

        # Lower distance per delivered package
        # means better efficiency.
        if delivered > 0 and efficiency < best_efficiency:
            best_efficiency = efficiency
            best_agent = agent_id

    report["agent"] = best_agent

    return report


def save_report(report, file_path):
    """Save the final report to report.json."""

    with open(file_path, "w") as file:
        json.dump(report, file, indent=4)