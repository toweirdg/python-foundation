nums=[1,2,3,4,5]
for num in nums:
    if num==3:
        print('Found it!')
        continue #orbreak
    for letters in 'abc':
        print(num,letters)

for i in range(1,11):#doesn't include last value
    print(i)