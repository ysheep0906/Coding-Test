# 다이나믹 프로그래밍
T = int(input())

for _ in range(T):
  num = int(input())
  dp = [[0 for col in range(4)] for row in range(11)]
  dp[1][1] = 1 # Memoization
  dp[1][2] = 0
  dp[1][3] = 0
  dp[2][1] = 1
  dp[2][2] = 1
  dp[2][3] = 0
  dp[3][1] = 2
  dp[3][2] = 1
  dp[3][3] = 1
  for i in range(4,num+1):
    dp[i][1] = dp[i-1][1] + dp[i-1][2] + dp[i-1][3]
    dp[i][2] = dp[i-2][1] + dp[i-2][2] + dp[i-2][3]
    dp[i][3] = dp[i-3][1] + dp[i-3][2] + dp[i-3][3]
  print(dp[num][1] + dp[num][2] + dp[num][3])
