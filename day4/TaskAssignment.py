
todo=[]

def print_todo():
    for i in range(len(todo)):
        print(f"{i+1}. {todo[i]}")

if len(todo)==0:
    print("Your to-do list is empty. Let's add some tasks")
    for i in range(1,6):
        print(f"Enter task {i}:")
        task = input()
        todo.append(task)
    print_todo()
else:
    for e in todo:
        print(e)


user_input=input("Do you want to continue managing your todo list")
while user_input.lower()=="yes":
    task_completed=input("Enter the task completed")

    if todo.__contains__(task_completed):
        ind = todo.index(task_completed)
        todo[ind]= task_completed +" completed"
    else:
        print("Enter the task present in todo list")
    print_todo()
    user_input = input("Do you want to continue managing your todo list")
else:
    print_todo()

