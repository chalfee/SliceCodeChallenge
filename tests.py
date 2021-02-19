from unittest import TestCase


import pizzabot


class TestPizzaBot(TestCase):
    def test_get_grid_size_without_grid_boundaries(self):
        self.assertEqual(pizzabot.get_grid_size('(1, 3) (4, 4)'), None)

    def test_get_grid_size(self):
        self.assertEqual(pizzabot.get_grid_size('5x5 (1, 3) (4, 4)'), (5, 5))

    def test_check_points_boundaries_out_of_boundaries(self):
        self.assertEqual(pizzabot.check_points_boundaries((5, 5), [(1, 3), (6, 4)]), False)

    def test_check_points_boundaries_within_the_boundaries(self):
        self.assertEqual(pizzabot.check_points_boundaries((5, 5), [(1, 3), (4, 4)]), True)

    def test_pizzabot_without_points(self):
        self.assertEqual(pizzabot.pizzabot('5x5'), '')

    def test_pizzabot(self):
        self.assertEqual(pizzabot.pizzabot('5x5 (1, 3) (4, 4)'), 'ENNNDEEEND')

    def test_convert_grid_definition_to_points_without_points(self):
        self.assertEqual(pizzabot.convert_grid_definition_to_points('5x5'), [])

    def test_convert_grid_definition_to_points(self):
        self.assertEqual(pizzabot.convert_grid_definition_to_points('5x5 (1, 3) (4, 4)'), [(1, 3), (4, 4)])

    def test_convert_string_to_coordinates(self):
        self.assertEqual(pizzabot.convert_string_to_coordinates('(1, 2)'), (1, 2))

    def test_get_path_with_same_points(self):
        self.assertEqual(pizzabot.get_bot_commands([(0, 0), (0, 0)]), 'DD')

    def test_get_path(self):
        self.assertEqual(pizzabot.get_bot_commands([(1, 3), (4, 4)]), 'ENNNDEEEND')

    def test_get_path_list_items_deleted(self):
        initial_list = [(0, 1), (1, 0), (2, 2)]
        pizzabot.get_bot_commands(initial_list)
        self.assertEqual(initial_list, [])

    def test_find_nearest_point_with_same_points(self):
        self.assertEqual(pizzabot.find_nearest_point((0, 0), [(2, 1), (0, 0), (2, 4)]), (0, 0))

    def test_find_nearest_point(self):
        self.assertEqual(pizzabot.find_nearest_point((2, 1), [(2, 5), (0, 0), (3, 2)]), (3, 2))

    def test_find_path_between_two_points_with_same_points(self):
        self.assertEqual(pizzabot.find_path_between_two_points(1, 1, 1, 1), '')

    def test_find_path_between_two_points(self):
        self.assertEqual(pizzabot.find_path_between_two_points(3, 0, 2, 1), 'WN')

    def test_get_distance_with_same_points(self):
        self.assertEqual(pizzabot.get_distance(0, 0, 0, 0), 0)

    def test_get_distance(self):
        self.assertAlmostEqual(pizzabot.get_distance(0, 0, 1, 1), 1.41421, 5)
