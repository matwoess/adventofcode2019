from challenges.challenge import Challenge


def test_conditions1(number):
    digits = [int(d) for d in str(number)]
    six_digits = len(digits) == 6
    in_range = 100000 <= number <= 999999
    adjacent_digits = False
    increasing = True

    last_digit = digits[0]
    digits.remove(digits[0])
    for d in digits:
        if d == last_digit:
            adjacent_digits = True
        if d < last_digit:
            increasing = False
        last_digit = d
    return six_digits and in_range and adjacent_digits and increasing


def test_conditions2(number):
    digits = [int(d) for d in str(number)]
    six_digits = len(digits) == 6
    in_range = 100000 <= number <= 999999
    increasing = sorted(digits) == digits
    pair_of_matching_digits = False
    for i in range(0, 10):
        count = sum([1 for d in digits if d == i])
        if count == 2:
            pair_of_matching_digits = True
    return six_digits and in_range and pair_of_matching_digits and increasing


class Day04(Challenge):
    input = range(246540, 787419 + 1)

    def part1(self):
        result = list()
        for i in self.input:
            if test_conditions1(i):
                result.append(i)
        self.print_result(len(result))

    def part2(self):
        result = list()
        for i in self.input:
            if test_conditions2(i):
                result.append(i)
        self.print_result(len(result))
