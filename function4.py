def calc_gmean( a,b): # parameters
    sum=(a+b)*(a-b)
    print(sum)
def calc_isGreater(a,b):# parameters
    if a>b:
        print("first number is greater ")
    else:
        print(" second number is greater")
a=56
b=65
calc_isGreater(a,b)# function call: argument
calc_gmean(a,b) # function call: argument
c=98
d=78
calc_isGreater(c,b) # function  call: argument
calc_gmean(c,d) # function call: argument
