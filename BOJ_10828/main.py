import sys

class Stack:
  arr = []

  def push(self, num):
    self.arr.append(num)

  def pop(self):
    if(len(self.arr) == 0):
      print(-1)
    else:
      print(self.arr.pop())

  def size(self):
    print(len(self.arr))

  def empty(self):
    if(len(self.arr) == 0):
      print(1)
    else:
      print(0)
    
  def top(self):
    if(len(self.arr) == 0):
      print(-1)
    else:
      print(self.arr[-1])

def run():
  stack = Stack()
  N = int(input())

  for i in range(N):
    input_N = sys.stdin.readline().rstrip().split()

    if(input_N[0] == 'push'):
      stack.push(input_N[1])
      
    elif(input_N[0] == 'pop'):
      stack.pop()
    elif(input_N[0] == 'size'):
      stack.size()
    elif(input_N[0] == 'empty'):
      stack.empty()
    elif(input_N[0] == 'top'):
      stack.top()
    else:
      return '잘못 입력하였습니다!'

run()

