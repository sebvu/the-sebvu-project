from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)

        return False


solution = Solution()

# not a part of solution
nums1 = [1, 2, 3, 1]

nums2 = [1, 2, 3, 4]

nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

print(solution.containsDuplicate(nums1))

print(solution.containsDuplicate(nums2))

print(solution.containsDuplicate(nums3))
