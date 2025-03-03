from operator import itemgetter

listTasks = []
input_answer = ''

# Function to sort the list
def sort_list():
    global listTasks
    listTasks = sorted(listTasks, key=itemgetter(1))
    
# Function to add a task to the list
def add_task():
    taskName = input('Task Name= ')
    while True:
        try:
            priorityTask = int(input('Task Priority (1 and 3)= '))
            if 1 <= priorityTask <= 3:
                listTasks.append((taskName, priorityTask))
                sort_list()
                break
            else:
                print("Use a number between 1 and 3")
        except:
            print("Use a number")

# Function to delete a task from the list
def delete_task():
    taskDelete = input("Which task would you like to delete? = ")
    task_found = False
    for task in listTasks:
        if task[0] == taskDelete:
            listTasks.remove(task)
            sort_list()
            task_found = True
            break
    if not task_found:
        print("Task is not known in list")

while input_answer != 'quit':
    input_answer = input('What would you like to do? (Add task, Delete task or Quit)')
    if input_answer == 'Add task':
        add_task()
    elif input_answer == 'Delete task':
        delete_task()
    elif input_answer == 'Quit':
        sort_list()
        print('List of Tasks:' + str(listTasks))
        break
    else:
        print('Use one of the exact following Add task, Delete task or Quit')
