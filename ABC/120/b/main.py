a, b, k = map(int, input().split())
ls = []

for i in range(1, a*b+1):
    if a % i == 0 and b % i == 0:
        ls.append(-i)

ls.sort()
print(-ls[k-1])
