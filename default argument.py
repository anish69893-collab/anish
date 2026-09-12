# default argument
def name( fname,mname="Rahul", lname="Whatname"):
    print("hello", fname,mname,lname)
name("Rohan", "Agrawal","Soni")

# Average 
def calc_Average(a=98,b=90):
    print("The average", a+b/9)

calc_Average(b=78)

# Keyword argument
def calc_Average(a=98,b=90):
    print("The average", a+b/9)

calc_Average(b=78 ,a=67)

# Required argument
def calc_Average(a,b=90):
    print("The average", a+b/9)

calc_Average(a=20)
