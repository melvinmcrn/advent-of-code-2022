file = open("../data/q8", "r")

data = []
count_visible = 0

for line in file.readlines():

    data.append([int(e) for e in line.strip()])

for i in range(len(data)):
    for j in range(len(data[i])):
        # * edge
        if i == 0 or j == 0 or i == len(data) - 1 or j == len(data[i]) - 1:
            count_visible += 1
            continue

        current_height = data[i][j]

        check_visible = False

        # * left
        for m in range(j - 1, -1, -1):
            if data[i][m] >= current_height:
                break
        else:
            check_visible = True

        # * top
        for m in range(i - 1, -1, -1):
            if data[m][j] >= current_height:
                break
        else:
            check_visible = True

        # * right
        for m in range(j + 1, len(data[i])):
            if data[i][m] >= current_height:
                break
        else:
            check_visible = True

        # * bottom
        for m in range(i + 1, len(data)):
            if data[m][j] >= current_height:
                break
        else:
            check_visible = True

        if check_visible:
            count_visible += 1


print("count_visible", count_visible)


file.close()
