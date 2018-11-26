class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = min(1, len(s))

        word = {}
        start = 0
        for idx, char in enumerate(s):
            if char in word and start < word[char] + 1:
                start = word[char] + 1
            else:
                max_len = max(max_len, idx - start + 1)

            word[char] = idx

        return max_len


def stringToString(input):
    return input[1:-1].decode('string_escape')


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            s = "aaaa"

            ret = Solution().lengthOfLongestSubstring(s)

            out = intToString(ret)
            print out
            break
        except StopIteration:
            break


if __name__ == '__main__':
    main()