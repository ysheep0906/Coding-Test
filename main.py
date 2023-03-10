T = int(input())
data = []
count = 0

for i in range(T):
    data.append(input())
    
for i in range(T):
    count = 0
    for j in range(len(data[i])):
        if count == 0 and data[i][j] == ')':
            count -= 100
        elif data[i][j] == '(':
            count += 1
        elif count > 0 and data[i][j] == ')':
            count -= 1
    if(count == 0):
        print('YES')
    else:
        print('NO')

