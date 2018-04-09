#!/opt/local/bin/python3

import math

# only attempts the simple cases
def solve(case):
    area = float(case)
    rot_angle = math.acos(area/ math.sqrt(2))  # derived from the projection
    x = math.sin(rot_angle) * 0.5
    y = math.sin(rot_angle) * 0.5
    print('%f %f 0' % (x,y))
    print('%f %f 0' % (-1*x,y))
    print('0.5 0.5 0')

def main():
    num_cases = int(input()) # T
    for i in range(1, num_cases+1):
        case = input() # one line with the desirce size
        print('Case #%d:' % (i))
        solve(case)


if __name__ == '__main__':
    main()