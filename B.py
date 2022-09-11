n = int(input())

otbor = dict()
for i in range(n):
    s, m = input().split(',')
    otbor[s] = {}
    otbor[s]['m'] = int(m)
    otbor[s]['participants'] = []

k = int(input())

for j in range(k):
    c, q, r, p = input().split(',')
    if q in otbor:
        otbor[q]['participants'].append((c, int(r), int(p)))

ans = []
for sorev, data in otbor.items():
    participants = data['participants']
    m = data['m']
    if len(participants) > m:
        participants = sorted(participants, key=lambda x: (-x[1], x[2]))
    for i in range(m):
        if i < len(participants):
            ans.append(participants[i][0])
        else:
            break

for i in sorted(ans):
    print(i)


