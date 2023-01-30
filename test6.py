import sys

n, m = map(int, input().split())

listen = {i : sys.stdin.readline().strip() for i in range(n)}
see = {i : sys.stdin.readline().strip() for i in range(m)}
listensee = []

k = list(see.values())

for i in range(len(listen)):
    if listen[i] in k:
        listensee.append(listen[i])

listensee.sort()

print(len(listensee))
print(*listensee, sep='\n')