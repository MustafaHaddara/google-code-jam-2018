#!/opt/local/bin/python3
import sys

def log(s):
    if (s[-1] != '\n'):
        s += '\n'
    # sys.stderr.write(s)
    # sys.stderr.flush()

def prepare(num_cells):
    ## init empty field
    ## we can get away with this dirty hack because we are told num_cells is either 20 or 200
    log('num_cells: %d\n' % (num_cells))
    width = int(num_cells / 5)
    height = 5
    field = [ [ False for i in range(width) ] for i in range(height) ]
    log('field size: %dx%d\n' % (width, height))
    log(str( len(field) ) + ' ' + str( len(field[0]) ))

    ## three phases
    # step 1: try and get the inner most rect prepared
    # step 2: do a second pass on the inner most rect again?
    # step 3: 'force' a cell to be prepared by requesting it over and over until it is prepared

    # phase 1
    for h in range(1, height-1):
        for w in range(1, width-1):
            request_field(w, h)
            sys.stdout.flush()
            if recieve_response(field):
                return

    # phase 2
    for h in range(1, height-1):
        for w in range(1, width-1):
            if field[h][w]:
                continue
            request_field(w, h)
            if recieve_response(field):
                return

    # phase 3
    log('PHASE 3')
    for h in range(height):
        for w in range(width):
            if field[h][w]:
                continue
            if w == 0:
                req_w = 1
            elif w == width-1:
                req_w = width-2
            else:
                req_w = w

            if h == 0:
                req_h = 1
            elif h == height-1:
                req_h = height-2
            else:
                req_h = h

            log('attempting to clean %d %d' % (w,h))
            while not field[h][w]:
                request_field(req_w, req_h)
                if recieve_response(field):
                    return

def request_field(w, h):
    log('writing to %d %d\n' % (w, h))
    print('%d %d' % (w+1, h+1))  # 1-indexed, ew
    sys.stdout.flush()

def recieve_response(field):
    raw_w, raw_h = [int(x) for x in input().split(' ')]
    if raw_h == 0 and raw_w == 0:
        return True
    if raw_h == -1 and raw_w == -1:
        return True
    act_w, act_h = raw_w-1, raw_h-1
    log('%d %d\n' % (act_w, act_h))
    log(str(field[act_h]))
    log(str(field[act_h][act_w]))
    field[act_h][act_w] = True
    return False

def main():
    num_cases = int(input()) # T
    for i in range(1, num_cases+1):
        num_cells = int(input())
        prepare(num_cells)

if __name__ == '__main__':
    main()