#!/usr/bin/env python
minm = -1000000000
maxm = 1000000000
testcases = int(raw_input())
if(testcases<1 or testcases>10):
    exit()
for i in range(0, testcases):
    N = int(raw_input())
    if(N<1 or N>pow(10,5)):
    	exit()
    numbers = map(int,raw_input().split(" "))
    listing = []
    for j in range(0, (len(numbers)-1)):
        count = 1
        for k in range(j, (len(numbers)-1)):
            if (numbers[k]*numbers[k+1]<0):
                count += 1
            else:
                break
        listing.append(count)
    listing.append(count)
    print ' '.join(str(a) for a in listing) 



