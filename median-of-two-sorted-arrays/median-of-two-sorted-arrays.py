import json


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)

        if len(nums) % 2 == 0:
            return (nums[len(nums) / 2 - 1] + nums[len(nums) / 2]) / float(2)
        else:
            return nums[len(nums) / 2]


def stringToIntegerList(input):
    return json.loads(input)


def doubleToString(input):
    if input is None:
        input = 0
    return "%.5f" % input


def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()

    try:

        nums1 = stringToIntegerList('[1, 3]')

        nums2 = stringToIntegerList('[2]')

        ret = Solution().findMedianSortedArrays(nums1, nums2)

        out = doubleToString(ret)
        print out
    except StopIteration:
        pass


if __name__ == '__main__':
    main()