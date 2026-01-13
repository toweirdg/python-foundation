student={'name':'nakul','age':28,'courses':['Math','CompSci']}
# print(student['courses'])
student['phone']='9779-6578'
# print(student)
student.update({'name':'neha','age':25,'phone':'9669-6577'})

# del student['age']#delete

# age=student.pop('age')#remove key
# print(student)
# print(age)#give value of the removed key
# print(len(student))#length of keys 
# print(student.keys())#keys
# print(student.values()) #give values
# print(student.items())#give pairs of key and values

for keys,values in student.items():
    print(keys,values)
