from typing import List


def reverseStringByToPointer(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverseStringByPythonicWay(s: List[str]) -> None:
    s.reverse()
