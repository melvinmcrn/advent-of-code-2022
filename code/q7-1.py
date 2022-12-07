import json

file = open("../data/q7", "r")

current_dir = []
dir_str = ""
full_total = 0

full_data = dict()


def get_dir_size(dir):
    if len(full_data[dir]["sub_dir"]) > 0:

        for sub_dir in full_data[dir]["sub_dir"]:
            full_data[dir]["total"] += get_dir_size(f"{dir}{sub_dir}/")

        full_data[dir]["sub_dir"] = []

    return full_data[dir]["total"]


for line in file.readlines():

    data = line.strip().split()

    if data[0] == "$":
        if data[1] == "cd":
            if data[2] == "/":
                current_dir = ["/"]
            elif data[2] == "..":
                current_dir.pop()
            else:
                current_dir.append(f"{data[2]}/")

            dir_str = "".join(current_dir)

        elif data[1] == "ls":
            continue

    elif data[0] == "dir":
        if dir_str not in full_data:
            full_data[dir_str] = {"total": 0, "sub_dir": []}

        if (
            f"{dir_str}{data[1]}/" not in full_data
            or len(full_data[f"{dir_str}{full_data[1]}/"]["sub_dir"]) > 0
        ):
            full_data[dir_str]["sub_dir"].append(data[1])
        else:
            full_data[dir_str]["total"] += full_data[f"{dir_str}{data[1]}/"]["total"]

    else:
        if dir_str not in full_data:
            full_data[dir_str] = {"total": 0, "sub_dir": []}

        full_data[dir_str]["total"] += int(data[0])


for key in full_data.keys():
    if len(full_data[key]["sub_dir"]) > 0:
        for sub_dir in full_data[key]["sub_dir"]:
            full_data[key]["total"] += get_dir_size(f"{key}{sub_dir}/")
        full_data[key]["sub_dir"] = []

    if full_data[key]["total"] <= 100000:
        full_total += full_data[key]["total"]


print("full_total", full_total)

file.close()
