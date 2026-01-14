print("Enter Your Marks :")
marks=int(input())

if marks<=100 and marks>80:
    print("Grade A")
elif marks<=80 and marks>60:
    print("Grade B")
elif marks<=60 and marks>40:
    print("Grade C")
elif marks<=40 and marks>0:
    print("Grade F")
else :
    print("Invalid Input")
