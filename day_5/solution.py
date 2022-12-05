import math, os
    
def parse_line(line):
    elf_1_range, elf_2_range = line.split(',')[0], line.split(',')[1]
    elf_1_start, elf_1_stop = int(elf_1_range.split('-')[0]), int(elf_1_range.split('-')[1])
    elf_2_start, elf_2_stop = int(elf_2_range.split('-')[0]), int(elf_2_range.split('-')[1])
    return (elf_1_start, elf_1_stop, elf_2_start, elf_2_stop)

def part_1(input):
    input_lines = input.splitlines()
    line_length = len(input_lines[0])
    number_of_columns = math.ceil(line_length / 4.0)
    stacks = [[] for _ in range(number_of_columns)]
    is_starting_map = True
    for line in input_lines:
        if line.strip() and line[1] == '1':
            is_starting_map = False
            for stack in stacks:
                stack.reverse()
        if is_starting_map:
            curr_column = 0
            while (1 + (curr_column * 4)) < line_length:
                for value in line[1 + (curr_column * 4)]:
                    if value != ' ':
                        stacks[curr_column].append(value)
                    curr_column += 1
        else:
            if line.strip() and line[0] == 'm':
                amount_to_move = int(line.split(' ')[1])
                source_stack = int(line.split(' ')[3]) - 1
                dest_stack = int(line.split(' ')[5]) - 1
                for i in range(amount_to_move):
                    stacks[dest_stack].append(stacks[source_stack].pop())
    
    message_string = ''
    for stack in stacks:
        message_string += stack.pop()
    return message_string


def part_2(input):
    input_lines = input.splitlines()
    line_length = len(input_lines[0])
    number_of_columns = math.ceil(line_length / 4.0)
    stacks = [[] for _ in range(number_of_columns)]
    is_starting_map = True
    for line in input_lines:
        if line.strip() and line[1] == '1':
            is_starting_map = False
            for stack in stacks:
                stack.reverse()
        if is_starting_map:
            curr_column = 0
            while (1 + (curr_column * 4)) < line_length:
                for value in line[1 + (curr_column * 4)]:
                    if value != ' ':
                        stacks[curr_column].append(value)
                    curr_column += 1
        else:
            if line.strip() and line[0] == 'm':
                amount_to_move = int(line.split(' ')[1])
                source_stack = int(line.split(' ')[3]) - 1
                dest_stack = int(line.split(' ')[5]) - 1
                stacks[dest_stack].extend(stacks[source_stack][-amount_to_move:])
                stacks[source_stack] = stacks[source_stack][:-amount_to_move]

    message_string = ''
    for stack in stacks:
        message_string += stack.pop()
    return message_string

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