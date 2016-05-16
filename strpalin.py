#https://www.codechef.com/viewsolution/9959096

testcases = int(raw_input())
if(testcases<1 or testcases>10):
    exit()
for i in range(0, testcases):
    A=raw_input()
    B=raw_input()
    if(len(A)<1 or len(A)>1000 or len(B)<1 or len(B)>1000):
    	exit()
    i = 0
    j = 0
    flag = 0;
    if (len(A)>=26 and len(B)>=26):
        while i < 26:
            while j < 26:
                if A[i]==B[j]:
                    flag = 1
                    break
                else:
                    flag = 0
                j += 1
            i+=1
            if flag == 1:
                    break  

    if(len(A)<26 and len(B)>26):
        while i < len(A):
            while j < 26:
                if A[i]==B[j]:
                    flag = 1
                    break
                else:
                    flag = 0
                j += 1
            i+=1
            if flag == 1:
                    break

    if(len(A)>26 and len(B)<26):
        while i < len(B):
            while j < 26:
                if B[i]==A[j]:
                    flag = 1
                    break
                else:
                    flag = 0
                j += 1
            i+=1
            if flag == 1:
                    break    

    if(len(A)<26 and len(B)<26):
        if len(A)<len(B):
            while i < len(A):
                while j < len(B):
                    if A[i]==B[j]:
                        flag = 1
                        break
                    else:
                        flag = 0
                    j += 1
                i+=1
                if flag == 1:
                    break

        elif len(A)>=len(B) :
            while i < len(B):
                while j < len(A):
                    if(B[i] == A[j]):#KUCH LOAD HAI!!!!!!!!!!!!!!!!!!!!!!!!
                        flag = 1
                        break
                    else:
                        flag = 0
                    j += 1
                i+=1
                if flag == 1:
                    break


    if flag == 1:
        print ("YES")
    else:
        print ("NO")
