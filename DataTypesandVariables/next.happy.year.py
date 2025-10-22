year = int(input())

year += 1
while True:
    s = str(year)
    if len(set(s)) == len(s):  
        print(year)
        break
    year += 1
