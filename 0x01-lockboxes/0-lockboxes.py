#!/usr/bin/python3
"""
Unlock boxes
"""


from collections import deque


def canUnlockAll(boxes):
    """
    Find if all boxes can be opened
    Args:
        boxes: list of list representing boxes and keys
    Returns:
        True if all boxes can be opened otherwise False
    """
    if not boxes or len(boxes) == 1:
        return True

    visited = set()
    key_check = deque([0])
    while key_check:
        box_num = key_check.popleft()
        visited.add(box_num)
        for key in boxes[box_num]:
            if key not in visited and key < len(boxes):
                key_check.append(key)
    return len(visited) == len(boxes)
