def solve():
    with open("input.txt", 'r', encoding='utf-8') as f:
        line = f.read()

    open_el = '{'
    close_el = '}'
    o_cnt = 0
    c_cnt = 0
    o_index = len(line) + 1
    c_index = len(line) + 1

    ans = ''

    for i in range(len(line)):
        if line[i] == open_el:
            o_cnt += 1
            o_index = min(i, o_index)

        if line[i] == close_el:
            c_cnt += 1
            if o_cnt == c_cnt:
                o_index = len(line) + 1
                c_index = len(line) + 1
            else:
                c_index = min(i, c_index)

        if line[i] == '=' or i == len(line) - 1:
            if o_cnt - c_cnt == 1:
                ans = o_index + 1
            elif c_cnt - o_cnt == 1:
                ans = c_index + 1
            elif c_cnt == o_cnt:
                o_index = len(line) + 1
                c_index = len(line) + 1
            else:
                return -1

    if o_index == c_index == len(line) + 1:
        return -1

    return ans


print(solve())
