from typing import List

class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        # union find

        self.id = list(range(len(nums)))
        d = {}
        for i, n in enumerate(nums):
            if n in d.keys():
                continue
            d[n] = i
            if n - 1 in d.keys():
                self.union(i, d[n - 1])
            if n + 1 in d.keys():
                self.union(i, d[n + 1])
        return self.findmaxlength()

    def find(self, i: int) -> int:
        while i != self.id[i]:
            i = self.id[i]
        return i

    def union(self, i: int, j: int):
        left = self.find(i)
        right = self.find(j)
        self.id[left] = right

    def findmaxlength(self) -> int:
        self.compress()
        count = [0] * len(self.id)
        maxlength = 0
        for i, n in enumerate(self.id):
            count[n] += 1
            maxlength = max(maxlength, count[n])
        return maxlength

    def compress(self):
        for i in range(len(self.id)):
            self.id[i] = self.find(i)



def main():
    solution = Solution()
    print(solution.longestConsecutive([1, 3, 5, 2, 4]))
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))


if __name__ == "__main__":
    main()