import re

def parse_input(line):
    game_pattern = r'Game (\d+): (.*)'
    color_pattern = r'(\d+) (red|green|blue)'
    game_match = re.search(game_pattern, line)

    game_id, color_string = game_match.groups()
    turns = color_string.split(';')
    turns_data = []

    for turn in turns:
        color_matches = re.findall(color_pattern, turn.strip())
        d = dict()
        for count, color in color_matches:
            d[color] = int(count)
        turns_data.append(d)

    game = {
        'game_id': int(game_id),
        'turns': turns_data
    }
    print(game)
    return game

def sum_possible_games(file):
    curr_sum = 0
    for line in file:
        curr_id = None
        game_info = parse_input(line)
        red_max, green_max, blue_max = 0, 0, 0
        for turn in game_info['turns']:
            for color, count in turn.items():
                if color == 'green':
                    green_max = max(green_max, count)
                if color == 'blue':
                    blue_max = max(blue_max, count)
                if color == 'red':
                    red_max = max(red_max, count)
        if curr_id != 0:
            prod = red_max * green_max * blue_max
            curr_sum += prod
    return curr_sum

file_name = "input2.txt"
with open(file_name, 'r') as file:
    res = sum_possible_games(file)
    print(res)