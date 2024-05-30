from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storage = []

        for i in nums:
            for x in storage:
                if i == x:
                    return True
            storage.append(i)
        return False


solution = Solution()

nums1 = [1, 2, 3, 3]

nums2 = [1, 2, 3, 4]

print(solution.hasDuplicate(nums1))

print(solution.hasDuplicate(nums2))
