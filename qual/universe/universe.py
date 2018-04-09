#!/opt/local/bin/python3

CHARGE = 'C'
SHOOT  = 'S'


def find_strength(program):
    strength = 1
    total = 0
    for i in program:
        if i == CHARGE:
            strength *= 2
        elif i == SHOOT:
            total += strength
    return total


def find_biggest_swap(program):
    i = len(program)
    # if i == 1:
    #     return program
    while i > 0:
        i -= 1
        if program[i] == SHOOT and program[i-1] == CHARGE:
            # here we can make a swap that will help us
            return program[:i-1] + program[i] + program[i-1] + program[i+1:]
    return program


def solve(case):
    max_strength_str, program = case.split(' ')
    max_strength = int(max_strength_str)
    curr_strength = find_strength(program)

    num_swaps = 0
    while curr_strength > max_strength:
        new_program = find_biggest_swap(program)
        if new_program == program:
            # can't make any changes that will help us here
            return 'IMPOSSIBLE'
        else:
            program = new_program
            new_strength = find_strength(program)
            num_swaps += 1
            if (new_strength > curr_strength):
                return 'IMPOSSIBLE'
            else:
                curr_strength = new_strength
    return str(num_swaps)



def main():
    num_cases = int(input()) # T
    for i in range(1, num_cases+1):
        case = input() # one line with D and then a space and then program
        print('Case #%d: %s' % (i,solve(case)))


if __name__ == '__main__':
    main()