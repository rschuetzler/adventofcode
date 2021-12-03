


with open("../data/day1") as file:
    prev = None
    higher = 0
    lower = 0
    data = file.readlines()
    for idx, row in enumerate(data):
        newval = int(row.strip()) if len(row.strip()) > 0 else None
        if prev == None or newval == None:
            pass
        elif newval > prev:
            higher += 1
        elif newval < prev:
            lower += 1
        prev = newval

        # print(f"{idx=}")

    print(f"{higher=}")
    print(f"{lower=}")