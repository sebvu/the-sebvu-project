#include <iostream>
#include <vector>

class Solution {
public:
  int removeDuplicates(std::vector<int> &nums) {
    int k = 1;

    if (nums.size() > 1) {
      for (int i = 0; i < nums.size() - 1; i++) {
        if (nums[i] != nums[i + 1]) {
          for (int x = k; x < i + 1; x++)
            nums[x] = nums[i + 1];
          k++;
        }
      }
    }
    return k;
  }
};

void print(std::vector<int> nums, Solution s) {

  // #, array

  std::cout << s.removeDuplicates(nums) << ", ";

  std::cout << "[";

  // for (auto i : nums) {
  //   std::cout << i << ", ";
  // }

  for (int i = 0; i < nums.size(); i++) {
    std::cout << nums[i];
    if (i < nums.size() - 1)
      std::cout << ", ";
  }

  std::cout << "]" << std::endl;
}

int main() {
  Solution solution;

  std::vector<int> nums1 = {1, 1, 2};

  std::vector<int> nums2 = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};

  print(nums1, solution);
  print(nums2, solution);
}
