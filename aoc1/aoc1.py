file_name = 'input1.txt'
def sum_calibration_vals(file):
    nums = list()
    digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8",
              "nine": "9"}
    for line in file:
        first = None
        second = None

        for r in range(len(line)):
            for k in digits.keys():
                if k in line[:r + 1]:
                    first = digits[k]
                    break
            if first: break
            if 48 <= ord(line[r]) <= 57:
                first = line[r]
                break

        l_ptr = len(line) - 1
        while l_ptr >= 0:
            for k in digits.keys():
                if line[l_ptr:].startswith(k):
                    second = digits[k]
                    break
            if second: break
            if 48 <= ord(line[l_ptr]) <= 57:
                second = line[l_ptr]
                break
            l_ptr -= 1

        nums.append(first + second)
    return sum([int(num) for num in nums])


with open(file_name, 'r') as file:
    res = sum_calibration_vals(file)
    print(res)
