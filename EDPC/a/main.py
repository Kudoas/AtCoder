n = int(input())
H = list(map(int, input().split()))

dp = [0]*(10**5)
dp[0] = 0
dp[1] = abs(H[0]-H[1])

for i in range(2, n):
    dp[i] = min(dp[i-1]+abs(H[i]-H[i-1]), dp[i-2]+abs(H[i]-H[i-2]))

print(dp[n-1])
