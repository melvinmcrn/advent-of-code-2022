file = open("../data/q8", "r")

data = []
max_score = 0

for line in file.readlines():

    data.append([int(e) for e in line.strip()])

for i in range(len(data)):
    for j in range(len(data[i])):

        left = 0
        right = 0
        top = 0
        bottom = 0

        current_height = data[i][j]

        # * left
        for m in range(j - 1, -1, -1):
            left += 1
            if data[i][m] >= current_height:
                break

        # * top
        for m in range(i - 1, -1, -1):
            top += 1
            if data[m][j] >= current_height:
                break

        # * right
        for m in range(j + 1, len(data[i])):
            right += 1
            if data[i][m] >= current_height:
                break

        # * bottom
        for m in range(i + 1, len(data)):
            bottom += 1
            if data[m][j] >= current_height:
                break

        score = left * right * top * bottom

        if score > max_score:
            max_score = score


print("max_score", max_score)


file.close()
