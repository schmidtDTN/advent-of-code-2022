import math, os

def part_1(input):
    characters_seen = 0
    potential_marker = []
    for character in input:
        potential_marker.append(character)
        if len(potential_marker) > 4:
            potential_marker.pop(0)
        characters_seen += 1
        if len(set(potential_marker)) == 4:
            return characters_seen


def part_2(input):
    characters_seen = 0
    potential_marker = []
    for character in input:
        potential_marker.append(character)
        if len(potential_marker) > 14:
            potential_marker.pop(0)
        characters_seen += 1
        if len(set(potential_marker)) == 14:
            return characters_seen

def main():
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'sample_input.txt')
    # filename = os.path.join(dir, 'input.txt')
    file = open(filename)
    input = file.read()
    part_1_solution = part_1(input)
    part_2_solution = part_2(input)

    print("Part 1: " +  str(part_1_solution))
    print("Part 2: " +  str(part_2_solution))
main()