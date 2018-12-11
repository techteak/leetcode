import json


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def get_max_long(s, pos):
            max_long = min(pos, len(s) - pos)
            for i in range(0, max_long):
                left = pos - i
                right = pos + i
                if s[left] != s[right]:
                    return i - 1
            return max_long

        def append_shape(s):
            shape = '#'
            new_s = shape
            for char in s:
                new_s += char
                new_s += shape

            return new_s

        def remove_shape(s):
            shape = '#'
            return s.replace(shape, '')

        new_s = append_shape(s)
        palindrome_len = 0
        palindrome = ''
        for i in range(0, len(new_s)):
            max_long = get_max_long(new_s, i)
            if max_long > palindrome_len:
                palindrome = new_s[i - max_long:i + max_long]
                palindrome_len = max_long

        return remove_shape(palindrome)


def stringToString(input):
    return input[1:-1].decode('string_escape')


def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()

    try:

        s = "ac"

        ret = Solution().longestPalindrome(s)

        out = (ret)
        print out
    except StopIteration:
        pass


if __name__ == '__main__':
    main()