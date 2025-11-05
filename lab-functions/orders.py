product = input()
counts = int(input())

def solve(products, number_count):
    result = 0
    if products == 'coffee':
        result = number_count * 1.50
    elif products == 'water':
        result = number_count * 1
    elif products == 'coke':
        result = number_count * 1.40
    elif products == 'snacks':
        result = number_count * 2
    return f"{result:.2f}"

print(solve(product,counts))
