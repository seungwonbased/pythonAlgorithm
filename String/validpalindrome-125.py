import collections
import re


def isPalindromeByList(s: str) -> bool:
    strs = []

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


def isPalindromeByDeque(s: str) -> bool:
    strs = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


def isPalindromeBySlicing(s: str) -> bool:
    s = s.lower()

    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]


if __name__ == '__main__':
    input_a = 'A man, a plan, a canal: Panama'
    input_b = 'race a car'

    print(isPalindromeByList(input_a))
    print(isPalindromeByList(input_b))
    print(isPalindromeByDeque(input_a))
    print(isPalindromeByDeque(input_b))
    print(isPalindromeBySlicing(input_a))
    print(isPalindromeBySlicing(input_b))