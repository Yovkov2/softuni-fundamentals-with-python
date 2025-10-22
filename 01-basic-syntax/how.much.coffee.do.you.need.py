coffee = 0

while True:
    event = input()
    if event == "END":
        break
    event_lower = event.lower()

    if event_lower in ["coding", "dog", "cat", "movie"]:
        if event.isupper():
            coffee += 2
        else:
            coffee += 1

if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)