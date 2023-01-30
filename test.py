a, b = map(int, input().split())

people = [(i + 1) for i in range(a)]
index = people * b
remove_list = []
count = 0

for i in range(a):
    for j in range(a):
        if people[j] not in remove_list:
            count += 1
            
        if count == b:
            remove_list.append(people[j])
            count = 0

print(index)