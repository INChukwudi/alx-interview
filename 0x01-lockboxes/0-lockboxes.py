#!/usr/bin/python3

"""
File that contains the canUnlockAll method
"""


def canUnlockAll(boxes):
    """
    Method that determines if all the boxes can be opened

    Args:
    boxes (list) - list bearing lists called boxes

    Return:
    value (bool) - true if all boxes can be opened or false if otherwise
    """
    boxes_count = len(boxes)
    unlocked_boxes = [False] * boxes_count
    unlocked_boxes[0] = True
    investigation_keys = [0]

    while investigation_keys:
        current_box = investigation_keys.pop()

        for key in boxes[current_box]:
            if key < boxes_count and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                investigation_keys.append(key)

    return all(unlocked_boxes)
