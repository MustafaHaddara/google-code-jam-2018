#!/opt/local/bin/python3

def trouble_sort(num_list):
    done = False
    while not done:
        done = True
        for i in range(len(num_list) - 2):
            if num_list[i] > num_list[i+2]:
                done = False
                # reverse the sublist from num_list[i] to num_list[i+2], inclusive
                # notice that num_list[i+1] remins the same!
                num_list[i], num_list[i+2] = num_list[i+2], num_list[i]
    return num_list

def verify_trouble_sort(num_list):
    trouble_sort(num_list)  # sorts in place
    prev = None
    for idx, item in enumerate(num_list):
        num = int(item)
        if prev is None:
            prev = num
            continue
        if num < prev:
            return str(idx-1)
        prev = num
    return 'OK'

def main():
    num_cases = int(input()) # T
    for i in range(1, num_cases+1):
        list_len = input() # one line with list legnth
        str_list = input()
        num_list = [int(i) for i in str_list.split(' ')]
        print('Case #%d: %s' % (i,verify_trouble_sort(num_list)))

if __name__ == '__main__':
    main()