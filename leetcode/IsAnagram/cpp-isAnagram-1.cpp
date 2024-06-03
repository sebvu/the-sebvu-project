#include <iostream>

class Solution {
public:
  bool isAnagram(std::string s, std::string t) {
    for (int i = 0; i < s.length() - 1; i++) {
      if (s[i] < s[i + 1]) {
        char temp = s[i];
        s[i] = s[i + 1];
        s[i + 1] = temp;
      }
    }
  }
};

int main() {

  Solution solution;

  std::string s = "racecar", t = "carrace";

  std::cout << solution.isAnagram(s, t) << std::endl;
  // true

  s = "jar", t = "jam";

  std::cout << solution.isAnagram(s, t) << std::endl;
  // false
}
