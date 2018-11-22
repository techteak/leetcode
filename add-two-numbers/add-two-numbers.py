# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = ListNode(0)
        l3 = head
        flag = 0
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            num3 = (num1 + num2 + flag) % 10
            flag = (num1 + num2 + flag) / 10

            l3.next = ListNode(num3)
            l3 = l3.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if flag:
            l3.next = ListNode(flag)

        return head.next


import json


def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    # lines = readlines()
    # while True:
    try:
        l1 = stringToListNode('[5]')
        l2 = stringToListNode('[5]')

        ret = Solution().addTwoNumbers(l1, l2)

        out = listNodeToString(ret)
        print out
    except StopIteration:
        return


if __name__ == '__main__':
    main()