import os
    
def part_1(input):
    running_total = 0
    curr_max = 0
    for line in input.splitlines():
        if line.strip():
            running_total += int(line)
        else:
            if running_total >= curr_max:
                curr_max = running_total
            running_total = 0
    return curr_max

def part_2(input):
    running_total = 0
    top_3 = [0, 0, 0]
    for line in input.splitlines():
        if line.strip():
            running_total += int(line)
        else:
            if any(i < running_total for i in top_3):
                top_3.append(running_total)
                top_3.remove(min(top_3))
            running_total = 0
    if any(i < running_total for i in top_3):
        top_3.append(running_total)
        top_3.remove(min(top_3))
    return sum(top_3)


def main():
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'input.txt')
    file = open(filename)
    input = file.read()
    part_1_solution = part_1(input)
    part_2_solution = part_2(input)

    print("The elf carrying the most calories is carrying " +  str(part_1_solution) + " calories")
    print("The three elves carrying the most calories are carrying a total of " +  str(part_2_solution) + " calories")
main()