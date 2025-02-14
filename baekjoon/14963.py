"""
https://www.acmicpc.net/problem/14963
"""

from collections import Counter

N = int(input())
cards_drawn = [int(input()) for _ in range(N)]

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10] * 4 + [10] * 12 + [11] * 4
remaining_deck = Counter(deck)

for card in cards_drawn:
    remaining_deck[card] -= 1
    if remaining_deck[card] == 0:
        del remaining_deck[card]

current_sum = sum(cards_drawn)

X = 21 - current_sum

greater_than_X = sum(count for card, count in remaining_deck.items() if card > X)

total_remaining_cards = sum(remaining_deck.values())

if greater_than_X >= total_remaining_cards - greater_than_X:
    print("DOSTA")
else:
    print("VUCI")
