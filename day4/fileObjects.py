#File Objects

# f=open('text.txt','r')
# print(f.name)
# f.close()

with open('text.txt','r') as f:
    f_contents=f.read()
    print(f_contents,end=" ")