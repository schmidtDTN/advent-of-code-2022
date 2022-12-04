import os
    
def parse_line(line):
    elf_1_range, elf_2_range = line.split(',')[0], line.split(',')[1]
    elf_1_start, elf_1_stop = int(elf_1_range.split('-')[0]), int(elf_1_range.split('-')[1])
    elf_2_start, elf_2_stop = int(elf_2_range.split('-')[0]), int(elf_2_range.split('-')[1])
    return (elf_1_start, elf_1_stop, elf_2_start, elf_2_stop)

def part_1(input):
    overlaps = 0
    for line in input.splitlines():
        (elf_1_start, elf_1_stop, elf_2_start, elf_2_stop) = parse_line(line)
        elf_1_range = range(elf_1_start, elf_1_stop + 1)
        elf_2_range = range(elf_2_start, elf_2_stop + 1)
        elf_1_range_set = set(elf_1_range)
        elf_2_range_set = set(elf_2_range)
        if elf_1_range_set.intersection(elf_2_range_set) == elf_1_range_set or elf_1_range_set.intersection(elf_2_range_set) == elf_2_range_set:
            overlaps += 1
    return overlaps
    


def part_2(input):
    overlaps = 0
    for line in input.splitlines():
        (elf_1_start, elf_1_stop, elf_2_start, elf_2_stop) = parse_line(line)
        elf_1_range = range(elf_1_start, elf_1_stop + 1)
        elf_2_range = range(elf_2_start, elf_2_stop + 1)
        elf_1_range_set = set(elf_1_range)
        elf_2_range_set = set(elf_2_range)
        intersection = elf_1_range_set.intersection(elf_2_range_set)
        if len(intersection) != 0:
            overlaps += 1
        
    return overlaps


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