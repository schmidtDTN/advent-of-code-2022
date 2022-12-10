import math, os
from functools import reduce

clock = 1
register_x = 1
register_x_values = {}
crt_lines = []
current_crt_line = ''

def clock_step(number_of_steps):
    global clock
    for _ in range(number_of_steps):
        if (clock - 20) % 40 == 0:
            register_x_values.update({clock: register_x})
        clock += 1
        
def part_2_clock_step(number_of_steps):
    global clock
    global current_crt_line
    for _ in range(number_of_steps):
        currently_drawn_pixel = (clock - 1) % 40
        if currently_drawn_pixel in range(register_x - 1, register_x + 2):
            current_crt_line += '#'
        else:
            current_crt_line += '.'
        if clock % 40 == 0:
            crt_lines.append(current_crt_line)
            current_crt_line = ''
        clock += 1

def part_1(input):
    global register_x
    for line in input.splitlines():
        command = line.split(' ')[0]
        if command == 'noop':
            clock_step(1)
        elif command == 'addx':
            value = line.split(' ')[1]
            clock_step(2)
            register_x += int(value)
    signal_strength = 0
    for cycle, value in register_x_values.items():
        signal_strength += (cycle * value)
    return signal_strength 

def part_2(input):
    global clock
    global register_x_values
    global register_x
    clock = 1
    register_x = 1
    register_x_values.clear()
    for line in input.splitlines():
        command = line.split(' ')[0]
        if command == 'noop':
            part_2_clock_step(1)
        elif command == 'addx':
            value = line.split(' ')[1]
            part_2_clock_step(2)
            register_x += int(value)
    for line in crt_lines:
        print(line)
    return

def main():
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'sample_input.txt')
    filename = os.path.join(dir, 'sample_input_2.txt')
    filename = os.path.join(dir, 'input.txt')
    file = open(filename)
    input = file.read()
    part_1_solution = part_1(input)
    part_2(input)

    print("Part 1: " +  str(part_1_solution))
main()