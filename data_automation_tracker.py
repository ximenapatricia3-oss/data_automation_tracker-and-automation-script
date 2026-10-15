"""
Project: Automated Data Tracker and Management System
Author: Ximena Patricia López Yau
Description: Python automation script for managing and filtering data records.
"""

print("=" * 60)
print("         AUTOMATED DATA TRACKER & MANAGEMENT SYSTEM         ")
print("=" * 60 + "\n")

# Initial database simulation (List of dictionaries)
records = [
    {"id": 1, "task": "Configure OSPF Network Routing", "status": "Completed", "priority": "High"},
    {"id": 2, "task": "Optimize Python Script Repository", "status": "In Progress", "priority": "Medium"},
    {"id": 3, "task": "Apply for Remote Software Roles", "status": "Pending", "priority": "High"}
]

def display_records():
    print("--- CURRENT DATABASE RECORDS ---")
    for rec in records:
        print(f"ID: {rec['id']} | Task: {rec['task']} | Status: {rec['status']} | Priority: {rec['priority']}")
    print("-" * 60)

display_records()

new_task_name = input("Enter a new task to add to the system: ").strip()

if new_task_name:
    new_priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()
    new_id = len(records) + 1
    
    records.append({
        "id": new_id, 
        "task": new_task_name, 
        "status": "Pending", 
        "priority": new_priority if new_priority in ["High", "Medium", "Low"] else "Normal"
    })
    
    print("\n[SUCCESS] Record successfully added and automated!\n")
    display_records()
else:
    print("[WARNING] No input provided. Skipping record addition.")

input("\nPress Enter to exit the system...")
