struct Node {
  int val;
  Node *next;
  Node(int val = 0, Node *next = nullptr) : val(val), next(next) {}
};

class MyLinkedList {
private:
  Node *head;

public:
  MyLinkedList() { head = nullptr; }

  int get(int index) {
    Node *curr = head;

    for (int i = 0; i < index; i++) {
      if (!curr)
        return -1;
      curr = curr->next;
    }
    return curr->val;
  }

  void addAtHead(int val) {
    if (!head) {
      head = new Node(val);
    }
    Node *newNode = new Node(val);
    newNode->next = head;
    head = newNode;
  }

  void addAtTail(int val) {
    if (!head) {
      head = new Node(val);
      return;
    }
    Node *curr = head;
    while (curr->next != nullptr)
      curr = curr->next;
    curr->next = new Node(val);
  }

  void addAtIndex(int index, int val) {
    Node *curr = head;

    for (int i = 0; i < index; i++) {
      if (curr == nullptr) {
        return;
      } else if (curr->next == nullptr and i + 1 == index) {
        head = new Node(val);
        return;
      }
      curr = curr->next;
    }

    if (curr == head) {
      Node *newNode = new Node(val);
      newNode->next = head;
      head = newNode;
    } else {
      Node *tmp = curr->next;
      curr->next = new Node(val);
      curr->next->next = tmp;
    }
    return;
  }

  void deleteAtIndex(int index) {
    Node *curr = head;

    for (int i = 0; i < index; i++) {
      if (curr == nullptr) {
        return;
      }
      curr = curr->next;
    }
  }
};

/**ur
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
