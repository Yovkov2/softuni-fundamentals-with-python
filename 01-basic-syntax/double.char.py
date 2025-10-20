while True:
    text = input()
    if text == "End":
        break
    if text == "SoftUni":
        continue

    doubled = ""
    for ch in text:
        doubled += ch * 2
    print(doubled)