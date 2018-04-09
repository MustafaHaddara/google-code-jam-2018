#!/opt/local/bin/python3

from universe import solve

with open('test.txt') as f:
    test_input = f.readlines()

with open('expected_output.txt') as f:
    expected_output = f.readlines()

test_case_num = 0
for row in test_input[1:]:
    inp = row.strip()
    output = solve(inp)
    expected = expected_output[test_case_num].strip().split(' ')[-1]
    if output == expected:
        print('%s passed!' % inp)
    else:
        print('%s failed! Expected <%s> but got <%s>' % (inp, expected, output))
    test_case_num += 1