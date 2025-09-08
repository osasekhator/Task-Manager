# 📝 Student Task Manager
A simple command-line-based Task Manager built with Python and PostgreSQL. It helps students organize tasks by allowing them to add, view, complete, and delete tasks with deadlines and priorities.

# 🚀 Features
✅ Add new tasks with deadlines and priorities
👀 View all current tasks
✔️ Mark tasks as complete
🗑️ Delete tasks with confirmation
🔁 Automatically reset task ID if all tasks are deleted
🧠 Simple date validation (YYYY-MM-DD format)
🛠️ Technologies Used
Python 3
PostgreSQL
psycopg2 (PostgreSQL adapter for Python)
# 📦 Requirements
Python 3.8 or above
PostgreSQL installed and running locally
Required Python packages:
pip install psycopg2
# 📌 Notes
Dates must be entered in the format: YYYY-MM-DD

Task id auto-increments using PostgreSQL's sequence feature

If all tasks are deleted, the task ID sequence is reset to start from 1

Deleting individual tasks will not reset the sequence unless the table becomes empty

Task data is stored persistently in PostgreSQL and will remain until manually deleted

# 🧑‍💻 Author
Osadebamwen Onoshokwe Ekhator (Osas) Student Software Engineer, passionate about building helpful tools that elevate the living experiences of people worldwide 📧 Email: osadebamwen.ekhator@gmail.com 🐙 GitHub: github.com/osasekhator

# 📜 License
This project is for educational purposes and is open-source under the MIT License.
