numbers = input().split(", ")

def is_palindrome(num):
    return num == num[::-1]
for n in numbers:
    print(is_palindrome(n))
    