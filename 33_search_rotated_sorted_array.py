from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        pivot = self.pivot(nums)
        #print('pivot {}'.format(pivot))
        if target < nums[0] or pivot == 0:
            index = self.binarysearch(nums[pivot:], target)
            return -1 if index == -1 else pivot + self.binarysearch(nums[pivot:], target)

        return self.binarysearch(nums[:pivot], target)

    def pivot(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            #print('left {} - {}, right {} - {}, mid{} - {}'.format(left, nums[left], right, nums[right], mid, nums[mid]))
            if nums[mid] > nums[left] and nums[mid] > nums[right]:
                left = mid
            elif nums[mid] < nums[left] and nums[mid] < nums[right]:
                right = mid
            elif nums[mid] >= nums[left] and nums[mid] < nums[right]:
                return left
            else:
                return right

        if mid < left:
            return mid + 1
        if mid > right:
            return mid

    def binarysearch(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            i = (left + right) // 2
            if nums[i] < target:
                left = i + 1
            elif nums[i] > target:
                right = i - 1
            else:
                return i
        return -1


def main():
    solution = Solution()
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 0)) # 4
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 3)) # -1
    print(solution.search([4, 5, 6, 0, 1, 2, 3], 3)) # 6
    print(solution.search([0, 1], 1)) # 1
    print(solution.search([0, 1], 0)) # 0
    print(solution.search([3, 1], 3)) # 0
    print(solution.search([3, 1], 1))  # 1
    print(solution.search([216, 221, 222, 225, 228, 231, 234, 244, 245, 246,
                           249, 251, 259, 262, 264, 265, 268, 271, 276, 277,
                           278, 281, 282, 286, 289, 294, 295, 296, 298, 299,
                           0, 4, 9, 10, 13, 18, 23, 25, 26, 33,
                           34, 38, 39, 42, 43, 45, 48, 49, 51, 52,
                           53, 55, 58, 60, 61, 62, 63, 65, 66, 70, 72, 74, 78, 79, 82, 85, 89, 90, 91, 95, 104, 109, 112, 113, 117, 118, 120, 122,
     123, 126, 127, 128, 133, 134, 138, 140, 142, 144, 147, 148, 149, 152, 156, 164, 165, 168, 169, 174, 177, 185, 191,
     192, 193, 194, 195, 197, 204, 211, 215], 0))
    print(solution.search([6,7,8,1,2,3,4,5], 6))


if __name__ == "__main__":
    main()
