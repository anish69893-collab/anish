# keyword Arbitrary
def calc_average(*number):
    sum=0
    for i in number:
        sum=sum+i
        print("Average is", sum/len(number))
calc_average(5,9)        