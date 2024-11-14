"""
https://www.acmicpc.net/problem/29864
"""
import sys

input = sys.stdin.readline

players = input().split()
winners = input().split()
results = []

while len(winners) > 1:
    players = players
    next_players = []
    round_winner: str

    for i in range(0, len(players), 2):
        round_winner = players[i] if players[i] in winners else players[i + 1]
        next_players.append(round_winner)
        winners.remove(round_winner)

    players = next_players
    results.append(players)

print(winners[0])
print(" ".join(results[-1]))
print(" ".join(results[-2]))
