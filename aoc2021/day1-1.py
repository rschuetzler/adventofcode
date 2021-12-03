


with open("../data/day1") as file:

    data = file.readlines()
    cleandata = [int(item.strip()) for item in data]

    higher = 0
    lower = 0

    for idx, row in enumerate(cleandata):
        try:
            thisdepth = sum(cleandata[idx:idx+3])
            nextdepth = sum(cleandata[idx+1:idx+4])
            print(f"{thisdepth=} and {nextdepth=}")
            if nextdepth > thisdepth:
                higher += 1
            elif thisdepth > nextdepth:
                lower += 1

        except LookupError:
            print(f"got to row {idx}")
            pass

    # for idx, row in enumerate(data):
    #     newval = int(row.strip()) if len(row.strip()) > 0 else None
    #     if prev == None or newval == None:
    #         pass
    #     elif newval > prev:
    #         higher += 1
    #     elif newval < prev:
    #         lower += 1
    #     prev = newval

        # print(f"{idx=}")

    print(f"{higher=}")
    print(f"{lower=}")