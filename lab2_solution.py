
# Q1
def day_of_week(day, offset):
    return (day + offset) % 7


# Q2
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Q3
def type_triangle(s1, s2, s3):
    s1, s2, s3 = sorted([s1, s2, s3])
    if s3 >= (s1 + s2):
        return 0
    else:
        sum_square_12 = s1**2 + s2**2
        square_3 = s3**2
        if sum_square_12 > square_3:
            return 1
        elif sum_square_12 == square_3:
            return 2
        else:
            return 3


if __name__ == '__main__':
    # If you want to use input, use it here, inside the if statement
    # day = float(input("Enter day:"))
    # offset = float(input("Enter offset:"))
    day = 1
    offset = 2

    # Testing Q1
    print(day_of_week(day, offset))

    # Testing Q2
    print(is_leap_year(2022))

    # Testing Q3
    print(type_triangle(3, 5, 4))
