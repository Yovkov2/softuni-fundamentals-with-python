first_num = int(input())
second_num = int(input())
three_num = int(input())

def sum_numbers(first, second):
    return  first + second
def subtract(result, third):
    return result - third
def add_and_subtract(first, second, third):
    result = sum_numbers(first, second)
    final_result = subtract(result, third)
    print(final_result)

add_and_subtract(first_num,second_num,three_num)