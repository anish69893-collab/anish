# Break
nums=[2,3,5,9,12,45,39,23,78,90,100,]

x=90

idx=0
while idx<len(nums):
    if(nums[idx]==x):
        print("FOUND",idx)
        break
    else:
        print("finding")

    idx+=1

# continue
nums=[2,3,5,9,12,45,39,23,78,90,100,]

x=90

idx=0
while idx<len(nums):
    if(nums[idx]==x):
        print("FOUND",idx)
        idx+=1
        continue
    else:
        print("finding")

    idx+=1