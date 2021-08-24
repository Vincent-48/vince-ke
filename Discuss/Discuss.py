""" it's for discuss' """

def func():
    x = 1
    def inner_func():
        pass
    return x

print(func.__dict__) #nothing to input

func.temp = 1 #what's it? Attribute?
func.x = 3    #why x not change within func?
print()
print(func())
print()


print(func.__dict__) #now it is Show temp,why?