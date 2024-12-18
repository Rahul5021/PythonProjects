# To-Do List Application

This is a simple Python-based To-Do List application that allows users to register, sign in, add tasks, view tasks, and mark them as done. The application uses PostgreSQL as the database and `pg8000` to establish the connection.

## Features
- **User Registration**: Users can create an account with a username and password.
- **Sign In**: Users can sign in to their account to manage tasks.
- **Add Tasks**: Users can add multiple tasks to their to-do list.
- **View Tasks**: Displays all tasks and their completion status.
- **Update Tasks**: Users can mark tasks as done.

## Requirements
- Python 3.x
- PostgreSQL
- `pg8000` library for PostgreSQL connection
- `python-dotenv` for loading environment variables

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/to-do-list-app.git
   cd to-do-list-app
   ```
2. Install the required libraries:
    ```bash
    pip install requirements.txt
    ```
3. Set up a PostgreSQL database and add the following environment variables to a `.env` file:
    ```bash
    DB_NAME=your_database_name
    DB_USER=your_database_user
    DB_PASSWORD=your_database_password
    DB_HOST=localhost
    DB_PORT=5432
    ```
4. Run the application:
    ```bash
    python main.py
    ```

## Usage Instructions
After running the application, follow the on-screen instructions to register or sign in, and then manage your tasks.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.