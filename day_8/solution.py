import math, os, numpy

def parse_input(input):
    tree_map = []
    for input_row in input.splitlines():
        curr_row = []
        for cell in input_row:
            curr_row.append(cell)
        tree_map.append(curr_row)
    return tree_map

def part_1(tree_map):
    visible_trees = 0
    grid_length = len(tree_map[0])
    grid_height = len(tree_map)
    visibility_row = [0] * grid_length
    visibility_map = []
    for i in range(0, grid_height):
        visibility_map.append(visibility_row.copy())
    transposed_map = numpy.transpose(tree_map)
    for row_idx, row in enumerate(tree_map):
        for col_idx, cell in enumerate(row):
            if col_idx == 0 or row_idx == 0 or col_idx == grid_length - 1 or row_idx == grid_height - 1:
                visibility_map[row_idx][col_idx] = 1
                visible_trees += 1
            else:
                cell = int(cell)
                column = transposed_map[col_idx]
                # visibility check
                left_highest = int(max(row[:col_idx]))
                right_highest = int(max(row[col_idx + 1:]))
                up_highest = int(max(column[:row_idx]))
                down_highest = int(max(column[row_idx + 1:]))
                if cell > left_highest or cell > right_highest or cell > up_highest or cell > down_highest:
                    visibility_map[row_idx][col_idx] = 1
                    visible_trees += 1
    
    return visible_trees
    

def part_2(tree_map):
    max_scenic_score = 0
    transposed_map = numpy.transpose(tree_map)
    for row_idx, row in enumerate(tree_map):
        for col_idx, cell in enumerate(row):
            cell = int(cell)
            column = transposed_map[col_idx]
            reversed_row = list(reversed(row))
            reversed_column = list(reversed(column))
            # scenic check
            left_view = 0
            right_view = 0
            up_view = 0
            down_view = 0
            for left in reversed_row[len(column) - col_idx:]:
                left_view += 1
                if int(left) >= cell:
                    break
            for right in row[col_idx + 1:]:
                right_view += 1
                if int(right) >= cell:
                    break
            for up in reversed_column[len(row) - row_idx:]:
                up_view += 1
                if int(up) >= cell:
                    break
            for down in column[row_idx + 1:]:
                down_view += 1
                if int(down) >= cell:
                    break

            curr_scenic_score = left_view * right_view * up_view * down_view
            if curr_scenic_score > max_scenic_score:
                max_scenic_score = curr_scenic_score
    
    return max_scenic_score


def main():
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'sample_input.txt')
    filename = os.path.join(dir, 'input.txt')
    file = open(filename)
    input = file.read()
    tree_map = parse_input(input)
    part_1_solution = part_1(tree_map)
    part_2_solution = part_2(tree_map)

    print("Part 1: " +  str(part_1_solution))
    print("Part 2: " +  str(part_2_solution))
main()