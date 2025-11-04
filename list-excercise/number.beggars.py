numbers = list(map(int, input().split(", ")))
beggars_count = int(input())

result = [0] * beggars_count

for index in range(len(numbers)):
    beggar_index = index % beggars_count
    result[beggar_index] += numbers[index]

print(result)