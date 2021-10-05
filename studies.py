"""print("Hello", 2, False, end='\n')
print("Hi")

# etc 

print("Hello", 2, False, end='|')
print("Hi")

x=4
y=2
print(x/y) # output is float not int

# Use // for int output in division

x = "HeLLo WorlD"
print(x.lower().count('l'))

print(ord('Z')) # ord() function give us the ASCII number of Z 

print('ab'> 'ad') # False because d's ASCII number is grather than b's

# use and or not operators
# order of precedence not>and>or

result1 = 4>5
result2 = 5==5

result3 = result1 or result2
result4 = result1 and result2
result5 = not result1 and result2

print(result3)
print(result4)
print(result5)

print(not(False and True))

# append etc extend

list1 = [1, 2, 3]
list1.append([4, 5, 6])

# or 

list2 = [1, 2, 3]
list2.extend([4, 5, 6])

print(list1)
print(list2)

# use of pop

x = [1,2,3,4]
print(x.pop())
print(x)

y = [1,2,3,4]
print(y.pop(0))
print(y)

# example

x = [2, False, 'x']
y = x
x[0] = 'y'
print(x,y)
# !!! code output is ['y', False, 'x'] ['y', False, 'x'] 

# etc 

x = [2, False, 'x']
y = x[:] # copies the list
x[0] = 'y'
print(x,y)
# !!! code output is ['y', False, 'x'] [2, False, 'x'] """
