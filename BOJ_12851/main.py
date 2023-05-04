from collections import deque

def BFS(N,K):
  queue = deque([N])
  time = 0
  visited[N] = 0
  count = 0
  result = 1000000

  while queue:
    size = len(queue)
    time += 1

    for _ in range(size):
      n = queue.popleft()
      if(n == K):
        if(visited[K] > result):
          continue
        elif(visited[K] < result):
          result = visited[K]
          count = 1
        else:
          count += 1
        continue

      if(n-1 >= 0 and (visited[n-1] == None or visited[n-1] > visited[n])):
        queue.append(n-1)
        visited[n-1] = time
      if(n+1 <= 100000 and (visited[n+1] == None or visited[n+1] > visited[n])):
        queue.append(n+1)
        visited[n+1] = time
      if(n*2 <= 100000 and (visited[n*2] == None or visited[n*2] > visited[n])):
        queue.append(n*2)
        visited[n*2] = time
        
  print(result)
  print(count)

N , K = map(int,input().split())
visited = [None] * 100001

BFS(N,K)

