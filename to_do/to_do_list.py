from to_do.conn import conn
# This project aims to create a simple CLI based to do list program

def main():
    if conn:
        cursor = conn.cursor()
        while True:
            print("==== TO DO LIST ===")
            print("1. Register")
            print("2. Sign in")
            print("0. Exit")
            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                print("===== REGISTER USER ====")
                username = input("Enter your username: ")
                password = input("Enter password:")
                try:
                    cursor.execute("INSERT INTO users (username, password) VALUES ($1, $2)", (username, password))
                    conn.commit()
                    print("User Registered Successfully")
                except Exception as e:
                    print("Exception Occured")
                    print(e)
            
            elif user_choice == "2":
                username = input("Enter your username: ")
                password = input("Enter password:")
                cursor.execute("SELECT * FROM users WHERE username = $1 AND password = $2", (username, password))
                user = cursor.fetchone()

                if user:
                    print("User Signed In Successfully")
                    user_id = user[0]

                    cursor.execute("SELECT task_id, task, done AS status FROM tasks WHERE user_id = $1", (user_id,))
                    tasks = cursor.fetchall()

                    while True:
                        print("==== TO DO LIST ===")
                        print("1. Add Task")
                        print("2. Show Task")
                        print("3. Update Task")
                        print("4. Sign Out")
                        print("0. Exit")

                        choice = input("Enter your choice: ")

                        if choice == "1":
                            task_count = input("Enter the number of tasks you want to add: ")
                            for i in range(int(task_count)):
                                task = input("Enter the task: ")
                                cursor.execute("INSERT INTO tasks(user_id, task) VALUES($1, $2)",(user_id, task))
                                conn.commit()
                                print("Task Added!!!")
                            
                            # Refetch tasks after adding
                            cursor.execute("SELECT task_id, task, done AS status FROM tasks WHERE user_id = $1", (user_id,))
                            tasks = cursor.fetchall()

                        elif choice == "2":
                            if len(tasks) == 0:
                                print("No tasks available")
                            else:
                                print("\nTasks:")
                                for index, task in enumerate(tasks):
                                    status = "Done" if task[2] else "Not Done"
                                    print(f"{index+1}. {task[1]} - {status}")
                                print()

                        elif choice == "3":
                            if len(tasks) == 0:
                                print("No Task to update")
                            else:
                                print("\nTasks:")
                                for index, task in enumerate(tasks):
                                    status = "Done" if task[2] else "Not Done"
                                    print(f"{index+1}. {task[1]} - {status}")
                                task_index = int(input("Enter the task number you want to add: ")) -1 
                                if 0 <= task_index < len(tasks):
                                    task_id = tasks[task_index][0]
                                    cursor.execute("UPDATE tasks set done=TRUE WHERE task_id = $1", (task_id,))
                                    conn.commit()
                                    print("Task Marked as Done")

                                    # Refetch tasks after updating
                                    cursor.execute("SELECT task_id, task, done AS status FROM tasks WHERE user_id = $1", (user_id,))
                                    tasks = cursor.fetchall()
                                else:
                                    print("Invalid Task number.")

                        elif choice == "4":
                            print("Exiting the TO DO LIST")
                            break

                        elif choice == "0":
                            print("Exiting the TO DO LIST")
                            exit()

                        else:
                            print("Invalid Choice...")

            elif user_choice == "0":
                print("Exiting the application...")
                break

            else:
                print("Invalid Choice")
        
        #closing server connection
        conn.close()

    else:
        print("Server not connected...")

if __name__ == "__main__":
    main()