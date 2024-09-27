#include <vector>

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  ListNode *mergeKLists(std::vector<ListNode *> &lists) {
    ListNode *mergeList = nullptr;
    for (int i = 0; i < lists.size() - 1; i++) {
			if (lists[i] == nullptr)
				continue;
		  else (if lists[i]->val < lists[i+1]->val) 
				mergeList == lists[i];
    }
    return mergeList;
  }
};
