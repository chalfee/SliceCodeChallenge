import sys
from math import sqrt
import re
from typing import List, Tuple


def pizzabot(grid_definition: str) -> str:
    """Take string with grid definition and return solution with commands to bot:
    N: Move north
    S: Move south
    E: Move east
    W: Move west
    D: Drop pizza

    :param grid_definition: str in format "grid_sizexgrid_size (x, y) (x, y)"
    :return: str in format "ENNNDEEEND"
    """
    points = convert_grid_definition_to_points(grid_definition)
    if not check_points_boundaries(get_grid_size(grid_definition), points):
        raise ValueError
    return get_bot_commands(points)


def get_grid_size(grid_definition: str) -> Tuple[int, int]:
    """Return size of the grid boundaries"""
    if re.search('[0-9]+.[0-9]+', grid_definition):
        grid_size_string = re.search('[0-9]+.[0-9]+', grid_definition).group(0)
        separator = re.search('\D', grid_definition).group(0)
        x, y = grid_size_string.split(separator)
        return int(x), int(y)
    else:
        return None


def check_points_boundaries(boundaries: Tuple[int, int], points: List[Tuple[int, int]]) -> bool:
    """Check if all points are within the boundaries of the grid"""
    for point in points:
        if point[0] > boundaries[0] or point[1] > boundaries[1] or point[0] < 0 or point[1] < 0:
            return False
    return True


def convert_grid_definition_to_points(grid_definition: str) -> List[Tuple[int, int]]:
    """Convert string with grid definition to list of point tuple(x, y)

    :param grid_definition: str in format "grid_sizexgrid_size (x, y) (x, y)"
    :return: list with provided in definition points
    """
    grid_definition = grid_definition.replace(' ', '')
    string_points = re.findall('\([0-9]+,[0-9]+\)', grid_definition)

    return [convert_string_to_coordinates(string_point) for string_point in string_points]


def convert_string_to_coordinates(point: str) -> Tuple[int, int]:
    """Convert string in format "(x,y)" to tuple of int with coordinates"""
    x, y = point[1:-1].split(',')
    return int(x), int(y)


def get_bot_commands(points: List[Tuple[int, int]]) -> str:
    """Return string with commands for bot to path all provided points:
    N: Move north
    S: Move south
    E: Move east
    W: Move west
    D: Drop pizza

    :param points: list
    :return: str
    """
    start_point = (0, 0)
    path = ''
    while points:
        nearest_point = find_nearest_point(start_point, points)
        points.remove(nearest_point)
        path += find_path_between_two_points(*start_point, *nearest_point) + 'D'
        start_point = nearest_point
    return path


def find_nearest_point(start: Tuple[int, int], points: List[Tuple[int, int]]) -> Tuple[int, int]:
    """Find and return nearest point to start from points list

    :param start: start point coordinates
    :param points: list with unvisited points
    :return: nearest point to start
    """
    min_distance = get_distance(*start, *points[0])
    min_index = 0
    for i, point in enumerate(points[1:], 1):
        distance = get_distance(*start, *point)
        if distance < min_distance:
            min_distance = distance
            min_index = i
    return points[min_index]


def get_distance(start_x: int, start_y: int, end_x: int, end_y: int) -> float:
    """Return distance between start and end points"""
    return sqrt((start_x - end_x) ** 2 + (start_y - end_y) ** 2)


def find_path_between_two_points(start_x: int, start_y: int, end_x: int, end_y: int) -> str:
    """Return path from start to end with the following commands:
    N: Move north
    S: Move south
    E: Move east
    W: Move west


    :param start_x: x coordinate of start point
    :param start_y: y coordinate of start point
    :param end_x: x coordinate of end point
    :param end_y: y coordinate of end point
    :return: str in format "EEEN"
    """
    path = ''

    x_difference = start_x - end_x
    if x_difference < 0:
        path += 'E' * (-1 * x_difference)
    else:
        path += 'W' * x_difference

    y_difference = start_y - end_y
    if y_difference < 0:
        path += 'N' * (-1 * y_difference)
    else:
        path += 'S' * y_difference

    return path


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ValueError
        arg = sys.argv[1].replace(' ', '')
        if re.search('^([0-9]+.[0-9]+)(\([0-9]+,[0-9]+\))*$', arg):
            print(pizzabot(arg))
        else:
            raise ValueError
    except ValueError:
        print('Run command in this format: python3 pizzabot.py "your grid definition"\n'
              'Where "your grid definition" in format '
              '"5x5 (1, 3) (4, 4)"\n'
              'And the coordinates must be positive and within the boundaries of the grid')
