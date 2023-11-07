import unittest


def puzzle(filename):
    top_three = list()
    with open(filename) as f:
        accumulator = 0
        for line in f.readlines():
            line = line.strip()
            if len(line) == 0:
                top_three.append(accumulator)
                accumulator = 0
            else:
                accumulator += int(line)
        # get the last accumulated value
        top_three.append(accumulator)
    top_three.sort(reverse=True)
    maximum = top_three[0]
    sum = 0
    for i in range(3):
        sum += top_three[i]
    return (sum, maximum)


class TestCase:
    def __init__(self, input_file, expected_maximum, expected_sum) -> None:
        self.input_file = input_file
        self.expected_maximum = expected_maximum
        self.expected_sum = expected_sum


test_cases = [
    TestCase("2022/1/example_input.txt", 24000, 45000),
    TestCase("2022/1/some_input.txt", 34142, 64146),
    TestCase("2022/1/input.txt", 75501, 215594),
]


class DayOne(unittest.TestCase):
    def testInputs(self):
        for test_case in test_cases:
            with self.subTest(input_file=test_case.input_file):
                sum, maximum = puzzle(test_case.input_file)
                self.assertEqual(maximum, test_case.expected_maximum)
                self.assertEqual(sum, test_case.expected_sum)


if __name__ == "__main__":
    unittest.main()
