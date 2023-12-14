def card_infos(file):
    card_infos = dict()
    for line in file:
        line = line.strip()
        card_num = line.split(':')
        num = card_num[0].split('Card')[1]
        x = card_num[1].split('|')
        my_nums = [int(num) for num in x[1].split()]
        winning_nums = [int(num) for num in x[0].split()]
        card_infos[int(num)] = [winning_nums, my_nums]
    return card_infos

def total_points(file):
    cards_info = card_infos(file)
    total = 0
    for k,v in cards_info.items():
        curr_total = 0
        win, mine = v
        for num in mine:
            if num in win:
                if curr_total == 0:
                    curr_total = 1
                else:
                    curr_total *= 2
        total += curr_total
    return total

file_name = "input4.txt"
with open(file_name, 'r') as file:
    res = total_points(file)
    print(res)