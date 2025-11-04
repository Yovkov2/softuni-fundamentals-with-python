factor = int(input())
count = int(input())

factor = abs(factor)
result = []

for i in range(1, count + 1):
    result.append(i * factor)

print(result)