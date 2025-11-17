num = int(input())

def odd_and_even_sum(number):
    odd_sum = 0
    even_sum = 0

    for digit in str(number):
        digit = int(digit)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

print(odd_and_even_sum(num))