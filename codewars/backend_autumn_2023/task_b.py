cards = {
    'A': {},
    'B': {}
}

diversity = 0

n, m, q = map(int, input().split())

# stage a
for number in input().split():
    cards['A'][number] = cards['A'].get(number, 0) + 1
    diversity += 1

# stage b
for number in input().split():
    temp = abs(cards['B'].get(number, 0) - cards['A'].get(number, 0))

    cards['B'][number] = cards['B'].get(number, 0) + 1

    after_temp = abs(cards['B'].get(number, 0) - cards['A'].get(number, 0))

    diversity += after_temp - temp

# stage c
diversity_change = []
for _ in range(q):
    type_card, player, card = input().split()
    type_card = int(type_card)

    temp = abs(cards['B'].get(card, 0) - cards['A'].get(card, 0))

    cards[player][card] = cards[player].get(card, 0) + type_card

    after_temp = abs(cards['B'].get(card, 0) - cards['A'].get(card, 0))

    diversity += after_temp - temp
    diversity_change.append(diversity)

print(*diversity_change)