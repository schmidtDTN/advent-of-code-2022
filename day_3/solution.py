import math, os

def get_priority(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38


def part_1(input):
    dupe_priority = 0
    for line in input.splitlines():
        comp_1_set = set()
        comp_2_set = set()
        line_length = len(line)
        halfway = math.floor(line_length / 2)
        first_compartment = line[:halfway]
        second_compartment = line[halfway:]
        for item in first_compartment:
            comp_1_set.add(item)
        for item2 in second_compartment:
            comp_2_set.add(item2)
        dupe = comp_1_set.intersection(comp_2_set).pop()
        dupe_priority += get_priority(dupe)

    return dupe_priority

def part_2(input):
    elf_count = 0
    group_sacks = []
    badge_priorities = 0
    for line in input.splitlines():
        if elf_count < 3:
            curr_set = set()
            for item in line:
                curr_set.add(item)
            group_sacks.append(curr_set)
            elf_count += 1
        if elf_count == 3:
            match = group_sacks[0].intersection(group_sacks[1].intersection(group_sacks[2])).pop()
            elf_count = 0
            badge_priorities += get_priority(match)
            group_sacks.clear()
    
    return badge_priorities

def main():
    dir = os.path.dirname(__file__)
    # filename = os.path.join(dir, 'sample_input.txt')
    filename = os.path.join(dir, 'input.txt')
    file = open(filename)
    input = file.read()
    part_1_solution = part_1(input)
    part_2_solution = part_2(input)

    print("Part 1: " +  str(part_1_solution))
    print("Part 2: " +  str(part_2_solution))

main()