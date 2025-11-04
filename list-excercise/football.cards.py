line = input().strip()

a_players = 11
b_players = 11

sent_off_a = set()
sent_off_b = set()

terminated = False

cards = line.split() if line else []

for card in cards:

    team, num_str = card.split('-')
    num = int(num_str)

    if team == 'A':
        if num not in sent_off_a:
            sent_off_a.add(num)
            a_players -= 1
    else:
        if num not in sent_off_b:
            sent_off_b.add(num)
            b_players -= 1


    if a_players < 7 or b_players < 7:
        terminated = True
        break

print(f"Team A - {a_players}; Team B - {b_players}")
if terminated:
    print("Game was terminated")