#include "node.h"

#ifndef AVL_H
#define AVL_H

// AVL Tree Class
class AVLTree{
    // Private Members
    private:
    
    // root: A pointer to the root of the AVL tree
    EATNode* root;
    // search: A function that searches for a node with a given key in the AVL tree
    EATNode* search(EATNode* node, int key);
    // insert: A function that inserts a node with a given key and contents into the AVL tree
    EATNode* insert(EATNode* node, EATNode* newNode);
    // rotateRight: A function that performs a right rotation on a node
    EATNode* rotateRight(EATNode* node);
    // rotateLeft: A function that performs a left rotation on a node
    EATNode* rotateLeft(EATNode* node);
    // getHeight: A function that returns the height of a node
    int getHeight(EATNode* node);
    // getBalance: A function that returns the balance factor of a node
    int getBalance(EATNode* node);
    // inorderTraversal: A function that performs an inorder traversal of the AVL tree
    void inorderTraversal(EATNode* node, int filter, int specifier, std::vector<std::string> &types);
    // deleteAllNodes: A function that deletes all nodes in the AVL tree
    void deleteAllNodes(EATNode* node);
    // isBalanced: A function that checks if the AVL tree is balanced
    bool isBalanced(EATNode* node);
    // visualize helper function
    void visualizeHelper(EATNode* node, std::ofstream& file);

    // print functions
    void printAllTypesHelper(EATNode* node, std::vector<std::string> &types, int &count);

    void printDueDate(EATNode* node, int i);
    void printLessonType(EATNode* node, int i);
    void printOpenable(EATNode* node, int i);
    void printTitle(EATNode* node, int i);
    void printStatus(EATNode* node, int i);
    void printUserScore(EATNode* node, int i);
    void printPotentialScore(EATNode* node, int i);

    void checkCol(EATNode* node, int i);

    void printKeyFront(EATNode* node, int filter, int specifier, std::vector<std::string> &types);
    void printKeyBack(EATNode* node, int filter, int specifier, std::vector<std::string> &types);

    

    // Public Members
    public:

    // Constructor: Initializes the root of the AVL tree to nullptr
    AVLTree();
    // Destructor: Deletes all nodes in the AVL tree
    ~AVLTree();
    // search: Searches for a node with a given key in the AVL tree
    EATNode* search(int key);
    // insert: A function that inserts a node with a given key and contents into the AVL tree
    void insert(EATNode* node);


    // printAVLTree: Prints the contents of the AVL tree in order
    // we will take in an int to determine if we are filtering by a specific thing
    void printAVLTree(int filter);

    // isBalanced: A function that checks if the AVL tree is balanced
    bool isBalanced();

    // visualize: A function that visualizes the AVL tree
    void visualize();
    
    // printFilter
    void printFilters();

    // printAllTypes
    void printAllTypes();
    

};

#endif // AVL_H

