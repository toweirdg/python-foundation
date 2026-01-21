#Already Created notes.txt with below lines...
    # with open("notes.txt","a") as src:
    #     src.write("NOTE 1 :\n")
    #     src.write("use to create and write a fileuse to create and write a file")
    #     src.write("\nQuote of the day :")
    #     src.write("\nYou are too Common to sense.")
    #     src.write("\nEnd")


#Menu
while True:
    print("\n1. Create")
    print("2.Read")
    print("3.Exit")

    choose=(input("Choice :"))

    if choose=="1":
        with open("notes.txt","a")as src:
            src.write(input("Write Note ")+ "\n")
        print("Notes Saved.")
    elif choose=="2":
        with open("notes.txt","r")as src:
            content=src.read()
            print("---NOTES---")
            print(content)

    elif choose=="3":
        break

    else:
        print("Invalid Choice")