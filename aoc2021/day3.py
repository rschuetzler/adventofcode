
with open("../data/day3") as file:
    data = [item.strip() for item in file.readlines()]

    gamma = ""
    epsilon = ""
    for idx, char in enumerate(data[0]):
        ones = 0
        zeros = 0
        print(idx)
        for num in data:
            if num[idx] == "1":
                ones += 1
            else:
                zeros += 1
        print(f"{ones=}, {zeros=}")
        if ones > zeros:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    print(f"{gamma=}")
    print(f"{epsilon=}")

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    print(gamma * epsilon)