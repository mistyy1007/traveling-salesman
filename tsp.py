import random
from earth_distance import *

def read_cities(file_name):
    map_file = open(file_name, 'r')
    road_map = list(map(lambda x: tuple(x.strip('\n').split('\t')), map_file.readlines()))
    map_file.close()
    return road_map

def print_cities(road_map):
    for city in road_map:
        print(city[0], city[1], round(float(city[2]),2), round(float(city[3]),2))


def compute_total_distance(road_map):
    total_distance = 0
    for i in range (0,len(road_map)):
        total_distance += distance(float(road_map[i][2]), float(road_map[i][3]), float(road_map[(i+1)%len(road_map)][2]), float(road_map[(i+1)%len(road_map)][3]))
    return total_distance
    
def swap_adjacent_cities(road_map, index):
    new_road_map = road_map[:]
    new_road_map[index] = road_map[(index+1) % len(road_map)]
    new_road_map[(index+1) % len(road_map)] = road_map[index]
    new_total_distance = compute_total_distance(new_road_map)
    return (new_road_map, new_total_distance)

def swap_cities(road_map, index1, index2):
    new_road_map = road_map[:]
    new_road_map[index1] = road_map[index2]
    new_road_map[index2] = road_map[index1]
    new_total_distance = compute_total_distance(new_road_map)
    return (new_road_map, new_total_distance)

def find_best_cycle(road_map):
    map_distance = []
    new_road_map = road_map[:]
    for i in range(0, 10000):
        r = random.randint(0, len(new_road_map) - 1)
        j = random.randint(0, len(new_road_map) - 1)
        k = random.randint(0, len(new_road_map) - 1)
        map_distance.append(swap_adjacent_cities(new_road_map, r))
        map_distance.append(swap_cities(new_road_map, k, j))
        new_road_map = min(map_distance, key = lambda x:x[1])[0]
    return new_road_map

def print_map(road_map):
    for i in range(0, len(road_map)):
        print ("From", road_map[i][0], "to", road_map[(i + 1) % len(road_map)][0], "is", distance(float(road_map[i][2]), float(road_map[i][3]), float(road_map[(i + 1) % len(road_map)][2]), float(road_map[(i + 1) % len(road_map)][3])))
    print ("The total cost is:", compute_total_distance(road_map))

def main():
    print('Analyzing...Please wait.')
    road_map = find_best_cycle(read_cities('cities.txt'))
    print_map(road_map)

main()
