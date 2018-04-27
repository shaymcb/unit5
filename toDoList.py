#Shaylee McBride
#27Apr2018
#toDoList.py

def add(task):
    toDo.append(task)

def delete(task):
    toDo.remove(task)

toDo = []
print('Valid commands = add, delete, print, quit')

while True:
    task = input('')
    if task == 'quit':
        break
    elif task == 'print':
        for item in toDo:
            print(item)
    task = task.split(' ')
    
    if 'add' in task:
        toDo.append(task[1:])

