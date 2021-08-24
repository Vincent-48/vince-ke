#Random otp create
import secrets as se
otp = ''
for i in range(6):
    otp+=se.choice('1234567890')
print(otp)