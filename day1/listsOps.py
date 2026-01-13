# lists
course = ['Chemistry','Math','Physics', 'CompSci']
course_new=['Art','Education']
# print(course[:2])same as other
# print(course[2:])#2nd to last no need to cuz last not included
#negative list
# print(course[-1])#last element from list

#modifying list

# course.insert(0,'Arts') add to list
# course.extend(course_new) #extend list by adding each other
# # course.remove('Math')#remove from list
# popped=course.pop() #extract last ele from list
# print(course)#print list
# # print(popped)#print popped element

#Sorting List
# num=[6,4,2,5,1,3]
# course.sort()
# # print(course)
# # num.sort()
# # print(num)
# # num.sort(reverse=True)
# # print(num)

#finding value
# print(min(num))
# print(max(num))
# print(sum(num))
# print(course.index('CompSci'))
# print('Art' in course)

#looping
# for index, courses in enumerate(course,start=1):
#     print(index,courses)

course_str=', '.join(course)
print(course_str)
new_list=course_str.split(', ')
print(new_list)