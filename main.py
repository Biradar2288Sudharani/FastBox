from src.delivery_system import (
    load_data,
    assign_packages,
    simulate_delivery,
    generate_report,
    save_report,
    visualize_routes,
    add_new_agent,
    export_top_performer
)

# Input JSON file
file_path = "data/test_cases/test_case_1.json"

# Output report file
output_file = "output/report.json"
csv_output_file = "output/top_performer.csv"

# Step 1: Load JSON data
data = load_data(file_path)
warehouses = data["warehouses"]
agents = data["agents"]
packages = data["packages"]

# -------------------------------------------------
# MID-DAY SIMULATION
# -------------------------------------------------

# First half of the packages
first_half = packages[:len(packages) // 2]

# Second half of the packages
second_half = packages[len(packages) // 2:]

# Step 2: Assign first-half packages
assignments_first = assign_packages(
    first_half,
    agents,
    warehouses
)
print("\nFirst Half Package Assignments:")
for package_id, agent_id in assignments_first.items():
    print(package_id, "->", agent_id)

# Step 3: Simulate first-half deliveries
results_first = simulate_delivery(
    first_half,
    assignments_first,
    agents,
    warehouses
)

# -------------------------------------------------
# A5 JOINS MID-DAY
# -------------------------------------------------
add_new_agent("A5", [50, 50], agents)

# Step 4: Assign second-half packages
assignments_second = assign_packages(
    second_half,
    agents,
    warehouses
)
print("\nSecond Half Package Assignments:")
for package_id, agent_id in assignments_second.items():
    print(package_id, "->", agent_id)


# Step 5: Simulate second-half deliveries
results_second = simulate_delivery(
    second_half,
    assignments_second,
    agents,
    warehouses
)

# -------------------------------------------------
# COMBINE RESULTS
# -------------------------------------------------
agent_results = {}
for agent_id in agents:
    first_result = results_first.get(
        agent_id,
        {
            "delivered": 0,
            "distance": 0.0,
            "delay_minutes": 0
        }
    )
    second_result = results_second.get(
        agent_id,
        {
            "delivered": 0,
            "distance": 0.0,
            "delay_minutes": 0
        }
    )
    agent_results[agent_id] = {
        "delivered": (
            first_result["delivered"]
            + second_result["delivered"]
        ),
        "distance": (
            first_result["distance"]
            + second_result["distance"]
        ),
        "delay_minutes": (
            first_result["delay_minutes"]
            + second_result["delay_minutes"]
        )
    }

# Step 6: Visualize all routes
all_assignments = {}
all_assignments.update(assignments_first)
all_assignments.update(assignments_second)
visualize_routes(
    packages,
    all_assignments
)

# Step 7: Generate final report
report = generate_report(
    agent_results
)
export_top_performer(
    report,
    csv_output_file
)

# Step 8: Save report
save_report(
    report,
    output_file
)

# Step 9: Display final report
print("\nDelivery Report:")
for agent_id in agents:

    print(
        agent_id,
        "->",
        report[agent_id]
    )
print("\nMost Efficient Agent:", report["agent"])

print("\nReport saved to:", output_file)

print("Top performer CSV saved to:", csv_output_file)