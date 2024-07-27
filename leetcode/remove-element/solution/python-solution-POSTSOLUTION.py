from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0

        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l


solution = Solution()

nums1 = [3, 2, 2, 3]
val1 = 3

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2

print(solution.removeElement(nums1, val1), end=", ")
print(nums1)
print(solution.removeElement(nums2, val2), end=" ")
print(nums2)
