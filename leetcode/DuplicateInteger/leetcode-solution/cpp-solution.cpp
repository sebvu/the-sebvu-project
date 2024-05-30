#include <iostream>
#include <unordered_set>
#include <vector>

class Solution {
public:
  bool containsDuplicate(std::vector<int> &nums) {
    std::unordered_set<int> set;

    for (auto i : nums) {
      if (set.count(i)) // return a 1 if true, 0 if false
        return true;
      set.insert(i);
    }
    return false;
  }
};

int main() {
  Solution solution;

  std::vector<int> nums1 = {1, 2, 3, 1};

  std::vector<int> nums2 = {1, 2, 3, 4};

  std::vector<int> nums3 = {1, 1, 1, 3, 3, 4, 3, 2, 4, 2};

  std::cout << solution.containsDuplicate(nums1) << std::endl
            << solution.containsDuplicate(nums2) << std::endl
            << solution.containsDuplicate(nums3) << std::endl;
}
