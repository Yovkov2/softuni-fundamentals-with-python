divisor = int(input())
bound = int(input())

N = bound - (bound % divisor)
print(N)