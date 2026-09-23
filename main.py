from src.delivery_system import (
    load_data,
    assign_packages,
    simulate_delivery,
    generate_report,
    save_report
)


# Input JSON file
file_path = "data/test_cases/test_case_1.json"

# Output report file
output_file = "output/report.json"


# Step 1: Load JSON data
data = load_data(file_path)

warehouses = data["warehouses"]
agents = data["agents"]
packages = data["packages"]


# Step 2: Assign packages to nearest agents
assignments = assign_packages(
    packages,
    agents,
    warehouses
)


# Display assignments
print("\nPackage Assignments:")

for package_id, agent_id in assignments.items():
    print(package_id, "->", agent_id)


# Step 3: Simulate deliveries
agent_results = simulate_delivery(
    packages,
    assignments,
    agents,
    warehouses
)


# Step 4: Generate report
report = generate_report(
    agent_results
)


# Step 5: Save report
save_report(
    report,
    output_file
)


# Display final report
print("\nDelivery Report:")

for agent_id in agents:

    print(
        agent_id,
        "->",
        report[agent_id]
    )

print("\nMost Efficient Agent:", report["agent"])

print("\nReport saved to:", output_file)