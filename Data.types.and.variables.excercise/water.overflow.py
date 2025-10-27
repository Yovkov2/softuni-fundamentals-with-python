counts = int(input())
capacity = 255
current_water = 0

for _ in range(counts):
    liters = int(input())

    if current_water + liters > capacity:
        print("Insufficient capacity!")
    else:
        current_water += liters

print(current_water)