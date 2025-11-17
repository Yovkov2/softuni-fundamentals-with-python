first_num = int(input())
second_num = int(input())
three_num = int(input())

def solve(first,second,third):
    result = 0
    if first < second and first < third:
        result = first
    elif second < first and second < third:
        result = second
    elif third < first and third < second:
        result = third
    return  result

print(solve(first_num,second_num,three_num))