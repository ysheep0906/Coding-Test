"""
N 
= x + (x+1) + (x+2) + ... (x+L-1)
= Lx + (1+2+...+L-1)
= Lx + (L-1)L / 2 -> t
= Lx + t
--> x = (N-t)/L
x는 정수이기 때문에 (N-t)가 L로 나누어 떨어져야 하며 0이상이어야 한다.
"""
N, L = input().split(' ')
N = int(N)
L = int(L)
x = -1
iter = -1

for i in range(L,101):
  t = int(((i-1)*i)/2)
  
  if( ((N-t)%i==0) and ((N-t)/i>=0) ):
    x = int((N-t)/i)
    iter = i
    break


if(x == -1):
  print(-1)
else:
  for i in range(iter):
    print(x + i)



    