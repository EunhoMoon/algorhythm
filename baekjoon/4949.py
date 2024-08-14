"""
https://www.acmicpc.net/problem/4949
"""
import sys

input = sys.stdin.readline

result = []

s = ["(",")","[","]"]

while True:
    command = str(input()).rstrip()
    chars = []
    if command == ".":
        break
    else:
        stk: list = []
        is_vps = True
        chars = [word for word in list(command) if word in s]

        for char in chars:
            if char == "(" or char == "[":
                stk.append(char)
            elif not stk:
                is_vps = False
                break
            elif char == ")":
                if stk.pop() == "(":
                    continue
                else:
                    is_vps = False
                    break
            elif char == "]":
                if stk.pop() == "[":
                    continue
                else:
                    is_vps = False
                    break

        if len(stk) > 0:
            is_vps = False

        print("yes" if is_vps else "no")
