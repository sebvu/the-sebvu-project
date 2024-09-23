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
    ListNode *mergedList = nullptr, *mergeList = nullptr;

    for (int i = 0; i < lists.size() - 1; i++) {
      if (lists[i] == nullptr)
        continue;
      else if (lists[i]->val < lists[i + 1]->val)
        mergeList = lists[i];
    }

    for (int i = 0; i < lists.size(); i++) {
      if (lists[i] == mergeList)
        continue;
      ListNode *indexCurr = lists[i], *mergeCurr = mergeList;

      while (mergeCurr->next && indexCurr) {
        while (mergeCurr->next && indexCurr->val > mergeCurr->next->val)
          mergeCurr = mergeCurr->next;
        ListNode *newNode = new ListNode(indexCurr->val);
        newNode->next = mergeCurr->next;
        mergeCurr->next = newNode;
        indexCurr = indexCurr->next;
      }
      if (indexCurr) {
        while (indexCurr) {
          mergeCurr->next = new ListNode(indexCurr->val);
          indexCurr = indexCurr->next;
          mergeCurr = mergeCurr->next;
        }
      }
    }
    return mergedList;
  }
};
