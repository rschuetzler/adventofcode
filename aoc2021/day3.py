
def calculate_o2(data):
    for i in range(len(data[0])):
        if len(data) == 1:
            print(data)
            break
        ones = 0
        zeros = 0
        for num in data:
            if num[i] == "1":
                ones += 1
            else:
                zeros += 1
        if ones >= zeros:
            data = [num for num in data if num[i] == "1"]
        else:
            data = [num for num in data if num[i] == "0"]
    return int(data[0], 2)

def calculate_co2(data):
    for i in range(len(data[0])):
        if len(data) == 1:
            print(data)
            break
        ones = 0
        zeros = 0
        for num in data:
            if num[i] == "1":
                ones += 1
            else:
                zeros += 1
        if ones < zeros:
            data = [num for num in data if num[i] == "1"]
        else:
            data = [num for num in data if num[i] == "0"]
    return int(data[0], 2)


with open("../data/day3") as file:
    data = [item.strip() for item in file.readlines()]

    gamma = ""
    epsilon = ""
    for idx, char in enumerate(data[0]):
        ones = 0
        zeros = 0
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

    O2 = calculate_o2(data)
    CO2 = calculate_co2(data)
    print(f"O2 * CO2 = {O2*CO2}")

