def getmin(listing, rate_list):
    x = -1
    k = 1
    maxm = -1
    difference = 0
     # for p in listing: print p
    while k<len(listing):
        if listing[x] == listing[x-k]:
            if cmp(rate_list[x], rate_list[x-k]) > 0:
                if rate_list[maxm]>=rate_list[x]:
                    continue
                else:
                    maxm = -1
            elif cmp(rate_list[x], rate_list[x-k]) < 0:
                temp_max = x-k
                old_difference = difference
                difference = rate_list[x-k] - rate_list[x]
                if difference>old_difference :
                    maxm = x-k
                else:
                    maxm = temp_max
            elif cmp(rate_list[x], rate_list[x-k]) == 0:
                maxm = x-k
        else :
            return(len(listing) + maxm + 1)
        k += 1
        return(len(listing) + maxm + 1)

    # for k in range(0, len(listing)):
            

testcases = int(raw_input())
if(testcases<1 or testcases>5):
    exit()
for i in range(0, testcases):
    n = int(raw_input())
    if(n<1 or n>100):
        exit()
    length_list = map(int,raw_input().split(" "))
    rating_list = map(int,raw_input().split(" "))
    if(len(length_list)<1 or len(length_list)>100 or len(rating_list)<1 or len(rating_list)>100):
        exit()
    product = 0
    product_list = []
    j = 0
    while  j<n:
        product = length_list[j]*rating_list[j]
        product_list.append(product)
        j += 1
    print(getmin(product_list, rating_list))
    # for p in product_list: print p




