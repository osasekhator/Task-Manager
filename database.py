import psycopg2
import re

connection = psycopg2.connect(
        dbname = "TaskManager",
        user = "postgres",
        password = "ONOshokwe5002",
        host = "localhost",
        port = "5432"
    )
cursor = connection.cursor()

def create_db():
    cursor.execute("" \
    "CREATE TABLE IF NOT EXISTS tasks (" \
    "id SERIAL PRIMARY KEY," \
    "title TEXT NOT NULL," \
    "deadline TEXT," \
    "priority TEXT," \
    "completed BOOLEAN DEFAULT FALSE" \
    ")")
    connection.commit()

def add_task():
    title = input("What's the title or brief description of your task? \n")
    deadline = input("When is this due?\n ")
    while(validate_date(deadline) != True):
        deadline = input("Invalid date format! Expected YYYY-MM-DD: \n")
    priority = input("Enter priority- high, mid or low: \n")

    adding = """INSERT INTO tasks (title, deadline, priority)
    VALUES (%s, %s, %s)"""

    cursor.execute(adding, (title, deadline, priority))
    connection.commit()
    print("Task added successfully!\n")

def view_tasks():
    viewing = """SELECT * FROM tasks"""
    cursor.execute(viewing)

    rows = cursor.fetchall()

    print("Here are your tasks:")
    for row in rows:
        print(row)

    connection.commit()
    print("\n")

def mark_complete():
    print("\nWhat task did you complete?\n")
    view_tasks()
    
    choice = int(input(" "))

    completing = """UPDATE tasks SET completed = %s WHERE id = %s"""
    cursor.execute(completing, (True, choice))
    connection.commit()
    print("Good job on completing this task!\n")

def delete_task():
    print("\nSo what are you definitely done with?")
    view_tasks()
    
    choice = int(input(" "))

    checker = input("Are you sure you want to delete this task? Y or N: ")

    if(checker.lower() == "n"):
        return
    
    deleting = """DELETE FROM tasks WHERE id = %s"""

    cursor.execute(deleting, (choice,))
    connection.commit()
    print("Successfully deleted task.\n")

    cursor.execute("ALTER SEQUENCE tasks_id_seq RESTART WITH 1")
    connection.commit()

def validate_date(date):
    pattern = r'^\d{4}[-/]\d{2}[-/]\d{2}$'
    return re.match(pattern, date) is not None

def closer():
    connection.close()