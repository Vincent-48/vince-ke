# numbers of steps you need to get from 1 to number of input. Steps are *2 or +1

print(len(b:=bin(int(input()or "7"))[3:]) + b.count("1"))