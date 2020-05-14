from typing import List

class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxlength = 0

        while len(s) > 0:
            n = s.pop()

            i = n
            l = 1
            while i - 1 in s:
                i -= 1
                s.remove(i)
                l += 1

            i = n
            while i + 1 in s:
                i += 1
                s.remove(i)
                l += 1
            maxlength = max(l, maxlength)

        return maxlength

def main():
    solution = Solution()
    print(solution.longestConsecutive([1, 3, 5, 2, 4]))
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))


if __name__ == "__main__":
    main()