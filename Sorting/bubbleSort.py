# This is a simple implementation of bubble sort in python
#Strings In Dictionary Order
data = ['selen','mango', 'masala', 'apple', 'samsonite' ]
data=[10,101,1,100,11]
for i in range(len(data)):
    for j in range(len(data)-1-i):# Why here -1 and -i because in every pass one element is sorted so we can ignore that element in next pass 
        if data[j]>data[j+1]:#If adhjacent elements are not in order then swap them
            data[j],data[j+1]=data[j+1],data[j]#Generic Swap In Python
print(data)
#Output: [1, 10, 11, 100, 101]
#Output: ['apple', 'mango', 'masala', 'selen', 'samsonite']