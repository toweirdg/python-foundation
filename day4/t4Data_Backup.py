with open("notes.txt","r") as src:
    with open("notes_backup.txt","w") as dbUP:
        for line in src:
            dbUP.write(line)
        

print("Backup Created.")