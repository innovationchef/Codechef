summation = 0
initialProduct = 0
endProduct = 0

def addToEnd(inputList, x):
    y = x 

    testList1 = inputList[:]
    testList2 = inputList[:]

    global endProduct
    product1 = testList1[-1]*numbers[x]
    endProduct += product1 * pow(2, N-x)
    testList1.append(numbers[x])
    x = x+1
    if x == N:
        x=x
    if x<N : 
        addToEnd(testList1, x)
    
    product2 = testList2[0]*numbers[y]
    endProduct += product2 * pow(2, N-y)
    testList2.insert(0, numbers[y])
    y = y+1
    if y == N : 
        y=y
    if y<N : 
        addToEnd(testList2, y)

    # return(endProduct+initialProduct) 

testcases = int(raw_input())
for i in range(0, testcases):
    N = int(raw_input())
    numbers = map(int,raw_input().split(" "))
    testList = [numbers[0]]
    addToEnd(testList, 1)
    print(endProduct/2)
    #print(endProduct+initialProduct)
    
    