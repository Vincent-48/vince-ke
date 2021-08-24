#function to calculate x raised to the power of y
def power(x, y):

    if y == 0:
        return 1
    if y % 2 == 0:
        return  power(x, y // 2)
    return x * power(x, y // 2)

#function to calculate order of the number
def order(x):

    #variable to store of the number
    n = 0
    while(x !=0):
        n = n + 1
        x = x // 10
    return n