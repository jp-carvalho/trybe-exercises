def minimum(numbers):
    smaller = numbers[0]
    for number in numbers:
        if number < smaller:
            smaller = number
    return smaller


# ===========================


def minimum2(numbers):
    return min(numbers)


# ou mesmo
minimum3 = min
