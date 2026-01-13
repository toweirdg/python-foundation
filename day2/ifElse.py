print("Enter Language:")
language=str(input())
if language=='java':
    print('Language is Java')
elif language=='python':
    print('Language is Python')
elif language=='typescript':
    print('Language is TypeScript')
else:
    print('No Match')

user='Admin'
logged_in=True

if user=='Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if not logged_in:
    print('Please login')
else:
    print('Welcome')

#is-- Object Identifier
a=[1,2,3]
b=[1,2,3]
# a=b

print(a==b)
print(a is b)
print(id(a))
print(id(b))

#False Values
# --False
# --None
# --0 
# --empty sequence'',[],()
# --empty mapping {}

condition=10
if condition:
    print('Evaluted to True')
else:
    print('Evaluted to False')
