from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for x in range(2):
            for i in nums:
                ans.append(i)

        return ans


# about the same solution


solution = Solution()

nums1 = [1, 2, 1]
print(solution.getConcatenation(nums1))

nums2 = [1, 3, 2, 1]
print(solution.getConcatenation(nums2))
