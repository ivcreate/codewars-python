def generate_number(digit_system: int, count_numbers: int, prefix=None):
    prefix = prefix or []

    if count_numbers is 0:
        print(prefix)
        return

    for digit in range(digit_system):
        prefix.append(digit)
        generate_number(digit_system, count_numbers - 1, prefix)
        prefix.pop()

generate_number(5, 4)