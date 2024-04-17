import uuid

filename = 'todo-list-data.txt'

def add_task():
    print('\n[ADD TASK]')
    task = input('What is the task? ')
    deadline = input('What is the deadline? ')
    
    try:
        stream = open(filename, 'a')
        stream.write(str(uuid.uuid4()) + ';' + task.replace(';', '') + ';' + deadline.replace(';', '') + '\n')
        stream.close()
    except Exception as e:
        print('Error while adding task:', e)
    finally:
        print()

def complete_task():
    print('\n[COMPLETE TASK]')
    if show_tasks() > 0:
        id_to_delete = input('Enter id to complete: ')
        try:
            stream = open(filename, 'r')
            lines = stream.readlines()
            stream.close()
            stream = open(filename, 'w')
            for line in lines:
                if not line.startswith(id_to_delete):
                    stream.write(line)
            stream.close()
        except Exception as e:
            print('Error while adding task:', e)
        finally:
            print()
    else:
        print('No tasks to complete\n')

def show_tasks():
    print('\n[YOUR TASKS]')
    try:
        stream = open(filename, 'r')
        tasks = stream.readlines()
        if len(tasks) == 0:
            print('Empty list\n')
            return 0
        for task in tasks:
            task_elements = task.split(';')
            print(' | '.join(task_elements), end='')
        print()
        return len(tasks)
    except Exception as e:
        if e.errno == 2:
            print('Empty list\n')
            return 0
        else:
            print('Error while adding task:', e)
            return 0

def show_menu():
    while True:
        print('== TODO LIST ==')
        choice = input('[1] show tasks\n[2] add task\n[3] complete task\n[4] exit\nYour choice: ')

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            break
        else:
            print('Enter a correct number')

if __name__ == '__main__':
    show_menu()

'''
Importing the uuid Module:
The line import uuid at the beginning of the code imports the uuid module.
The uuid module provides functions for generating universally unique identifiers (UUIDs).
UUIDs are unique identifiers that can be used to distinguish objects or entities across different systems.
Defining the filename Variable:
The line filename = 'todo-list-data.txt' assigns the string 'todo-list-data.txt' to the variable filename.
This variable represents the name of the file where task data will be stored.

Creating the add_task() Function:
The add_task() function allows the user to input a task description and its deadline.
It prompts the user for the task and deadline using input().
Inside a try block:
It opens the specified file in append mode ('a').
Writes a new line to the file containing:
A randomly generated UUID (using uuid.uuid4()).
The task description (after removing any semicolons).
The deadline (after removing any semicolons).
Closes the file.
If an error occurs during file I/O, it prints an error message.
The finally block ensures that the file is closed regardless of whether an exception occurred.

Creating the complete_task() Function:
The complete_task() function allows the user to mark a task as completed.
It first checks if there are any tasks to complete (by calling show_tasks()).
If tasks exist:
It prompts the user to enter an ID for the task to be completed.
Reads the existing task data from the file.
Removes the specified task by ID.
Writes the updated data back to the file.
If an error occurs during file I/O, it prints an error message.
The else block handles the case when there are no tasks to complete.

Creating the show_tasks() Function:
The show_tasks() function displays the list of tasks stored in the file.
It reads the file, splits each line into task elements (using semicolons as separators), and prints them.
If the file is empty or an error occurs, appropriate messages are displayed.
The function returns the number of tasks displayed.

show_menu() Function:
This function displays a menu for interacting with the task list.
It runs in an infinite loop (while True) until the user chooses to exit.
The menu options are:
[1] show tasks: Calls the show_tasks() function.
[2] add task: Calls the add_task() function.
[3] complete task: Calls the complete_task() function.
[4] exit: Breaks out of the loop and ends the program.
If the user enters an invalid choice, it prints “Enter a correct number.”
Conditional Block at the End:
The if __name__ == '__main__': block ensures that the code inside it runs only when the script is executed directly (not when imported as a module).
Inside this block, the show_menu() function is called to display the menu and handle user interactions.
'''
