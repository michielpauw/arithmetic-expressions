#!/usr/bin/python3.x

from itertools import combinations
from itertools import permutations
from itertools import product


class StreakFinder:
    def __init__(self, digits):
        self.all_targets = list(range(1, 6562))
        self.target = 1
        self.digits = digits

    def get_result(self, arithmetic):
        stack = []
        for a in arithmetic:
            if (a > 0):
                stack.append(a)
            else:
                d_1 = stack.pop()
                d_2 = stack.pop()
                if (a == -4):
                    stack.append(d_1 + d_2)
                elif (a == -3):
                    stack.append(d_1 - d_2)
                elif (a == -2):
                    stack.append(d_1 * d_2)
                else:
                    stack.append(d_1 / d_2)
        result = stack.pop()
        self.all_targets[result] = 0
        if result == self.target:
            return True

    def handle_partitions(self, operators, partitions, digits):

        for partition in partitions:
            arithmetic = []
            index_digits = 0
            index_operators = 0
            first = 1
            for s in partition:
                for i in range(0, s):
                    arithmetic.append(digits[index_digits])
                    index_digits += 1
                for k in range(0, s - first):
                    arithmetic.append(operators[index_operators])
                    index_operators += 1
                first = 0
            if self.get_result(arithmetic):
                return True

    def handle_operators(self, digits):
        operators = product(range(-4, -1), repeat=3)
        partitions = [[2, 1, 1], [2, 2], [3, 1], [4]]
        for o in operators:
            if self.handle_partitions(o, partitions, digits):
                return True

    def handle_permutations(self, perms):
        for p in perms:
            if (self.handle_operators(p)):
                return True
        return False

    def get_streak(self):
        while True:
            if not self.handle_permutations(permutations(self.digits)):
                return self.target
            while self.all_targets[self.target] == 0:
                self.target += 1


def main():
    comb = combinations(range(1, 10), 4)
    longest_streak = 0
    for c in comb:
        finder = StreakFinder(c)
        streak = finder.get_streak()
        if streak > longest_streak:
            print(c)
            print(streak)
            print()
            longest_streak = streak


if __name__ == "__main__":
    main()
