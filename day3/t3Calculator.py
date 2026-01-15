
def add_cal(num1,num2):
    print("Ans :",num1+num2)

def sub_cal(num1,num2):
    print("Ans :",num1-num2)

def mul_cal(num1,num2):
    print("Ans :",num1*num2)

def div_cal(num1,num2):
    if num2 ==0:
        print("Invalid Input")
    else:
        print("Ans :",num1/num2)


while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice=input("Enter Choice :")

    if choice=="5":
        break
        
    num1=int(input("num1 :"))
    num2=int(input("num2 :"))

    if choice=="1":
        add_cal(num1,num2)

    elif choice=="2":
        sub_cal(num1,num2)
    
    elif choice=="3":
        mul_cal(num1,num2)
    
    elif choice=="4":
        div_cal(num1,num2)

    else:
        print("Invalid Input")
