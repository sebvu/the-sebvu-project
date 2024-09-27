#include <cmath>
#include <iostream>

int parentNode(int sequence) {
  int parent = 1, upper = 2, lower = 1;
  if (sequence == 1)
    return -1;

  while (true) {
    if (sequence <= travel && sequence > parent)
      return parent;
    parent++;
    travel += parent;
  }
}

int main() { std::cout << parentNode(6) << std::endl; }
// 6
// is 6 <= 2 and > 1 (no)
// parent is now 2
// travel is now 4
// is 6 <= 4 and 6 > 2
// parent is now 3
// travel is now 7
