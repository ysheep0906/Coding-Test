N = int(input())
A = list(map(int, input().split(' ')))
A.sort()
M = int(input())
B = list(map(int, input().split(' ')))



def binsearch(x,List, n):
  low, high = 0, n-1
  isExist = False

  while(low <= high):
    mid = (low + high)//2
    if(x == List[mid]):
      isExist = True
      print(1)
      break
    elif(x < List[mid]):
      high = mid -1
    else:
      low = mid + 1
  
  if not isExist:
    print(0)

for i in B:
  binsearch(i,A,N)