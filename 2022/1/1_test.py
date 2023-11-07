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


class IntegerArithmeticTestCase(unittest.TestCase):
    def testExample(self):
        sum, maximum = puzzle("2022/1/example_input.txt")
        self.assertEqual(maximum, 24000)
        self.assertEqual(sum, 45000)

    def testSomeInput(self):
        sum, maximum = puzzle("2022/1/some_input.txt")
        self.assertEqual(maximum, 34142)
        self.assertEqual(sum, 64146)

    def testInput(self):
        sum, maximum = puzzle("2022/1/input.txt")
        self.assertEqual(maximum, 75501)
        self.assertEqual(sum, 215594)


if __name__ == "__main__":
    unittest.main()
