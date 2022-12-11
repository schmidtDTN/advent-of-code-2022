import math, re, os

class Monkey:
    def __init__(self, id, items, operation, divisibility_test, if_true, if_false, part):
        self.id = id
        self.items = [int(item) for item in items]
        self.operation = operation
        self.divisibility_test = int(divisibility_test)
        self.if_true = int(if_true)
        self.if_false = int(if_false)
        self.part = part
        self.inspection_count = 0

    def take_turn(self):
        while len(self.items) > 0:
            self.inspection_count += 1
            item = self.items.pop(0)
            item_operation = self.operation.replace("old", str(item))
            item = int(eval(item_operation))
            if self.part == 1:
                item = int(math.floor(float(item) / 3.0))
            # Divisibility check
            if item % self.divisibility_test == 0:
                # Throw item to true monkey
                receiving_monkey = monkeys[self.if_true]
                receiving_monkey.catch_item(item)
            else:
                # Throw item to false monkey
                receiving_monkey = monkeys[self.if_false]
                receiving_monkey.catch_item(item)
    
    def catch_item(self, item):
        self.items.append(item)

    def get_inspection_count(self):
        return self.inspection_count

monkeys = {}

def parse_monkey(monkey_rows, part):
    monkey_id = int(re.search(r"\d+", monkey_rows[0]).group())
    starting_items = re.findall(r"\d+", monkey_rows[1])
    operation = re.search(r"= .+", monkey_rows[2]).group().split('= ')[1]
    divisibility_test = re.search(r"\d+", monkey_rows[3]).group()
    monkey_if_true = re.search(r"\d+", monkey_rows[4]).group()
    monkey_if_false = re.search(r"\d+", monkey_rows[5]).group()
    monkey = Monkey(monkey_id, starting_items, operation, divisibility_test, monkey_if_true, monkey_if_false, part)
    monkeys.update({monkey_id: monkey})

def part_1(input):
    current_monkey_lines = []
    for line in input.splitlines():
        # Second condition is to not do this before monkey 0 is loaded
        if line.startswith("Monkey") and len(current_monkey_lines) != 0:
            parse_monkey(current_monkey_lines, 1)
            current_monkey_lines.clear()
        current_monkey_lines.append(line)
    # Parse the last monkey
    parse_monkey(current_monkey_lines, 1)
    current_round = 1
    max_monkey = max(monkeys.keys())
    while current_round <= 20:
        for curr_monkey in range(0, max_monkey + 1):
            monkeys[curr_monkey].take_turn()
        current_round += 1
    inspection_counts = []
    for monkey in range(0, max_monkey + 1):
        count = monkeys[monkey].get_inspection_count()
        inspection_counts.append(count)
    inspection_counts.sort(reverse=True)
    max_monkey = inspection_counts.pop(0)
    second_monkey = inspection_counts.pop(0)
    return max_monkey * second_monkey

    

def part_2(input):
    return 0
#     current_monkey_lines = []
#     for line in input.splitlines():
#         # Second condition is to not do this before monkey 0 is loaded
#         if line.startswith("Monkey") and len(current_monkey_lines) != 0:
#             parse_monkey(current_monkey_lines, 2)
#             current_monkey_lines.clear()
#         current_monkey_lines.append(line)
#     # Parse the last monkey
#     parse_monkey(current_monkey_lines, 2)
#     current_round = 1
#     max_monkey = max(monkeys.keys())
#     while current_round <= 10000:
#         for curr_monkey in range(0, max_monkey + 1):
#             monkeys[curr_monkey].take_turn()
#         current_round += 1
#     inspection_counts = []
#     for monkey in range(0, max_monkey + 1):
#         count = monkeys[monkey].get_inspection_count()
#         inspection_counts.append(count)
#     inspection_counts.sort(reverse=True)
#     max_monkey = inspection_counts.pop(0)
#     second_monkey = inspection_counts.pop(0)
#     return max_monkey * second_monkey



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