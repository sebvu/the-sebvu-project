from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1

        # check test case for when list is equal to 1
        if len(nums) > 1:
            # iterate through array list looking for copies of index i and its proceeding index
            # len(nums) - 1 as nums[i + 1] will result in an out of bounds error
            for i in range(len(nums) - 1):
                if nums[i] != nums[i + 1]:
                    # if nums[i] and nums[i + 1] is not a copy, replace everything in between k and i + 1 with nums[i + 1]
                    # increment k up by one, signalling a new unique value and prevent the unique values stored at the beginning of the array to be overwritten
                    for x in range(k, i + 1):
                        nums[x] = nums[i + 1]
                    k += 1
        return k


solution = Solution()

nums1 = [1, 1, 2]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

print(solution.removeDuplicates(nums1), end="")
print(",", nums1)
print(solution.removeDuplicates(nums2), end="")
print(",", nums2)
