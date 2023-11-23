# Day 3
#
# Part 1:
#
# The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.
#
# The Elves have made a list of all of the items currently in each rucksack (your puzzle input),
# but they need your help finding the errors.
#
# The list of items for each rucksack is given as characters all on a single line.
#
#
# Example:
# vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw
#
# To help prioritize item rearrangement, every item type can be converted to a priority:
#
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
# In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.
#

import unittest

EXAMPLE_FILE_NAME = "2022/3/example.txt"
INPUT_FILE_NAME = "2022/3/input.txt"


class ItemType:
    # Every item type is identified by a single lowercase or uppercase letter
    # (that is, a and A refer to different types of items).
    id = ""


class Compartment:
    # All items of a given type are meant to go into exactly one of the two compartments.
    items = []


class Rucksack:
    # Each rucksack has two large compartments.
    large_compartment_1 = Compartment()
    large_compartment_2 = Compartment()

    # A given rucksack always has the same number of items in each of its two compartments,
    # so the first half of the characters represent items in the first compartment,
    # while the second half of the characters represent items in the second compartment.


def split_line(line: str):
    middle_index = int(len(line) / 2)
    first = line[0:middle_index]
    second = line[middle_index:]
    return first, second


def get_duplicate(first: str, second: str):
    duplicate_set = set(first) & set(second)
    assert len(duplicate_set) == 1
    return duplicate_set.pop()


def get_letter_priority(letter):
    value = ord(letter)
    if ord("a") <= value <= ord("z"):
        return value - ord("a") + 1
    if ord("A") <= value <= ord("Z"):
        return value - ord("A") + 27
    return ValueError


def get_rucksacks_from_file(file_name):
    with open(file_name) as file:
        rucksacks = file.read().splitlines()
    return rucksacks


def get_priority_from_file(file_name):
    rucksacks = get_rucksacks_from_file(file_name)
    sum = 0
    for line in rucksacks:
        first, second = split_line(line)
        duplicate = get_duplicate(first, second)
        sum += get_letter_priority(duplicate)
    return sum


def get_group_badge(input):
    assert len(input) == 3
    set_1 = set(input[0])
    set_2 = set(input[1])
    set_3 = set(input[2])
    badge_set = set_1 & set_2 & set_3
    assert len(badge_set) == 1
    return badge_set.pop()


def get_badge_priorities_from_file(file_name):
    rucksacks = get_rucksacks_from_file(file_name)
    sum = 0
    group_count = int(len(rucksacks) / 3)
    for group_index in range(group_count):
        group_start = group_index * 3
        group_end = (group_index + 1) * 3
        group_lines = rucksacks[group_start:group_end]
        group_badge = get_group_badge(group_lines)
        sum += get_letter_priority(group_badge)
    return sum


class Day3TestCase(unittest.TestCase):
    def test_line_length(self):
        line = "vJrwpWtwJgWrhcsFMMfFFhFp"
        self.assertEqual(len(line), 24)

    def test_split_line(self):
        line = "vJrwpWtwJgWrhcsFMMfFFhFp"
        first, second = split_line(line)
        self.assertEqual(first, "vJrwpWtwJgWr")
        self.assertEqual(second, "hcsFMMfFFhFp")

    def test_get_duplicate(self):
        first = "vJrwpWtwJgWr"
        second = "hcsFMMfFFhFp"
        duplicate = get_duplicate(first, second)
        self.assertEqual(duplicate, "p")

    def test_get_duplicate_from_line(self):
        line = "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"
        first, second = split_line(line)
        duplicate = get_duplicate(first, second)
        self.assertEqual(duplicate, "L")

    def test_input(self):
        input = {
            "p": "vJrwpWtwJgWrhcsFMMfFFhFp",
            "L": "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "P": "PmmdzqPrVvPwwTWBwg",
            "v": "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "t": "ttgJtRGJQctTZtZT",
            "s": "CrZsJsPPZsGzwwsLwLmpwMDw",
        }
        sum = 0
        for letter in input:
            first, second = split_line(input[letter])
            duplicate = get_duplicate(first, second)
            self.assertEqual(duplicate, letter)
            sum += get_letter_priority(letter)
        self.assertEqual(sum, 157)

    def test_get_letter_priority(self):
        self.assertEqual(get_letter_priority("a"), 1)
        self.assertEqual(get_letter_priority("r"), 18)
        self.assertEqual(get_letter_priority("z"), 26)
        self.assertEqual(get_letter_priority("A"), 27)
        self.assertEqual(get_letter_priority("Z"), 52)

    def test_get_rucksacks_from_file(self):
        input = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
        ]
        self.assertEqual(get_rucksacks_from_file(EXAMPLE_FILE_NAME), input)

    def test_get_priority_from_file(self):
        self.assertEqual(get_priority_from_file(EXAMPLE_FILE_NAME), 157)
        self.assertEqual(get_priority_from_file(INPUT_FILE_NAME), 7821)

    def test_get_group_badge(self):
        group_1 = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
        ]
        group_2 = [
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
        ]
        self.assertEqual(get_group_badge(group_1), "r")
        self.assertEqual(get_group_badge(group_2), "Z")

    def test_get_badge_priorities_from_file(self):
        self.assertEqual(get_badge_priorities_from_file(EXAMPLE_FILE_NAME), 70)
        self.assertEqual(get_badge_priorities_from_file(INPUT_FILE_NAME), 2752)


if __name__ == "__main__":
    unittest.main()
