T = int(input())

for i in range(T):
  N = int(input())
  zero,one = 1,0
  for j in range(N):
    zero, one = one, zero + one # 피보나치 수열을 한 칸씩 이동
  print(zero, one)

# N에 따라 0이 출력되는 횟수인 zeros와 1이 출력되는 횟수인 ones 역시 
# 피보나치 수열의 패턴을 갖는다는 것

# 0이 출력되는 횟수의 규칙은 1,0,1,1,2,3,... 
# 1이 출력되는 횟수의 규칙은 0,1,1,2,3,...
# 0이 출력되는 횟수의 2번째 이후가 1이 출력되는 횟수의 규칙과 같음
