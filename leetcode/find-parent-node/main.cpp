#include <cmath>
#include <iostream>

int parentNode(int sequence) {
  int parent = 1, travel = 0;

  for (int i = 1; i <= sequence; i++) {
    if (travel == parent) {
      travel = 0, parent++;
    }
    travel++;
  }
  return parent;
}

int parentNodeGPT(int sequence) {
  // Using the quadratic formula to find the parent index directly
  int parent = (-1 + sqrt(1 + 8 * sequence)) / 2;

  // Increment parent by 1 to get the correct parent node value
  return parent + 1;
}

int main() { std::cout << parentNodeGPT(6) << std::endl; }
