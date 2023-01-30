a, b = map(int, input().split())

people = [(i + 1) for i in range(a)]
remove_list = []
count = 0
index = 0

for i in range(a):
    while True:
        if people[index] not in remove_list:
            count += 1
            index += 1
        else:
            index += 1

        if index == a:
            index = 0

        if count == b:
            remove_list.append(people[index - 1])
            count = 0
            break


print('<', end='')
for i in remove_list[ : -1]:
    print(f'{i}, ', end='')

print(f'{remove_list[-1]}', end='')
print('>')