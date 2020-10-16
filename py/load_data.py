def load_day_1():
    filename = "data/day1"
    with open(filename, "r") as file:
        number_list = file.readlines()
    return [int(number) for number in number_list]


def load_day_2():
    filename = "data/day2"
    with open(filename, "r") as file:
        number_list = file.read()
    return [int(number) for number in number_list.split(",")]

def load_day_3():
    filename = "data/day3"
    with open(filename, "r") as file:
        fuses = file.read()
    return [ [direction.strip() for direction in fuse.split(",")] for fuse in fuses.split('\n')]


def load_day_4():
    filename = "data/day4"
    with open(filename, "r") as file:
        puzzle_input = file.read()
    return puzzle_input.strip()


def load_day_5():
    filename = "data/day5"
    with open(filename, "r") as file:
        number_list = file.read()
    return [int(number) for number in number_list.split(",")]


def load_day_6():
    filename = "data/day6"
    with open(filename, "r") as file:
        orbits = file.read()
    return [orbit.strip() for orbit in orbits.split('\n')]


def load_day_7():
    filename = "data/day7"
    with open(filename, "r") as file:
        number_list = file.read()
    return [int(number) for number in number_list.split(",")]