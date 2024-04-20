import math
def quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        answer1 = (-b + math.sqrt(discriminant)) / (2 * a)
        answer2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return answer1, answer2
    elif discriminant == 0:
        answer = -(b / (2 * a))
        return answer
    else:
        return "Discriminant less than 0, no roots"
