import math


def quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        answer_1 = (-b + math.sqrt(discriminant) / 2 * a)
        answer_2 = (-b - math.sqrt(discriminant) / 2 * a)
        return answer_1, answer_2
    elif discriminant == 0:
        answer = -(b / 2 * a)
        return answer
    else:


if __name__ == '__main__':
    quadratic_equation(6, 3, -3)
    print(quadratic_equation())