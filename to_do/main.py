from conn import conn
import os

# User registration function
def register_user(cursor):
    """
    Handles user registration by inserting a new user into the database.
    """
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    
    if not username or not password:
        print("Username and password cannot be empty.")
        return
    
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES ($1, $2)", (username, password))
        cursor.connection.commit()
        print("User Registered Successfully")
    except Exception as e:
        print(f"Error registering user: {e}")
        cursor.connection.rollback()

# User sign-in function
def sign_in_user(cursor):
    """
    Handles user sign-in by validating username and password.
    """
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    
    cursor.execute("SELECT * FROM users WHERE username = $1 AND password = $2", (username, password))
    user = cursor.fetchone()
    
    if user:
        print("User Signed In Successfully")
        return user[0]  # Return user_id
    else:
        print("Invalid username or password.")
        return None

# Fetch tasks of the logged-in user
def fetch_tasks(cursor, user_id):
    """
    Fetches all tasks of a specific user from the database.
    """
    cursor.execute("SELECT task_id, task, done AS status FROM tasks WHERE user_id = $1", (user_id,))
    return cursor.fetchall()

# Add a new task
def add_task(cursor, user_id):
    """
    Allows the user to add new tasks to the to-do list.
    """
    task_count = int(input("Enter the number of tasks you want to add: "))
    
    for _ in range(task_count):
        task = input("Enter the task: ").strip()
        cursor.execute("INSERT INTO tasks(user_id, task) VALUES($1, $2)", (user_id, task))
        cursor.connection.commit()
        print("Task Added!!!")

# Show all tasks
def show_tasks(tasks):
    """
    Displays all tasks and their completion status.
    """
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks):
            status = "Done" if task[2] else "Not Done"
            print(f"{index + 1}. {task[1]} - {status}")
        print()

# Update task status
def update_task(cursor, tasks):
    """
    Allows the user to update the status of a task (mark as done).
    """
    if not tasks:
        print("No tasks to update.")
        return

    show_tasks(tasks)
    task_index = int(input("Enter the task number you want to update: ")) - 1

    if 0 <= task_index < len(tasks):
        task_id = tasks[task_index][0]
        cursor.execute("UPDATE tasks SET done=TRUE WHERE task_id = $1", (task_id,))
        cursor.connection.commit()
        print("Task marked as Done")
    else:
        print("Invalid task number.")

# Main menu logic
def main():
    """
    Main function that handles the user interface and connects to the database.
    """
    
    if not conn:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()

    while True:
        print("==== TO DO LIST ===")
        print("1. Register")
        print("2. Sign In")
        print("0. Exit")
        user_choice = input("Enter your choice: ").strip()

        if user_choice == "1":
            print("===== REGISTER USER ====")
            register_user(cursor)
        
        elif user_choice == "2":
            user_id = sign_in_user(cursor)
            
            if user_id:
                tasks = fetch_tasks(cursor, user_id)
                
                while True:
                    print("==== TO DO LIST ===")
                    print("1. Add Task")
                    print("2. Show Tasks")
                    print("3. Update Task")
                    print("4. Sign Out")
                    print("0. Exit")
                    choice = input("Enter your choice: ").strip()

                    if choice == "1":
                        add_task(cursor, user_id)
                        tasks = fetch_tasks(cursor, user_id)  # Refetch tasks after adding

                    elif choice == "2":
                        show_tasks(tasks)

                    elif choice == "3":
                        update_task(cursor, tasks)
                        tasks = fetch_tasks(cursor, user_id)  # Refetch tasks after update

                    elif choice == "4":
                        print("Signing out...")
                        break

                    elif choice == "0":
                        print("Exiting the application...")
                        exit()

                    else:
                        print("Invalid choice. Please try again.")
        
        elif user_choice == "0":
            print("Exiting the application...")
            break
        
        else:
            print("Invalid choice. Please try again.")
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
