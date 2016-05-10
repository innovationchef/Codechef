#!/usr/bin/env python
N = 0
summation = 0
initialProduct = 0
endProduct = 0

def addToEnd(inputList, x):
    y = x 

    testList1 = inputList[:]
    global endProduct
    product1 = testList1[-1]*numbers[x]
    product2 = testList1[0]*numbers[x]
    endProduct += product1 + product2
    testList1.append(numbers[x])
    x = x+1
    if x == N:
    	endProduct -= (product1 + product2)/2
    if x<N : 
        addToEnd(testList1, x)
    
    testList2 = inputList[:]
    global initialProduct 
    product1 = testList2[-1]*numbers[y]
    product2 = testList2[0]*numbers[y]
    initialProduct += product2 + product1
    testList2.insert(0, numbers[y])
    y = y+1
    if y == N : 
    	initialProduct -= (product2 + product1)/2
    if y<N : 
    	addToEnd(testList2, y)

    return(endProduct+initialProduct) 

testcases = input("Enter no. of testcases --->  ")
for i in range(0, testcases):
    N = input("input the no. of numbers --->")
    numbers = []
    for j in range(0, N):
    	numbers.append(input("Enter numbers ---> "))
    testList = [numbers[0]]
    
    print(addToEnd(testList, 1))
    #print(endProduct+initialProduct)
    
    