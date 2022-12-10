import math, os, numpy

# def part_1(input):
    # current_head_pos = (0,0) # x, y
    # current_tail_pos = (0,0) # x, y
    # head_path = [current_head_pos]
    # tail_path = [current_tail_pos]
    # for row in input.splitlines():
    #     direction = row.split(' ')[0]
    #     magnitude = int(row.split(' ')[1])
    #     if direction == 'R':
    #         x_change = 1
    #         y_change = 0
    #     elif direction == 'L':
    #         x_change = -1
    #         y_change = 0
    #     elif direction == 'U':
    #         x_change = 0
    #         y_change = 1
    #     elif direction == 'D':
    #         x_change = 0
    #         y_change = -1
    #     for _ in range(magnitude):
    #         head_x = current_head_pos[0] + x_change
    #         head_y = current_head_pos[1] + y_change
    #         tail_x = current_tail_pos[0]
    #         tail_y = current_tail_pos[1]
    #         new_head_pos = (head_x, head_y)
    #         head_path.append(new_head_pos)
    #         current_head_pos = new_head_pos
    #         # head is to the right by two
    #         if head_x - tail_x == 2:
    #             tail_x += 1
    #             if head_y - tail_y == 1:
    #                 tail_y += 1
    #             if head_y - tail_y == -1:
    #                 tail_y -= 1
    #         if head_x - tail_x == -2:
    #             tail_x -= 1
    #             if head_y - tail_y == 1:
    #                 tail_y += 1
    #             if head_y - tail_y == -1:
    #                 tail_y -= 1
    #         if head_y - tail_y == 2:
    #             tail_y += 1
    #             if head_x - tail_x == 1:
    #                 tail_x += 1
    #             if head_x - tail_x == -1:
    #                 tail_x -= 1
    #         if head_y - tail_y == -2:
    #             tail_y -= 1
    #             if head_x - tail_x == 1:
    #                 tail_x += 1
    #             if head_x - tail_x == -1:
    #                 tail_x -= 1
    #         new_tail_pos = (tail_x, tail_y)
    #         tail_path.append(new_tail_pos)
    #         current_tail_pos = new_tail_pos
    # distinct_tail_positions = set(tail_path)
    # return len(distinct_tail_positions)


knot_paths = {}
knot_pos = {}

def calculate_knot_path(prev_knot_id, curr_knot_id):
    # tail_x = current_tail_pos[0]
    # this_knot_x = curr_knot_pos[0]
    # this_knot_y = curr_knot_pos[1]
    prev_knot_x = knot_pos[prev_knot_id][0]
    prev_knot_y = knot_pos[prev_knot_id][1]
    this_knot_x = knot_pos[curr_knot_id][0]
    this_knot_y = knot_pos[curr_knot_id][1]
    

    # head is to the right by two
    if prev_knot_x - this_knot_x == 2:
        this_knot_x += 1
        if prev_knot_y - this_knot_y == 1:
            this_knot_y += 1
        if prev_knot_y - this_knot_y == -1:
            this_knot_y -= 1
    if prev_knot_x - this_knot_x == -2:
        this_knot_x -= 1
        if prev_knot_y - this_knot_y == 1:
            this_knot_y += 1
        if prev_knot_y - this_knot_y == -1:
            this_knot_y -= 1
    if prev_knot_y - this_knot_y == 2:
        this_knot_y += 1
        if prev_knot_x - this_knot_x == 1:
            this_knot_x += 1
        if prev_knot_x - this_knot_x == -1:
            this_knot_x -= 1
    if prev_knot_y - this_knot_y == -2:
        this_knot_y -= 1
        if prev_knot_x - this_knot_x == 1:
            this_knot_x += 1
        if prev_knot_x - this_knot_x == -1:
            this_knot_x -= 1
    return (this_knot_x, this_knot_y)

def solve(input, knot_count):
    starting_pos = (0,0)
    for i in range(knot_count + 1):
        knot_pos.update({i: starting_pos})
        knot_paths.update({i: [starting_pos]})
        # knot_pos.update({: starting_pos})

    # knot_paths.update({0: [starting_pos]})
    # knot_paths.update({1: [starting_pos]})
    for row in input.splitlines():
        direction = row.split(' ')[0]
        magnitude = int(row.split(' ')[1])
        if direction == 'R':
            x_change = 1
            y_change = 0
        elif direction == 'L':
            x_change = -1
            y_change = 0
        elif direction == 'U':
            x_change = 0
            y_change = 1
        elif direction == 'D':
            x_change = 0
            y_change = -1
        for _ in range(magnitude):
            head_x = knot_pos[0][0] + x_change
            head_y = knot_pos[0][1] + y_change
            new_head_pos = (head_x, head_y)

            knot_pos.update({0: new_head_pos})
            knot_paths[0].append(new_head_pos)

            for curr_knot in range(1, knot_count + 1):
                (tail_x, tail_y) = calculate_knot_path(curr_knot - 1, curr_knot)
                new_tail_pos = (tail_x, tail_y)
                knot_pos.update({curr_knot: new_tail_pos})
                knot_paths[curr_knot].append(new_tail_pos)
            
    distinct_tail_positions = set(knot_paths[knot_count])
    return len(distinct_tail_positions)


def main():
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'sample_input.txt')
    filename = os.path.join(dir, 'input.txt')
    file = open(filename)
    input = file.read()
    part_1_solution = solve(input, 1)
    # Part 2 solution works on the sample input but not the real input :(
    part_2_solution = solve(input, 9)

    print("Part 1: " +  str(part_1_solution))
    print("Part 2: " +  str(part_2_solution))
main()
