from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1

        # check test case for when list is equal to 1
        if len(nums) > 1:
            # iterate through array list looking for copies of index i and its proceeding index
            # len(nums) - 1 as nums[i + 1] will result in an out of bounds error
            for i in range(len(nums) - 1):
                # NEW NOTES❗❗❗
                # Instead of replacing everything between k and i + 1, instead we are ONLY replacing the index of k.
                # k acts as a left pointer, while i acts as a right pointer. If i reaches a new unique value, it will replace
                # k pointer and increment up by one. This is a more efficient solution then the original solution
                if nums[i] != nums[i + 1]:
                    nums[k] = nums[i + 1]
                    k += 1
        return k


solution = Solution()

nums1 = [1, 1, 2]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

print(solution.removeDuplicates(nums1), end="")
print(",", nums1)
print(solution.removeDuplicates(nums2), end="")
print(",", nums2)
