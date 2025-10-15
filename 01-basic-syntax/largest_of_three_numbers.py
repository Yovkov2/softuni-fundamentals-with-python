firtst_num = int(input())
second_num = int(input())
third_num = int(input())

if firtst_num > second_num and firtst_num > third_num:
    print(firtst_num)
elif second_num > firtst_num and second_num > third_num:
    print(second_num)
elif third_num > firtst_num and third_num > second_num:
    print(third_num)