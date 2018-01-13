import unittest
from tsp import *

class TSP(unittest.TestCase):


    def test_compute_total_distance(self):
        numbers = [('first', 'set', '2', '3'), ('second', 'set', '7', '3'), ('third', 'set', '5', '1')]
        self.assertAlmostEqual(compute_total_distance(numbers), distance(2, 3, 7, 3) + distance(7, 3, 5, 1) + distance(5, 1, 2, 3))

    def test_swap_adjacent_cities(self):
        self.assertEqual(swap_adjacent_cities(read_cities("cities.txt"), 1)[0][1], read_cities("cities.txt")[2])
        self.assertEqual(swap_adjacent_cities(read_cities("cities.txt"), 1)[0][2], read_cities("cities.txt")[1])

    def test_swap_cities(self):
        self.assertEqual(swap_cities(read_cities("cities.txt"), 1, 3)[0][1], read_cities("cities.txt")[3])
        self.assertEqual(swap_cities(read_cities("cities.txt"), 1, 3)[0][3], read_cities("cities.txt")[1])

    def test_find_best_cycle(self):
        road_map = read_cities("cities.txt")
        self.assertEqual(set(find_best_cycle(road_map)), set(road_map))
        self.assertFalse(find_best_cycle(road_map) == road_map)

unittest.main()
