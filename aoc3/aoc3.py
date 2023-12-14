def convert_to_grid(file):
    grid = list()
    for line in file:
        line = line.strip()
        row = list()
        for char in line:
            if 48 <= ord(char) <= 57:
                row.append(int(char))
            else:
                row.append(char)
        grid.append(row)
    return grid


def get_num(grid, cell):
    row, col = cell[0], cell[1]
    digits = ""
    idx, idx2 = col, col - 1
    while idx < len(grid[0]) and grid[row][idx] != -1 and isinstance(grid[row][idx], int):
        digits = digits + str(grid[row][idx])
        grid[row][idx] = (-1, grid[row][idx])
        idx += 1

    while idx2 >= 0 and grid[row][idx2] != -1 and isinstance(grid[row][idx2], int):
        digits = str(grid[row][idx2]) + digits
        grid[row][idx2] = (-1, grid[row][idx2])
        idx2 -= 1
    return int(digits)


def get_num_ratios(grid, cell):
    row, col = cell[0], cell[1]
    digits = ""
    idx, idx2 = col, col - 1
    while idx < len(grid[0]) and isinstance(grid[row][idx], tuple):
        digits = digits + str(grid[row][idx][1])
        grid[row][idx] = grid[row][idx][1]
        idx += 1

    while idx2 >= 0 and isinstance(grid[row][idx2], tuple):
        digits = str(grid[row][idx2][1]) + digits
        grid[row][idx2] = grid[row][idx2][1]
        idx2 -= 1

    int_digits = int(digits)
    # print(int_digits)
    return int_digits


def sum_part_nums(file):
    grid = convert_to_grid(file)
    rows = len(grid)
    cols = len(grid[0])
    nums = list()
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != -1 and isinstance(grid[row][col], int):
                shifts = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
                for x, y in shifts:
                    dx = x + row
                    dy = y + col
                    if (
                            0 <= dx < rows and
                            0 <= dy < cols and
                            grid[dx][dy] != -1 and
                            grid[dx][dy] != '.' and
                            not isinstance(grid[dx][dy], int)
                    ):
                        num = get_num(grid, (row, col))
                        nums.append(num)
                        break
    summ = sum(nums)
    rsum = sum_ratios(grid)
    print(grid)
    return [summ, rsum]


def sum_ratios(grid):
    rows = len(grid)
    cols = len(grid[0])
    ratios = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '*':
                shifts = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
                curr_nums = list()
                for x, y in shifts:
                    dx = x + row
                    dy = y + col
                    if (
                            0 <= dx < rows and
                            0 <= dy < cols and
                            isinstance(grid[dx][dy], tuple)
                    ):
                        num = get_num_ratios(grid, (dx, dy))
                        print(curr_nums)
                        curr_nums.append(num)
                if len(curr_nums) == 2:
                    prod = curr_nums[0] * curr_nums[1]
                    print(f"{curr_nums} {prod}")
                    ratios += prod
    return ratios


file_name = "input3.txt"
with open(file_name, 'r') as file:
    res = sum_part_nums(file)
    print(res)
