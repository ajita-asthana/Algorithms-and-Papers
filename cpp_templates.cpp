// Create a function template that returns the larget of two values of any comparable type

#include<iostream>

// Function template for finding maximum of two values
template<typename T>
T maximum(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    // Test with integers 
    std::cout << "Max of 10 and 15: " << maximum(10, 15) << std::endl;

    // Test with floating point 
    std::cout << "Max of 3.14 and 2.71?: " << maximum(3.14, 2.71) << std::endl;

    // Test with characters 
    std::cout << "Max of 'a' and 'z': " << maximum('a', 'z') << std::endl;

    // Test with strings
    std::cout << "Max of \"apple\" and \"orange\": " << maximum(std::string("apple"), std::string("orange")) << std::endl;

    return 0;

}

// Binary Tree Template: Generate a simple binary tree template class with insertion and traversal functions 
#include<iostream>
#include<memory>

template<typename T> 
class BinaryTree {
private:
  struct Node {
    T data;
    std::unique_ptr<Node> left;
    std::unique_ptr<Node> right;
    Node(const T& value) : data(value), left(nullptr), right(nullptr)
  };

  std::unique_ptr<Node> root;

  // Helper method for insertion
  void insertHelper(std::unique_ptr<Node>& node, const T& value) {
    if(!node) {
      node = std::make_unique<Node>(value);
      return;
    }

    if (value < node->data) {
      insertHelper(node->left, value);
    } else if (value > node->data) {
      insertHelper(node->right, value);
    }
    // Equal values are ignored in this implementation.
  }
  void inOrderHelper(const Node* node) const {
    if (!node) 
      return;
    inOrderHelper(node->left.get());
    std::cout << node->data << " "; 
    inOrderHelper(node->right.get());
  }
public:
  BinaryTree() : root(nullptr) {}

  // Insert value into the tree 
  void insert(const T& value) {
    insertHelper(root, value);
  }

  // Perform in-order traversal 
  void inOrderTraversal() const {
    inOrderHelper(root.get());
    std::cout << std::endl;
  }

  // Check if tree contains a value
  bool contains(const T& value) const {
    Node* current = root.get();
    while(current) {
      if (value == current->data) {
        return true;
      } else if (value < current->data) {
        current = current->left.get();
      } else {
        current = current->right.get();
      }
    }
    return false;
  }
};

int main() {
  BinaryTree<int> intTree;
  intTree.insert(5);
  intTree.insert(3);
  intTree.insert(7);
  intTree.insert(2);
  intTree.insert(3);
  intTree.insert(6);
  intTree.insert(8);

  std::cout << "Integer tree in-order traversal: " << std::endl;
  intTree.inOrderTraversal();

  std::cout << "Tree contains 4: " << (intTree.contains(4) ? "Yes" : "No" << std::endl;
  std::cout << "Tree contains 9: " << (intTree.contains(9) ? "Yes" : "No" << std::endl;

  // Create a binary tree of strings 
  BinaryTree<std::string> stringTree;
  stringTree.insert("Banana");
  stringTree.insert("Apple");
  stringTree.insert("Orange");
  stringTree.insert("Grape");
  stringTree.insert("Pear");

  std::cout << "String tree in-order traversal: ";
  stringTree.inOrderTraversal();
  return 0;
}
