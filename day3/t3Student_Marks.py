
student_marks={}

def add_students(name,marks):
    student_marks[name]=marks
    print("Student Added.")

def calculate_average():
    if not student_marks:
        print("Student Not Found")
        input("Press Enter to Continue....")
        return

    total= sum(student_marks.values())
    average=total/ len(student_marks)
    print("Average :",average)
    input("Press Enter to Continue....")

def show_topper():
    if not student_marks:
        print("Student Not Found")
        input("Press Enter to Continue....")
        return
    
    topper=max(student_marks, key=student_marks.get)
    print("Topper :",topper,"Marks",student_marks[topper])
    input("Press Enter to Continue....")

def show_all():
    for name,marks in student_marks.items():
        print(name,":",marks)
        input("next..")

while True:
    print("\n1. Add")
    print("2. Average")
    print("3. Topper")
    print("4. Show_All")
    print("5. Exit")

    choice=input("Enter Choice :")

    if choice=="1":
        name=input("Name :")
        marks=int(input("Marks :"))
        add_students(name,marks)
    
    elif choice=="2":
        calculate_average()

    elif choice=="3":
        show_topper()

    elif choice=="4":
        show_all()
    
    elif choice=="5":
        break

    else:
        print("Invalid Input")
