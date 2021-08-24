from random import randint
b = randint(50,100)
def secret(m,n):
    m = m+2
    if m >= n:
        return m-1
    return secret(m,n)-1

print(secret(0,b))