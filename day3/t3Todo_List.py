tasks=[]

def add_task(task):
    tasks.append(task)
    print("Task Added")


def remove_task():
    if not tasks:
        print("No tasks to remove")
        input("Press Enter to continue...")
        return
    show_tasks()
    num=int(input("Enter task number to remove "))
    if num>0 and num<=len(tasks):
        removed=tasks.pop(num-1)
        print("Removed",removed)
    
    else:
        print("Invalid number")
    input("Press Enter to continue...")

def show_tasks():
    if not tasks:
        print("No tasks to remove")
    else:
        for i in range(len(tasks)):
            print(i+1,".",tasks[i])

def main():
    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Show Task")
        print("4. Exit")

        choice=input("Enter Choice :")

        if choice=="1":
            task=input("Enter task :")
            add_task(task)

        elif choice=="2":
            remove_task()

        elif choice=="3":
            show_tasks()
            input("Press Enter to continue...")

        elif choice=="4":
            break
        else :
            print("Invalid Choice")
main()