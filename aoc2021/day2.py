
with open("../data/day2") as file:
    directions = [item.strip().split(' ') for item in file.readlines()]
    print(directions)

    x, depth, aim = 0, 0, 0

    for step in directions:
        movement = step[0]
        distance = int(step[1])

        match movement:
            case 'forward':
                x += distance
                depth += distance * aim
            case 'up':
                aim -= distance
            case 'down':
                aim += distance
    print(f"{x=}, {depth=}")
    print(f"{x*depth}")
