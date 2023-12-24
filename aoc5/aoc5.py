def parse(file):
    seed_soil_map, soil_fert_map, fert_water_map, water_light_map, light_temp_map, temp_humid_map, humid_location_map = [], [], [], [], [], [], []
    seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_location = False, False, False, False, False, False, False
    seeds = list()
    for line in file:
        line = line.strip()
        seeds_str = line.split(':')
        #print(seeds_str)
        if seeds_str[0] == 'seeds':
            for num_char in seeds_str[1].split(' '):
                if num_char:
                    seeds.append(int(num_char))
            continue
        #print(line)
        if "map" in seeds_str[0] and "seed" in seeds_str[0] and "soil" in seeds_str[0]:
            seed_soil = True
        elif "map" in seeds_str[0] and "fertilizer" in seeds_str[0] and "soil" in seeds_str[0]:
            seed_soil = False
            soil_fert = True
        elif "map" in seeds_str[0] and "fertilizer" in seeds_str[0] and "water" in seeds_str[0]:
            soil_fert = False
            fert_water = True
        elif "map" in seeds_str[0] and "light" in seeds_str[0] and "water" in seeds_str[0]:
            fert_water = False
            water_light = True
        elif "map" in seeds_str[0] and "light" in seeds_str[0] and "temperature" in seeds_str[0]:
            water_light = False
            light_temp = True
        elif "map" in seeds_str[0] and "temperature" in seeds_str[0] and "humidity" in seeds_str[0]:
            light_temp = False
            temp_humid = True
        elif "map" in seeds_str[0] and "location" in seeds_str[0] and "humidity" in seeds_str[0]:
            temp_humid = False
            humid_location = True

        nums = line.split(' ')
        if len(nums) == 3:
            nums = [int(y) for y in nums]
        if seed_soil and len(nums) == 3:
            seed_soil_map.append(nums)
        elif soil_fert and len(nums) == 3:
            soil_fert_map.append(nums)
        elif fert_water and len(nums) == 3:
            fert_water_map.append(nums)
        elif water_light and len(nums) == 3:
            water_light_map.append(nums)
        elif light_temp and len(nums) == 3:
            light_temp_map.append(nums)
        elif temp_humid and len(nums) == 3:
            temp_humid_map.append(nums)
        elif humid_location and len(nums) == 3:
            humid_location_map.append(nums)

    # return {
    #     'seeds': seeds,
    #     'seed-to-soil': seed_soil_map,
    #     'soil-to-fert': soil_fert_map,
    #     'fert-to-water': fert_water_map,
    #     'water-to-light': water_light_map,
    #     'light-to-temp': light_temp_map,
    #     'temp-to-humid': temp_humid_map,
    #     'humid-to-loc': humid_location_map,
    # }

    return [
            seeds,
            seed_soil_map,
            soil_fert_map,
            fert_water_map,
            water_light_map,
            light_temp_map,
            temp_humid_map,
            humid_location_map,
        ]

def x(file):
    cons = parse(file)
    min_val = float('inf')
    for seed in cons[0]:
        start = seed
        for i in range(1, len(cons)):
            for j in range(len(cons[i])):
                dest, src, rg = cons[i][j]
                if src <= start <= src + rg:
                    start = (start - src) + dest
                    break
        min_val = min(start, min_val)
    return min_val



file_name = "input5.txt"
with open(file_name, 'r') as file:
    sol = x(file)
    print(sol)
