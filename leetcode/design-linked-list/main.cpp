struct Node {
  int val;
  Node* next;
  Node(int val = 0, Node* next = nullptr) : val(val), next(next) {}
};

class MyLinkedList {
private:
  Node* head;

public:
    MyLinkedList() : head(nullptr) {}
    
    int get(int index) {
      if (head == nullptr) 
	  	  return -1;

      Node *curr = head;

      for (int i = 0; i < index; i++) {
        if (curr == nullptr)
          return -1;
				curr = curr->next;
      }
	  return curr->val;
    }
    
    void addAtHead(int val) {
      if (head == nullptr) {
        head = new Node(val);
			} else {
        Node *newNode = new Node(val, head);
			head = newNode;
			}
    }
    
    void addAtTail(int val) {
      if (head == nullptr) {
        head = new Node(val);
			} else {
        Node *curr = head;
			while (curr->next != nullptr) 
				curr = curr->next;
			curr->next = new Node(val);
			}
    }
    
    void addAtIndex(int index, int val) {
    }
    
    void deleteAtIndex(int index) {
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */

