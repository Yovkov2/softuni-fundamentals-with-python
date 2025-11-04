cards = input().split()
shuffles = int(input())

for _ in range(shuffles):
    half = len(cards) // 2
    left_half = cards[:half]
    right_half = cards[half:]

    shuffled = []
    for i in range(half):
        shuffled.append(left_half[i])
        shuffled.append(right_half[i])

    cards = shuffled

print(cards)