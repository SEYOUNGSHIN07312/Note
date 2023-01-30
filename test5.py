import sys

n, m = map(int, input().split())

listen = [sys.stdin.readline().strip() for _ in range(n)]
see = [sys.stdin.readline().strip() for _ in range(m)]
listensee = []

for i in range(len(listen)):
    if listen[i] in see:
        listensee.append(listen[i])

listensee.sort()

print(len(listensee))
print(*listensee, sep='\n')