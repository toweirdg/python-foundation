
def save_data(text):
    file=open("data.txt","a")
    file.write(text+"\n")
    file.close()
    print("Data Saved")

def load_data():
    try:
        file=open("data.txt","r")
        print("\n Saved Data :")
        for line in file:
            print(line.strip())
        file.close()
    except:
        print("No Data Found")

def main():
    while True:
        print("\n1. Save File")
        print("2. Load File")
        print("3. Exit")

        choice=input("Enter Choice :")

        if choice=="1":
            text=input("Enter Data to save :")
            save_data()
        
        elif choice=="2":
            load_data()
            input("Press Enter to continue...")
        
        elif choice=="3":
            break

        else:
            print("Invalid Choice")



main()