a = [1,2,3]

print(a,a[:])
print(a is a[:])
# False But Why ??

print(id(a),id(a[:]))

"""
got the answer

a == a[:]
returns True
because '==' compares values

while

a is a[:]
returns False
because 'is' compares memory addresses



"""