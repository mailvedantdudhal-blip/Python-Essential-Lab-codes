assignments = ["Lab 1 Report", "Math Homework", "Physics Quiz Prep"]
print("Initial Assignment List:", assignments)

# Add a new assignment
new_task = input("\nEnter a new assignment to add: ").strip()
if new_task:
    assignments.append(new_task)
    print(f"Added '{new_task}' successfully.")

# Remove a completed assignment
completed_task = input("\nEnter an assignment to mark completed/remove: ").strip()
if completed_task in assignments:
    assignments.remove(completed_task)
    print(f"Removed '{completed_task}'.")
else:
    print(f"Task '{completed_task}' not found in the list.")

# Display updated list
print("\n--- Updated Assignment List ---")
for idx, task in enumerate(assignments, 1):
    print(f"{idx}. {task}")
