#include <iostream>
#include <vector>
#include "node.h"

#ifndef BH_H
#define BH_H

// Binary Heap class
class BinaryHeap {

    private:
    /*
    Private Members:
    Heap: Array to store the nodes
    heapSize: The size of the heap
    resize: Helper function to resize the heap
    heapify: Helper function to maintain the heap property
    */
    
    std::vector<EATNode*> heap;
    int heapSize;
    void resize(int newSize);
    void heapify(int index);
    void printDueDate(int i, int j);
    void printLessonType(int i, int j);
    void printOpenable(int i, int j);
    void printTitle(int i, int j);
    void printStatus(int i, int j);
    void printUserScore(int i, int j);
    void printPotentialScore(int i, int j);
    void printAllTypesHelper(std::vector<std::string> &types, int &count);
    void printBinaryHeap(int filter, int specifier, std::vector<std::string> &types);
    void printKeyFront(int i, int filter, int specifier, std::vector<std::string> &types);
    void printKeyBack(int i, int filter, int specifier, std::vector<std::string> &types);


    public:
    /*
    Public Members:
    BinaryHeap: Constructor
    ~BinaryHeap: Destructor
    -------------------
    insert: Used to insert a new node into the heap
    find: Used to find a node with a given key
    extractMin: Used to extract the node with the minimum key
    printBinaryHeap: Used to print the contents of the heap
    */

    BinaryHeap();
    ~BinaryHeap();
    void insert(EATNode* node);
    EATNode* find(int key);
    EATNode* extractMin();
    void printBinaryHeap(int filter);
    void printFilters();
    void filterBinaryHeap(int filter);
    void checkCol(int i, int j);
    void printAllTypes();




    
};



#endif // BH_H