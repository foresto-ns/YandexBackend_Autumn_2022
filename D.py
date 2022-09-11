from collections import deque

n,m = list(map(int, input().split()))

field = []

S_place = ()

for i in range(n):
    data = input()
    pos = data.find('S')
    if pos > 0:
        S_place = (i,pos)
    field.append(list(data))

queue = deque()
queue.append(S_place)

while len(queue) != 0:
    el = queue.popleft()

    if field[el[0] + 1][el[1]] == '.':
        field[el[0] + 1][el[1]] = 'U'
        queue.append((el[0] + 1, el[1]))

    if field[el[0] - 1][el[1]] == '.':
        field[el[0] - 1][el[1]] = 'D'
        queue.append((el[0] - 1, el[1]))

    if field[el[0]][el[1] + 1] == '.':
        field[el[0]][el[1] + 1] = 'L'
        queue.append((el[0], el[1] + 1))

    if field[el[0]][el[1] - 1] == '.':
        field[el[0]][el[1] - 1] = 'R'
        queue.append((el[0], el[1] - 1))

res = ''
for line in field:
    res += ''.join(line)
    res += '\n'

print(res)