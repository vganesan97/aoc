def get_card_infos(file):
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
    cards_info = get_card_infos(file)
    total = 0
    for k, v in cards_info.items():
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

def total_points_2(file):
    card_infos = get_card_infos(file)
    for k, v in card_infos.items():
        v.append(1)
    for k in card_infos:
        win, mine, copies = card_infos[k]
        count = 0
        for num in mine:
            if num in win:
                count += 1
        for _ in range(copies):
            for i in range(count):
                card_infos[k+i+1][2] += 1
    return sum([x[2] for x in card_infos.values()])


file_name = "input4.txt"
with open(file_name, 'r') as file:
    res = total_points_2(file)
    print(res)
