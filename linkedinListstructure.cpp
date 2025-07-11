# Define a node 

#include<iostream>

class Node {
  int data;
  Node* next;

  // Constructor
  Node(int val) {
    data = val;
    next = nullptr;
  }
};

# Define linked list class 
class LinkedList {
private:
  Node* head;

public:
  LinkedList() {
    head = nullptr;
  }

  // Insert at end
  void insert(int val) {
    Node* newNode = new Node(val);
    if(head == nullptr) {
      head = newNode;
      return;
    }

    Node* temp = head;
    while(temp->next != nullptr) {
      temp = temp->next;
    }
    temp->next = newNode;
  }
};
