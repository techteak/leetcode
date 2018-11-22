#!/usr/bin/env python
# -*- coding=utf-8 -*-

import os
import sys


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    num_dict = {}
    for idx, num in enumerate(nums):
        left = target - num
        if left in num_dict:
            return [num_dict[left], idx]
        else:
            num_dict[num] = idx

    return []


def main():
    nums = [3, 3]
    target = 6
    print twoSum(nums, target)


if __name__ == '__main__':
    main()