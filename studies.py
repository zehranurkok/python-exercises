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
# !!! code output is ['y', False, 'x'] [2, False, 'x'] 


# for -> start, stop, step
for i in range(1,10,0): #error
    print(i)

for i in range(10,-2,-1): 
    print(i)


# enumerate function
x = [2,50,71,6,88,96]
for i, element in enumerate(x):
    print(i, element)

# output
# 0 2
# 1 50
# 2 71
# 3 6
# 4 88
# 5 96


i = 0
while True:
    print('okay')
    i += 1
    if i == 5:
        break


# sliced
x = [0,1,2,3,4,5,6,7,8,9]
y = ['zehra', 'cihan', 'serap', 'ahmet']
z = 'zehra'

# sliced = x[start:stop:step]
sliced1 = x[0:4:1]
sliced2 = y[0:3:2]
sliced3 = z[0:3]
sliced4 = z[::2]

print(sliced1)
print(sliced2)
print(sliced3)
print(sliced4)
# x[:4] stop 4th index
# x[2:] start from 2nd index and go to the end
# x[::-1] print in reverse

# output
# [0, 1, 2, 3]
# ['zehra', 'serap']
# zeh
# zha

# example for sliced (tuple ver.)
sliced =  (4,65,635,1,8,516,58,33) [::-3]
print(sliced)

# output
# (33, 8, 65)

# dictionary
x = set()
y = {1, 2, 3, 4}
z = {1, 5, 6 ,7}
y.add(5)
y.remove(3)
print(y)
print(2 in y) # True or False?
print(3 in y) # True or False?
print(y.union(z)) # combination
print(y.difference(z))
print(y.intersection(z)) # cross

# output
# {1, 2, 4, 5}
# True
# False
# {1, 2, 4, 5, 6, 7}
# {2, 4}
# {1, 5}"""


