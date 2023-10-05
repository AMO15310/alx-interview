#!/usr/bin/env python3
"""Check if all boxes can be unlocked"""

def canUnlockAll(boxes):
    """Function checks whether there is a key for another box in the current box"""
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
