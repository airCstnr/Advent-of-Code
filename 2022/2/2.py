#
# Day 2
#
#
# Example:
#
# A Y
# B X
# C Z
#
#
# Part 1:
#
# In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
# In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
# The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
# In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).
#
#
# Part 2:
#
# In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
# In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
# In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
# Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.
#

import unittest

from enum import Enum

EXAMPLE_RELATIVE_PATH = "2022/2/example.txt"
INPUT_RELATIVE_PATH = "2022/2/input.txt"


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(Enum):
    LOST = 0
    DRAW = 3
    WON = 6


def get_total_score(round_scores):
    """Total score is the sum of your scores for each round."""
    return sum(round_scores)


def get_single_round_score(shape_selected: Shape, outcome: Outcome):
    """
    The score for a single round is
        the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
    plus
        the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
    """
    return shape_selected.value + outcome.value


def get_outcome(opponent: Shape, chosen: Shape):
    """
    Classical Rock, Paper, Scissors rules

    TODO : May be improved for readability
    """

    if opponent == chosen:
        return Outcome.DRAW
    if opponent == Shape.PAPER:
        if chosen == Shape.ROCK:
            return Outcome.LOST
        if chosen == Shape.SCISSORS:
            return Outcome.WON
    if opponent == Shape.ROCK:
        if chosen == Shape.PAPER:
            return Outcome.WON
        if chosen == Shape.SCISSORS:
            return Outcome.LOST
    if opponent == Shape.SCISSORS:
        if chosen == Shape.PAPER:
            return Outcome.LOST
        if chosen == Shape.ROCK:
            return Outcome.WON
    raise ArithmeticError


def choose_shape(opponent: Shape, expected: Outcome):
    if expected == Outcome.DRAW:
        return opponent
    if expected == Outcome.WON:
        if opponent == Shape.PAPER:
            return Shape.SCISSORS
        if opponent == Shape.ROCK:
            return Shape.PAPER
        if opponent == Shape.SCISSORS:
            return Shape.ROCK
    if expected == Outcome.LOST:
        if opponent == Shape.PAPER:
            return Shape.ROCK
        if opponent == Shape.ROCK:
            return Shape.SCISSORS
        if opponent == Shape.SCISSORS:
            return Shape.PAPER
    raise ArithmeticError


def get_letters(line: str):
    """Returns letters for given line

    Args:
        line (str): input stream line

    Returns:
        tuple(char, char): opponent_letter, chosen_letter
    """
    opponent_letter, chosen_letter = line.split(" ")
    return opponent_letter, chosen_letter


def get_opponent_shape(letter):
    """Opponent : A for Rock, B for Paper, and C for Scissors"""

    if letter == "A":
        return Shape.ROCK
    if letter == "B":
        return Shape.PAPER
    if letter == "C":
        return Shape.SCISSORS
    raise ValueError(f"Unexpected letter {letter}")


def get_chosen_shape(letter):
    """Response : X for Rock, Y for Paper, and Z for Scissors"""

    if letter == "X":
        return Shape.ROCK
    if letter == "Y":
        return Shape.PAPER
    if letter == "Z":
        return Shape.SCISSORS
    raise ValueError(f"Unexpected letter {letter}")


def get_expected_outcome(letter):
    """
    X means you need to lose
    Y means you need to end the round in a draw,
    and Z means you need to win
    """
    if letter == "X":
        return Outcome.LOST
    if letter == "Y":
        return Outcome.DRAW
    if letter == "Z":
        return Outcome.WON
    raise ValueError(f"Unexpected letter {letter}")


def get_shapes(line: str):
    """Returns shapes from given line

    Args:
        line (str): input stream

    Returns:
        (Shape, Shape): opponent_shape, chosen_shape
    """
    opponent_letter, chosen_letter = get_letters(line)

    opponent_shape = get_opponent_shape(opponent_letter)
    chosen_shape = get_chosen_shape(chosen_letter)

    return opponent_shape, chosen_shape


def get_score_from_strategy_guide(strategy_guide):
    """Returns total score for rounds following given strategy guide

    Args:
        strategy_guide (list(str)): list of input stream lines

    Returns:
        int: total score
    """
    round_scores = []

    for line in strategy_guide:
        opponent_shape, chosen_shape = get_shapes(line)
        outcome = get_outcome(opponent_shape, chosen_shape)
        round_score = get_single_round_score(chosen_shape, outcome)
        round_scores.append(round_score)

    return get_total_score(round_scores)


def get_score_from_other_strategy_guide(strategy_guide):
    """Returns total score for rounds following given strategy guide

    Args:
        strategy_guide (list(str)): list of input stream lines

    Returns:
        int: total score
    """
    round_scores = []

    for line in strategy_guide:
        opponent_letter, outcome_letter = get_letters(line)
        opponent_shape = get_opponent_shape(opponent_letter)
        expected_outcome = get_expected_outcome(outcome_letter)
        chosen_shape = choose_shape(opponent_shape, expected_outcome)
        round_score = get_single_round_score(chosen_shape, expected_outcome)
        round_scores.append(round_score)

    return get_total_score(round_scores)


def get_strategy_guide_from_file(file_name):
    """Returns a strategy guide from input file

    Args:
        file_name (str): input file relative path

    Returns:
        list(str): list of input stream lines
    """
    with open(file_name) as file:
        strategy_guide = file.read().splitlines()
    return strategy_guide


def main(file_name):
    """Returns the score for given file

    Args:
        file_name (str): input file relative path

    Returns:
        int: total score
    """
    strategy_guide = get_strategy_guide_from_file(file_name)
    score = get_score_from_strategy_guide(strategy_guide)
    return score


def main_with_the_other_strategy(file_name):
    """Returns the score for given file with the other strategy

    Args:
        file_name (str): input file relative path

    Returns:
        int: total score
    """
    strategy_guide = get_strategy_guide_from_file(file_name)
    score = get_score_from_other_strategy_guide(strategy_guide)
    return score


class Day2TestCase(unittest.TestCase):
    def test_get_total_score(self):
        self.assertEqual(get_total_score([]), 0)
        self.assertEqual(get_total_score([1]), 1)
        self.assertEqual(get_total_score([8, 1, 6]), 15)

    def test_get_single_round_score(self):
        self.assertEqual(get_single_round_score(Shape.PAPER, Outcome.WON), 8)
        self.assertEqual(get_single_round_score(Shape.ROCK, Outcome.LOST), 1)
        self.assertEqual(get_single_round_score(Shape.SCISSORS, Outcome.DRAW), 6)

    def test_get_outcome(self):
        self.assertEqual(get_outcome(Shape.ROCK, Shape.PAPER), Outcome.WON)
        self.assertEqual(get_outcome(Shape.PAPER, Shape.ROCK), Outcome.LOST)
        self.assertEqual(get_outcome(Shape.SCISSORS, Shape.SCISSORS), Outcome.DRAW)

    def test_letters(self):
        self.assertEqual(get_letters("A Y"), ("A", "Y"))
        self.assertEqual(get_letters("B X"), ("B", "X"))
        self.assertEqual(get_letters("C Z"), ("C", "Z"))

    def test_get_shapes(self):
        self.assertEqual(get_opponent_shape("A"), Shape.ROCK)
        self.assertEqual(get_opponent_shape("B"), Shape.PAPER)
        self.assertEqual(get_opponent_shape("C"), Shape.SCISSORS)

        self.assertEqual(get_chosen_shape("X"), Shape.ROCK)
        self.assertEqual(get_chosen_shape("Y"), Shape.PAPER)
        self.assertEqual(get_chosen_shape("Z"), Shape.SCISSORS)

        self.assertEqual(get_shapes("A Y"), (Shape.ROCK, Shape.PAPER))
        self.assertEqual(get_shapes("B X"), (Shape.PAPER, Shape.ROCK))
        self.assertEqual(get_shapes("C Z"), (Shape.SCISSORS, Shape.SCISSORS))

    def test_get_score_from_strategy_guide(self):
        strategy_guide = [
            "A Y",
            "B X",
            "C Z",
        ]
        self.assertEqual(get_score_from_strategy_guide(strategy_guide), 15)

    def test_get_score_from_other_strategy_guide(self):
        strategy_guide = [
            "A Y",
            "B X",
            "C Z",
        ]
        self.assertEqual(get_score_from_other_strategy_guide(strategy_guide), 12)

    def test_get_strategy_guide_from_file(self):
        strategy_guide = get_strategy_guide_from_file(EXAMPLE_RELATIVE_PATH)
        expected_strategy_guide = [
            "A Y",
            "B X",
            "C Z",
        ]
        self.assertEqual(strategy_guide, expected_strategy_guide)

    def test_main(self):
        self.assertEqual(main(EXAMPLE_RELATIVE_PATH), 15)
        self.assertEqual(main(INPUT_RELATIVE_PATH), 15632)

    def test_main_with_the_other_strategy(self):
        self.assertEqual(main_with_the_other_strategy(EXAMPLE_RELATIVE_PATH), 12)
        self.assertEqual(main_with_the_other_strategy(INPUT_RELATIVE_PATH), 14416)


if __name__ == "__main__":
    print("### Day 2 ###")
    unittest.main()
