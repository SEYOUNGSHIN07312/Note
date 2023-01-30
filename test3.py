num = int(input())

len_list = [list(map(int, input().split())) for _ in range(6)]
vertical = []
horizontal = []


for i in range(6):
    if len_list[i][0] == 3 or len_list[i][0] == 4:
        vertical.append([len_list[i], i])

    else:
        horizontal.append([len_list[i], i])

height = max(r[0][1] for r in vertical)
width = max(r[0][1] for r in horizontal)

total_area = height * width

for i in range(3):
    if vertical[i][0][1] == height:
        a = vertical[i][1]

    if horizontal[i][0][1] == width:
        b = horizontal[i][1]

if a > b:
    len_else = []

    for i in range(1, 7):
        if len_list[a + i][1] != height:
            len_else.append(len_list[a + i])

        


else:
    pass