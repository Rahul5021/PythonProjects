from conn import conn
# This project aims to create a simple CLI based to do list program

if conn:
    def main():
        tasks = []

        while True:
            print("==== TO DO LIST ===")
            print("1. Add Task")
            print("2. Show Task")
            print("3. Update Task")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                task_count = input("Enter the number of tasks you want to add: ")
                for i in range(int(task_count)):
                    task = input("Enter the task: ")
                    tasks.append({"task": task , "done":False})
                    print("Task Added!!!")

            elif choice == "2":
                if len(tasks) == 0:
                    print("No tasks available")
                else:
                    print("\nTasks:")
                    for index, task in enumerate(tasks):
                        status = "Done" if task["done"] else "Not Done"
                        print(f"{index+1}. {task['task']} - {status}")
                    print()

            elif choice == "3":
                if len(tasks) == 0:
                    print("No Task to update")
                else:
                    task_index = int(input("Enter the task number you want to add: ")) -1 
                    if 0 <= task_index < len(tasks):
                        tasks[task_index]["done"] = True
                        print("Task Marked as Done")
                    else:
                        print("Invalid Task number.")

            elif choice == "4":
                print("Exiting the TO DO LIST")
                break

            else:
                print("Invalid Choice...")
else:
    print("Server not connected...")
if __name__ == "__main__":
    main()