import sqlite3

def add_task(description, priority):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('INSERT INTO tasks (description, priority) VALUES (?, ?)', (description, priority))
    conn.commit()
    conn.close()
import sqlite3

def get_tasks():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks ORDER BY priority DESC')
    tasks = c.fetchall()
    conn.close()
    return tasks
import sqlite3

def filter_tasks(priority):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks WHERE priority >= ? ORDER BY priority DESC', (priority,))
    tasks = c.fetchall()
    conn.close()
    return tasks
while True:
    print('1. Add task')
    print('2. List all tasks')
    print('3. Filter tasks by priority')
    print('4. Quit')
    choice = input('Enter your choice: ')

    if choice == '1':
        description = input('Enter task description: ')
        priority = int(input('Enter task priority (1-5): '))
        add_task(description, priority)
    elif choice == '2':
        tasks = get_tasks()
        for task in tasks:
            print(f'{task[0]}. {task[1]} ({task[2]})')
    elif choice == '3':
        priority = int(input('Enter priority level: '))
        tasks = filter_tasks(priority)
        for task in tasks:
            print(f'{task[0]}. {task[1]} ({task[2]})')
    elif choice == '4':
        break
    else:
        print('Invalid choice')
