i=0
while i<=100:
    print(i)
    if(i==3):
        break
    i+=1
print("end of loop")

# continue
i=0
while i<=100:
    print(i)
    if(i==3):
        i+=1
        continue
    i+=1
    print(i)
print("end of loop")