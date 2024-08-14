"""
https://www.acmicpc.net/problem/9012
 - stack 사용, 괄호의 쌍이 존재 여부 확인
"""

for _ in range(int(input())):
    stk: list = []
    is_vps: bool = True

    for ch in input():
        if ch == "(":
            stk.append(ch)
        else:
            if stk:
                stk.pop()
            else:
                is_vps = False
                break

    if stk:
        is_vps = False

    print("YES" if is_vps else "NO")
