import os

values = {'X': 1, 'Y': 2, 'Z': 3}
opp_values = {'A': 1, 'B': 2, 'C': 3}
    
part_2_moves = {'AX': 'C', 'AY': 'A', 'AZ': 'B', 'BX': 'A', 'BY': 'B', 'BZ': 'C', 'CX': 'B', 'CY': 'C', 'CZ': 'A'}
part_2_win_values = {'X': 0, 'Y': 3, 'Z': 6}
def win_points(opp, me):
    diff = values[me] - opp_values[opp]
    # Win
    if diff == -2:
        return 6
    # Lose
    elif diff == -1:
        return 0
    # Tie
    elif diff == 0:
        return 3
    # Win
    elif diff == 1:
        return 6
    # Lose
    elif diff == 2:
        return 0
    
    
def part_1(input):
    score = 0
    for line in input.splitlines():
        opp, me = line.split(' ')[0], line.split(' ')[1]
        score += values[me]
        score += win_points(opp, me)
        
    return score

def part_2(input):
    score = 0
    for line in input.splitlines():
        opp, end_state = line.split(' ')[0], line.split(' ')[1]
        move = part_2_moves.get(opp + end_state)
        move_score = opp_values.get(move)
        end_state_score = part_2_win_values.get(end_state)
        score += move_score
        score += end_state_score
    return score

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