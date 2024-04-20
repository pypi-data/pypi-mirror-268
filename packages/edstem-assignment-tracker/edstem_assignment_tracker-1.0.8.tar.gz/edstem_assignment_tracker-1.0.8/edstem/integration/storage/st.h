#include "node.h"

#ifndef ST_H
#define ST_H

// Splay Tree Class
class SplayTree{

    private:
    /*
    Private Members
    root: A pointer to the root of the splay tree
    splay: A function that performs the splay operation on a node
    findNode: A function that finds a node with a given key
    rotateRight: A function that performs a right rotation on a node
    rotateLeft: A function that performs a left rotation on a node
    deleteSplayTree: A function that deletes all nodes in the splay tree - should be called by the destructor with the root
    */

    EATNode* root;
    void splay(EATNode* node);
    EATNode* findNode(int key);
    void rotateRight(EATNode* node);
    void rotateLeft(EATNode* node);
    void deleteSplayTree(EATNode* node);
    void inorderTraversal(EATNode* node);
    EATNode* searchRecursive(EATNode* node, int key);

    public:
    /*
    Public Members
    Constructor: Initializes the root of the splay tree to nullptr
    Destructor: Deletes all nodes in the splay tree
    insert: Inserts a node with a given key and contents into the splay tree
    remove: Removes a node with a given key from the splay tree
    search: Searches for a node with a given key in the splay tree
    printSplayTree: Prints the contents of the splay tree in order
    */

    SplayTree();
    ~SplayTree();
    void insert(EATNode* node);
    void remove(int key);
    EATNode* search(int key);
    void printSplayTree();
    void add_bh_pointer(int key, void* ptr);
    void* get_bh_pointer(int key);
};

#endif // ST_H