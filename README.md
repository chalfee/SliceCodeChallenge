# Code Challenge

Program takes the definition of a grid with points and return solution (visit all point and leave pizza at them) with commands to bot:

    N: Move north
    S: Move south
    E: Move east
    W: Move west
    D: Drop pizza


The definition of a grid should look like this:

    5*5 (1, 3) (4, 4) - where 5*5 is the size of the grid and (1, 3) is the coordinates of the point
    
    The coordinates must be positive and within the boundaries of the grid


Run the script in the project's root directory.
Python 3.7+ is required.
**Example**:

    python3 pizzabot.py "5*5 (1, 3) (4, 4)"
