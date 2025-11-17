numbers = input().split()

even_numbers = list(filter(lambda x: int(x) % 2 == 0, numbers))
even_numbers = [int(x) for x in even_numbers]

print(even_numbers)