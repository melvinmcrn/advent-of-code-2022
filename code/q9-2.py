file = open("../data/q9", "r")

head_position = [0, 0]
middle_position = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
tail_position = [0, 0]
visited_position = set()

visited_position.add("0,0")


def calculate_next_step(lead, follow):
    if abs(lead[0] - follow[0]) <= 1 and abs(lead[1] - follow[1]) <= 1:
        return follow
    elif lead[0] == follow[0]:
        # * same X (same column)
        if lead[1] > follow[1]:
            follow[1] += 1
        else:
            follow[1] -= 1
    elif lead[1] == follow[1]:
        # * same Y (same row)
        if lead[0] > follow[0]:
            follow[0] += 1
        else:
            follow[0] -= 1

    else:
        # * diagonally
        if abs(lead[0] - follow[0]) > 1:
            follow[0] += (lead[0] - follow[0]) / abs(lead[0] - follow[0])
            follow[1] += (lead[1] - follow[1]) / abs(lead[1] - follow[1])
        elif abs(lead[1] - follow[1]) > 1:
            follow[1] += (lead[1] - follow[1]) / abs(lead[1] - follow[1])
            follow[0] += (lead[0] - follow[0]) / abs(lead[0] - follow[0])
    return follow


for line in file.readlines():

    line = line.strip().split()
    direction, amount = line[0], int(line[1])

    for i in range(amount):
        if direction == "L":
            head_position = [head_position[0] - 1, head_position[1]]
        elif direction == "U":
            head_position = [head_position[0], head_position[1] + 1]
        elif direction == "R":
            head_position = [head_position[0] + 1, head_position[1]]
        elif direction == "D":
            head_position = [head_position[0], head_position[1] - 1]

        # * Calculate middle
        for i in range(len(middle_position)):
            if i == 0:
                middle_position[i] = calculate_next_step(
                    head_position, middle_position[i]
                )
            else:
                middle_position[i] = calculate_next_step(
                    middle_position[i - 1], middle_position[i]
                )

        # * Calculate tail
        tail_position = calculate_next_step(middle_position[-1], tail_position)

        visited_position.add(f"{int(tail_position[0])},{int(tail_position[1])}")


print("visited_position", len(visited_position))


file.close()
