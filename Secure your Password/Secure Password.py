secPass = (("and","&"),("a","@"),("s","$"))
def securePass (password):
    for a,b in secPass :
        password = password.replace(a,b)
    return password
password = input ()
paassword = password.lower()
securedPassword = securePass (paassword)
print (f"Secured password is{securedPassword}")