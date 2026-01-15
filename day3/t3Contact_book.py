contact={} #empty dictionary

def add_contact(name,phone):
    contact[name]=phone #Store the phone number under the name key
    print("Contact Added.")


def search_contact(name):
    if name in contact :
        print("phone :", contact[name])
    else:
        print("contact not found")


def show_all():
    for name, phone in contact.items():
        print(name,":",phone)



while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Show All")
    print("4. End")


    choice=input("Enter Choice :")
    if choice=="1":
        name=input("Name:")
        phone=input("Phone :")
        add_contact(name,phone)
    elif choice=="2":
        name=input("Enter a Name :")
        search_contact(name)
    elif choice=="3":
        show_all()
    elif choice=="4":
         break
    else:
        print("Invalid Choice")
