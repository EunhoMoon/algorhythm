"""
https://www.acmicpc.net/problem/1343
"""

board = input().strip()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if "X" in board:
    print(-1)
else:
    print(board)
