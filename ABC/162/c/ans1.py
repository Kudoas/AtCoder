from math import gcd

k = int(input())

cnt = 0
for i in range(1, k+1):
    for j in range(1, k+1):
        for k in range(1, k+1):
            cnt += gcd(gcd(i, j), k)

print(cnt)
