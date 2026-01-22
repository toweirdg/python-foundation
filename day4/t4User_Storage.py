username=str(input("Username :"))
password=str(input("Password :"))

with open("users.txt","a") as f:
    f.write(username + "," + password + "\n")

print("User Saved.")

