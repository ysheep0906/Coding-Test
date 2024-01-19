def fibonacci(n,count):
    if(n==0):
      count[0] += 1 
      return 0
    elif (n==1):
      count[1] += 1
      return 1
    else:
       return fibonacci(n-1,count) + fibonacci(n-2,count)

T = int(input())
T_list = []

for i in range(T):
  T_list.append(int(input()))

for i in range(T):
  count = [0,0]
  fibonacci(T_list[i],count)
  print(str(count[0]) + ' ' + str(count[1]))
# 파이썬은 list, dict, set와 같이 mutable object가 argument로 넘어가면
# object reference가 넘어가서 담고 있는 값을 바꿀 수 있다
# immutable object인 int, float, str, tuples 등은 단일 값이거나 static 속성
# 하지만 이렇게 재귀형식으로 푼다면 오류!!(시간제한)
    