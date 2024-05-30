#include <iostream>
#include <unordered_set>
#include <vector>

class Solution {
public:
  bool hasDuplicate(std::vector<int> &nums) {
    std::unordered_set<int> storage;

    for (auto i : nums) {
      if (storage.count(i)) // return 1 if inside hashet, else 0.
        return true;
      storage.insert(i);
    }
    return false;
  }
};

int main() {
  Solution solution;

  std::vector<int> nums1 = {1, 2, 3, 3};

  std::vector<int> nums2 = {1, 2, 3, 4};

  std::cout << solution.hasDuplicate(nums1) << std::endl
            << solution.hasDuplicate(nums2) << std::endl;
}
