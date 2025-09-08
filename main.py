import database

def menu():
    
    print("What would you like to do?")
    print("1. Add tasks")
    print("2. View tasks")
    print("3. Mark task as complete")
    print("4. Delete task")
    print("5. Exit\n")

    choice = int(input("Enter your choice:\n "))
    while(choice < 1 or choice > 5):
        choice = int(input("Invalid input! Enter your choice:\n "))
    
    match choice:
        case 1:
            database.add_task()
        case 2:
            database.view_tasks()
        case 3:
            database.mark_complete()
        case 4:
            database.delete_task()
        case 5:
            print("Goodbye!")
            return False
    return True

if __name__ == '__main__':
    database.create_db()
    print("Welcome to your Task Manager\n")
    running = True
    while(running):
        running = menu()
    database.closer()