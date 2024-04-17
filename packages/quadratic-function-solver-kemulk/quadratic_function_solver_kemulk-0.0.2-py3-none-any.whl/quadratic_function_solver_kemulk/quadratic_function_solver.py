import cmath
import math


def solve_quadratic_function(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(root1, root2)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        print(root)
        return root,
    else:
        print("Ruutvõrrandil puudub lahend")
        return "Ruutvõrrandil puudub lahend"


if __name__ == "__main__":
    solve_quadratic_function(3, 3, 4)
    solve_quadratic_function(2, 5, 2)
