"""Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?"""

import math

print(int(math.factorial(40)/(math.factorial(20)**2)))

"""permutation with repetition 

we need 40 moves: 20 rights and 20 downs

How many ways can we arrange 20 rights and 20 downs.
"""