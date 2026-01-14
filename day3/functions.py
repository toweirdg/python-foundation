# def hello_func(greeting,name='You'):
#     return'{},{}'.format(greeting,name)

# print(hello_func('Hi',"Corey"))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

# student_info('Math','Art',name='John' , age=20)

course=['Math','Art']
info={'name':'john', 'age':20}
student_info(*course,**info)