# Enter the password in the floating window

password = input()
#password should contain atleast two of below symbols and two numbers
symbols = ('!','@','#','$','%','&','*','?','/','+',',','_',':',';',
           '|')
numbers = ('0','1','2','3','4','5','6','7','8','9')

symbols_count = 0
numbers_count = 0

if len(password)<7:
    print("Password must contain atleast 7 characters!")

for x in password:
    if x in symbols:
        symbols_count +=1
    if x in numbers:
        numbers_count +=1

if len(password)>=7:
    if symbols_count >=2 and numbers_count>=2 :
        print("Strong")
    else:
        print("Weak")