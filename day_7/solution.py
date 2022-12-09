import math, os

directory_tree = {'/': {}}
current_dir = ''
total_sizes = {}
used_space = 0

def parse_command(cmd):
    global current_dir
    command_type = cmd[1]
    if command_type == 'cd':
        dir_change = cmd[2]
        if dir_change == '/':
            current_dir = '/'
        elif dir_change == '..':
            current_dir = '/'.join(current_dir.split('/')[:-2]) + '/'
        else:
            current_dir = current_dir + dir_change + '/'
    # We can ignore the ls command technically and just parse the values of the current directory

# This doesn't correctly calculate the size for '/', but that doesn't matter
# in this case because we track total used space in the global var
def combine_directories():
    global total_sizes
    for dir, total_size in total_sizes.items():
        super_dirs = dir.split('/')
        build_up_super = '/'
        for super in super_dirs:
            if super != '':
                build_up_super = build_up_super + super + '/'
                if build_up_super != '//' and build_up_super != dir:
                    existing_super_size = total_sizes.get(build_up_super)
                    total_sizes.update({build_up_super: existing_super_size + total_size})
    print(total_sizes)

def calculate_total_sizes():
    global total_sizes
    for dir, contents in directory_tree.items():
        contents_sum = sum(contents.values())
        total_sizes.update({dir: contents_sum})
    combine_directories()

def get_target_directories():
    sum_of_dirs = 0
    for total_size in total_sizes.values():
        if total_size <= 100000:
            sum_of_dirs += total_size
    return sum_of_dirs

def part_1(input):
    global used_space
    for line in input.splitlines():
        split_line = line.split(' ')
        if split_line[0] == '$':
            parse_command(split_line)
        elif split_line[0] == 'dir':
            directory_tree.update({current_dir + split_line[1] + '/': {}})
        else:
            current_directory_files = directory_tree.get(current_dir)
            current_directory_files.update({split_line[1]: int(split_line[0])})
            used_space += int(split_line[0])
    calculate_total_sizes()
    sum_of_dirs = get_target_directories()
    return sum_of_dirs

def get_sum_of_all_root_dirs():
    sum_of_dirs = 0
    for dir, total_size in total_sizes.items():
        if len(dir) <= 3:
            sum_of_dirs += total_size
    return sum_of_dirs

def part_2():
    unused_space = 70000000 - used_space
    needed_space = 30000000 - unused_space
    possible_dirs = {}
    for dir, size in total_sizes.items():
        if dir != '/' and size >= needed_space:
            possible_dirs.update({dir: size})
    best_option = min(possible_dirs.values())
    return best_option



def main():
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'sample_input.txt')
    filename = os.path.join(dir, 'input.txt')
    file = open(filename)
    input = file.read()
    part_1_solution = part_1(input)
    part_2_solution = part_2(input)

    print("Part 1: " +  str(part_1_solution))
    print("Part 2: " +  str(part_2_solution))
main()