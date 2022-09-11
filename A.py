
a = input()
b = input()

alfabet = {}

for i in a:
    if alfabet.get(i):
        alfabet[i] += 1
    else:
        alfabet[i] = 1

ans = []

for i in range(len(a)):
    if a[i] == b[i]:
        alfabet[b[i]] -= 1
        ans += 'P'
    else:
        ans += 'I'

for i in range(len(a)):
    if a[i] != b[i] and ans[i] == 'I' and b[i] in alfabet and alfabet[b[i]] > 0:
        alfabet[b[i]] -= 1
        ans[i] = 'S'

print(*ans, sep='')
