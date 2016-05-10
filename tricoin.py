#!/usr/bin/env python

testcases = input("Enter no. of testcases --->  ")
for i in range(0, testcases):
    N = input("input the no. of coins --->")
    sum = 0
    summation = []
    j = 0
    while sum <= N : 
	    sum = sum + j
	    summation.append(sum) 
	    # print(summation[j])
	    j = j+1 
	print(j - 2)



