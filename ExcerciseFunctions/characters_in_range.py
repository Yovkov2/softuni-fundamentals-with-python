first_char = input()
second_char = input()

def solve(ch1, ch2):
    result = []
    for i in range(ord(ch1) + 1, ord(ch2)):
        result.append(chr(i))
    return ' '.join(result)

print(solve(first_char,second_char))