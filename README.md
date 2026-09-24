# 🚚 FastBox Delivery System

## 📌 Project Overview

FastBox Delivery System is a Python-based delivery simulation project.

This project simulates how delivery agents receive packages from different warehouses and deliver them to different destinations.

The system finds the nearest agent for each package, calculates the delivery distance, simulates delivery, and creates a final delivery report.

I also added some bonus features to make the project more realistic.

---

## 🎯 Main Features

* Read package, warehouse, and agent data from a JSON file
* Calculate distance using Euclidean distance
* Assign each package to the nearest delivery agent
* Simulate package delivery
* Calculate total distance travelled by each agent
* Calculate delivery efficiency
* Find the most efficient agent
* Generate a JSON delivery report

---

## ⭐ Bonus Features

### 1. Random Delivery Delays

Each package gets a random delivery delay between **1 and 10 minutes**.

The total delay is added to the agent's final report.

### 2. ASCII Route Visualization

The project displays delivery routes in the terminal.

Example:

```text
A3 Route:
  W5 -> P1 -> Destination
  W5 -> P3 -> Destination
  W4 -> P8 -> Destination
```

### 3. New Agent Joining Mid-Day

The project supports a new delivery agent joining during the delivery process.

For example:

```text
New Agent Joined Mid-Day:
A5 -> Location [50, 50]
```

The new agent is available for the second half of the package assignments.

### 4. Top Performer CSV Export

The most efficient agent is exported to a CSV file.

The file is saved as:

```text
output/top_performer.csv
```

---

## 🛠️ Technologies Used

* Python
* JSON
* CSV
* Math module
* Random module

---

## 📂 Project Structure

```text
FastBox_Delivery_System/
│
├── data/
│   └── test_cases/
│       └── test_case_1.json
│
├── src/
│   └── delivery_system.py
│
├── output/
│   ├── report.json
│   └── top_performer.csv
│
├── main.py
└── README.md
```

---

## ⚙️ How the Project Works

### Step 1: Read JSON Data

The program reads the input JSON file using Python's `json` module.

The JSON contains:

* Warehouses
* Agents
* Packages
* Package destinations

### Step 2: Find Nearest Agent

For every package, the program checks the distance between the warehouse and all available agents.

The nearest agent is selected for that package.

### Step 3: Simulate Delivery

The selected agent:

```text
Current Location
       ↓
Warehouse
       ↓
Package Destination
```

The distance travelled is calculated and added to the agent's total distance.

### Step 4: Calculate Efficiency

The efficiency is calculated using:

```text
Efficiency = Total Distance / Packages Delivered
```

A lower distance per delivered package means better efficiency.

### Step 5: Generate Report

The final report contains:

* Number of packages delivered
* Total distance
* Efficiency
* Delivery delay

The report is saved as:

```text
output/report.json
```

---

## ▶️ How to Run the Project

### 1. Open the project folder

Open the project in VS Code or terminal.

### 2. Run the Python program

```bash
python main.py
```

### 3. Check the output

The terminal shows:

* Package assignments
* New agent joining
* ASCII routes
* Delivery report
* Most efficient agent

---

## 📄 Output Files

### `report.json`

Contains the complete delivery report for all agents.

### `top_performer.csv`

Contains the details of the most efficient agent.

---

## 🧮 Distance Calculation

The project uses Euclidean distance.

Formula:

```text
distance = √((x2-x1)² + (y2-y1)²)
```

Python implementation:

```python
math.sqrt(
    (x2 - x1) ** 2 +
    (y2 - y1) ** 2
)
```

---

## 💡 What I Learned From This Project

Through this project, I practiced:

* Reading and working with JSON data
* Python functions
* Dictionaries and lists
* Loops and conditions
* File handling
* Distance calculation
* Data processing
* CSV file creation
* Basic simulation logic
* Writing clean and understandable Python code

