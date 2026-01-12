
message='Hello World'
print(message)#print string 
print(len(message)) #length of the string
print(message[:5]) # can be written as[0:5]or[:5]or [0:] ~ cause of end is not included
print(message[6:]) # can be written as [6:11]or[6:]or[:11] ~ cause end is not included
#methodsORfunctions are same as just function belong to an object.
print(message.lower()) #changestolowercase
print(message.upper()) #changestouppercase
print(message.count('l')) #countno.of characters
print(message.find('World')) #find the characters

greetings='Hello'
name='Michael'
new_message='{},{}. Welcome!'.format(greetings,name)
print(new_message)
print(dir(name))#directory of attributes of that variable