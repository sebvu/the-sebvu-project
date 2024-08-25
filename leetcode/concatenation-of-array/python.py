from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        for i in range((len(nums))):
            nums.append(nums[i])

        return nums


solution = Solution()

nums1 = [1, 2, 1]
print(solution.getConcatenation(nums1))

nums2 = [1, 3, 2, 1]
print(solution.getConcatenation(nums2))
