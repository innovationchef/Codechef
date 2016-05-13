#!/usr/bin/env python

testcases = int(raw_input())
if(testcases<1 or testcases>100):
    exit()
for i in range(0, testcases):
    N = int(raw_input())
    if(N<1 or N>pow(10,9)):
    	exit()
    sum = 0
    summation = []
    j = 0
    while sum <= N : 
	    sum = sum + j
	    summation.append(sum) 
	    j = j+1 
    print(j-2)



