def calc_avg(a,b,c):
    if a>b and a>c:
        print(a,"greater")
    elif b>a and b>c:
        print(b," greater")
    else:
        print(c,"greater")
    Gmean=(a+b+c)/(a*b*c)
    avg=Gmean/8
    print(avg)
    return avg
calc_avg(68,67,65)

# More line of code
calc_avg(98,34,56)
print(type(calc_avg))



