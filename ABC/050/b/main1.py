n = int(input())
T = list(map(int, input().split()))
m = int(input())

for i in range(m):
    p, x = map(int, input().split())
    ans = sum(T)-T[p-1]+x
    print(ans)
