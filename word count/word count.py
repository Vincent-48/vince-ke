txt = input("Word Count is:")
count = 0
for word in txt:
    if word == ' ':
        count = count + 1
count = count + 1

print(count)