file = open("../data/q5", "r")


# * READ STACK DATA

stack_data = []
temp_stack_data = []

while True:
    line = file.readline().strip()

    if not line.strip():
        break

    if "[" not in line and "1" in line:
        # * the last line with the number of stack
        # * extract the number of stack

        found_number = False
        for c in line:
            if c != " " and not found_number:
                found_number = True
                stack_data.append([])
            else:
                found_number = False
    else:
        temp_stack_data.append(line)

# * iterate each stack and put the data into list
for stack in temp_stack_data:
    stack_no = 0
    for i in range(len(stack)):
        if (i - 1) % 4 == 0:
            # * position of the data
            if stack[i] != " ":
                stack_data[stack_no].insert(0, stack[i])
            stack_no += 1

for instruction in file.readlines():
    instruction = (
        instruction.replace("move", "").replace("from", "").replace("to", "").strip()
    )

    amount, stack_from, stack_to = [int(e.strip()) for e in instruction.split()]

    for i in range(amount):
        stack_data[stack_to - 1].append(stack_data[stack_from - 1].pop())

result = ""
for stack in stack_data:
    result += stack[-1]

print("result:", result)

file.close()
