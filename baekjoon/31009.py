"""
https://www.acmicpc.net/problem/31009
"""

N = int(input())

charge_array = []
jinju_charge: int = 0

for _ in range(N):
    destination, charge = input().split()
    charge = int(charge)

    charge_array.append(charge)

    if destination == "jinju":
        print(charge)
        jinju_charge = charge

print(len(list(filter(lambda x: x > jinju_charge, charge_array))))
