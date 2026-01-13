#list[]
# list_1 = ['Chemistry','Math','Physics', 'CompSci']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0]='Art'
# print(list_1)
# print(list_2)

#Tuples()
# tuple_1 = ('Chemistry','Math','Physics', 'CompSci')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)
# #Immutable 
# tuple_1[0] ='Art'
# print(tuple_1)
# print(tuple_2)

#Sets{}-- unordered and no duplicate //don't care about order, throw-away duplicates
cs_courses = {'History','Math','Physics', 'CompSci'}
art_course = {'History', 'Math','Art','Design'}

print(cs_courses)
#common 
print(cs_courses.intersection(art_course))
#uncommon
print(cs_courses.difference(art_course))
#combine
print(cs_courses.union(art_course))

#emptyLists
empty_list=[]
empty_list=list()

#emptyTuples
empty_tuple=()
empty_list=tuple()

#emptySets
empty_sets={}# this isn't right, It creates dictionary
empty_sets=set()