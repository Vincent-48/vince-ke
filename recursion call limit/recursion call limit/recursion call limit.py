def recursion_limit(x=1):
    try: return recursion_limit(x+1)
    except: return x

print(
    "recursion call limit: ",
    recursion_limit()
)
