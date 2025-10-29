n = int(input())
positive = []
negatives = []

for n in range(n):
    current_number = int(input())
    if current_number >= 0:
        positive.append(current_number)
    else:
        negatives.append(current_number)

print(positive)
print(negatives)
print(f"Count of positives: {len(positive)}\nSum of negatives: {sum(negatives)}")