#This program take the first letter of each word and put it on the end, then add 'ay'
#to the end of that. ("road" = "oadray")

#This is Pig Latin

txt = input('Please Enter your TXT in English: ')
q = txt.split()
w = (q[0][1:]+q[0][0]+'ay ')
for i in q[1:]:
    w+=i[1:]+i[0]+'ay'print(w)
