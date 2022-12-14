file = open("../data/q10", "r")

cycle = 0
total = 0
x = 1
pause = False

while True:

    cycle += 1

    if cycle > 220:
        break

    if cycle % 40 == 20:
        total += cycle * x

    if pause:
        x += amount
        pause = False
        continue

    line = file.readline()

    if not line.strip():
        break

    data = line.strip().split()

    if data[0] == "noop":
        continue
    elif data[0] == "addx":
        amount = int(data[1])
        pause = True


print("total", total)


file.close()
