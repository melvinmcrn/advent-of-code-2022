file = open("../data/q9", "r")

head_position = [0, 0]
tail_position = [0, 0]
visited_position = set()

visited_position.add("0,0")


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

        # * Calculate tail

        # * case do nothing
        if (
            abs(head_position[0] - tail_position[0]) <= 1
            and abs(head_position[1] - tail_position[1]) <= 1
        ):
            continue
        elif head_position[0] == tail_position[0]:
            # * same X (same column)
            if head_position[1] > tail_position[1]:
                tail_position[1] += 1
            else:
                tail_position[1] -= 1
        elif head_position[1] == tail_position[1]:
            # * same Y (same row)
            if head_position[0] > tail_position[0]:
                tail_position[0] += 1
            else:
                tail_position[0] -= 1

        else:
            # * diagonally
            if abs(head_position[0] - tail_position[0]) > 1:
                tail_position[0] += (head_position[0] - tail_position[0]) / abs(
                    head_position[0] - tail_position[0]
                )
                tail_position[1] += (head_position[1] - tail_position[1]) / abs(
                    head_position[1] - tail_position[1]
                )
            elif abs(head_position[1] - tail_position[1]) > 1:
                tail_position[1] += (head_position[1] - tail_position[1]) / abs(
                    head_position[1] - tail_position[1]
                )
                tail_position[0] += (head_position[0] - tail_position[0]) / abs(
                    head_position[0] - tail_position[0]
                )

        visited_position.add(f"{int(tail_position[0])},{int(tail_position[1])}")


print("visited_position", len(visited_position))


file.close()
