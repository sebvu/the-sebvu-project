from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()  # creation of a hashset with O(1) lookup time

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False


solution = Solution()

nums1 = [1, 2, 3, 3]

nums2 = [1, 2, 3, 4]

print(solution.hasDuplicate(nums1))

print(solution.hasDuplicate(nums2))
