from math import lcm

data = [
    {
        "items": [71, 86],
        "operation": lambda x: x * 13,
        "test": lambda x: 6 if x % 19 == 0 else 7,
    },
    {
        "items": [66, 50, 90, 53, 88, 85],
        "operation": lambda x: x + 3,
        "test": lambda x: 5 if x % 2 == 0 else 4,
    },
    {
        "items": [97, 54, 89, 62, 84, 80, 63],
        "operation": lambda x: x + 6,
        "test": lambda x: 4 if x % 13 == 0 else 1,
    },
    {
        "items": [82, 97, 56, 92],
        "operation": lambda x: x + 2,
        "test": lambda x: 6 if x % 5 == 0 else 0,
    },
    {
        "items": [50, 99, 67, 61, 86],
        "operation": lambda x: x * x,
        "test": lambda x: 5 if x % 7 == 0 else 3,
    },
    {
        "items": [61, 66, 72, 55, 64, 53, 72, 63],
        "operation": lambda x: x + 4,
        "test": lambda x: 3 if x % 11 == 0 else 0,
    },
    {
        "items": [59, 79, 63],
        "operation": lambda x: x * 7,
        "test": lambda x: 2 if x % 17 == 0 else 7,
    },
    {
        "items": [55],
        "operation": lambda x: x + 7,
        "test": lambda x: 2 if x % 3 == 0 else 1,
    },
]


count_list = [0 for i in range(8)]
test_lcm = lcm(19, 2, 13, 5, 7, 11, 17, 3)

for z in range(10_000):
    for i in range(8):
        current_items = data[i]["items"]
        data[i]["items"] = []
        for item in current_items:
            count_list[i] += 1
            new_item = data[i]["operation"](item) % test_lcm

            data[data[i]["test"](new_item)]["items"].append(new_item)


selected_list = sorted(count_list, reverse=True)[:2]

print(selected_list[0] * selected_list[1])
