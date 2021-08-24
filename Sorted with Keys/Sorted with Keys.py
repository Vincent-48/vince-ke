lst1 = ["abc", "1334", "ca*!?"]
print(sorted(lst1))
# sort by length
print(sorted(lst1, key=len))

lst2 = [(1,3), (2,4), (3,0)]
print(sorted(lst2))
# sort by second element
print(sorted(lst2, key = lambda x: x[1]))