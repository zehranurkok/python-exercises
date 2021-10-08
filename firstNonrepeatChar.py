string = input("Write a string: ")
list = list(string)
y = [None] * len(list)

for i in range(len(list)):
    y[i] = list.count(list[i])

for i, element in enumerate(list):
    if i == len(list) -1 and y[i] > 1:
        print(-1) 
        
    elif y[i] == 1: 
        print(element, "first non-repeat character in", i, ". element of string")
        break  
               

