#include "bh.h"
#include <iostream>
#include <vector>
#include <algorithm> // For std::swap

#define RESET   "\033[0m"
#define GREEN   "\033[32m"


BinaryHeap::BinaryHeap() : heapSize(0) {}

BinaryHeap::~BinaryHeap() {
    for (auto node : heap) {
        delete node;
    }
}

void BinaryHeap::resize(int newSize) {
    heap.resize(newSize);
}

void BinaryHeap::heapify(int index) {
    int left = 2 * index + 1;
    int right = 2 * index + 2;
    int smallest = index;

    if (left < heapSize && heap[left]->data.first < heap[smallest]->data.first) {
        smallest = left;
    }
    if (right < heapSize && heap[right]->data.first < heap[smallest]->data.first) {
        smallest = right;
    }

    if (smallest != index) {
        std::swap(heap[index], heap[smallest]);
        heapify(smallest);
    }
}

void BinaryHeap::insert(EATNode* node) {
    if (heapSize == heap.size()) {
        resize(heapSize + 1);
    }
    int i = heapSize++;
    heap[i] = node;

    while (i != 0 && heap[(i - 1) / 2]->data.first > heap[i]->data.first) {
        std::swap(heap[(i - 1) / 2], heap[i]);
        i = (i - 1) / 2;
    }
}

EATNode* BinaryHeap::extractMin() {
    if (heapSize <= 0)
        return nullptr;

    if (heapSize == 1) {
        heapSize--;
        return heap[0];
    }

    EATNode* root = heap[0];
    heap[0] = heap[heapSize - 1];
    heapSize--;
    heapify(0);

    return root;
}

void BinaryHeap::printBinaryHeap(int filter, int specifier, std::vector<std::string> &types) {
    for (int i = 1; i < heapSize; i++) {
        printKeyFront(i, filter, specifier, types);
        // Iterate over both column names and elements in the column
        for (size_t j = 1; j < heap[i]->data.second.first.size() - 1; j++) {
            
            if (filter == 0) {    
                checkCol(i, j);
            }
            else if (filter == 1 && types[specifier] == heap[i]->data.second.first[2]) {
                checkCol(i, j);
            }
            else if (filter == 2 && heap[i]->data.second.first[1] != "Unavailable") {
                checkCol(i, j);
            }
            else if (filter == 3 && heap[i]->data.second.first.size() > 6) {
                checkCol(i, j);
            }
            else if (filter == 4 && specifier == 1 && heap[i]->data.second.first[3] == "True") {
                checkCol(i, j);
            }
            else if (filter == 4 && specifier == 0 && heap[i]->data.second.first[3] == "False") {
                checkCol(i, j);
            }
            else if (filter == 5 && specifier == 1 && heap[i]->data.second.first[5] == "attempted") {
                checkCol(i, j);
            }
            else if (filter == 5 && specifier == 0 && heap[i]->data.second.first[5] == "unattempted") {
                checkCol(i, j);
            }
        }
        printKeyBack(i, filter, specifier, types);
        std::this_thread::sleep_for(std::chrono::milliseconds(50));

    }
}


EATNode* BinaryHeap::find(int key) {
    for (auto node : heap) {
        if (node->data.first == key) {
            return node;
        }
    }
    return nullptr;
}

// Function to return the available filters for users
void BinaryHeap::printFilters() {
    std::cout << "Available filters: " << std::endl;
    std::cout << "1: " << BLUE << "type" << RESET << std::endl;
    std::cout << "2: " << BLUE << "due_date" << RESET << std::endl;
    std::cout << "3: " << BLUE << "grade" << RESET << std::endl;
    std::cout << "4: " << BLUE << "open" << RESET << std::endl;
    std::cout << "5: " << BLUE << "attempted" << RESET << std::endl;
    return;
}

// Public function to print the contents of the AVL tree in order
void BinaryHeap::filterBinaryHeap(int filter) {
    
    // create empty vector to store types
    std::vector<std::string> types;
    int specifier = -1;

    // when the print tree is called and filter is 0 just print tree like normal
    if (filter == 0) {
        printBinaryHeap(0, specifier, types);
        std::cout << std::endl;
    }
    // when the print tree is called and filter is 1 filter by type
    else if (filter == 1) {
        // call the print all types function to have the user pick a type to filter by
        printAllTypes();
        std::cout << std::endl;
    }
    // when the print tree is called and filter is 2 filter by due_date
    else if (filter == 2) {
        // tell them we are filtering out unavailable due dates
        std::cout << "Filtering out unavailable due dates" << std::endl;
        printBinaryHeap(2, specifier, types);
        std::cout << std::endl;
    }
    // when the print tree is called and filter is 3 filter by grade
    else if (filter == 3) {
        // tell them we are going to filter out grades that are 0 or unavailable
        std::cout << "Filtering out grades with a user score of 0 or are unavailable" << std::endl;
        printBinaryHeap(3, specifier, types);
        std::cout << std::endl;
    }
    // when the print tree is called and filter is 4 filter by open
    else if (filter == 4) {
        // Ask the user if they want to filter by open or closed
        std::cout << "Would you like to filter by open or closed? (1 for open, 0 for closed): ";
        std::cin >> specifier;
        printBinaryHeap(4, specifier, types);
        std::cout << std::endl;
    }
    // when the print tree is called and filter is 5 filter by attempted
    else if (filter == 5) {
        // Ask the user if they want to filter by attempted or unattempted
        std::cout << "Would you like to filter by attempted or unattempted? (1 for attempted, 0 for unattempted): ";
        std::cin >> specifier;
        printBinaryHeap(5, specifier, types);
        std::cout << std::endl;
    }
}

// print in order help function
void BinaryHeap::checkCol(int i, int j){
    // If j is 0: print Due Date: in RED
    if (j == 1) {
        printDueDate(i, j);
    }
    // If j is 1: print Lesson Type: in RED
    else if (j == 2) {
        printLessonType(i, j);
    }
    // If j is 2: print Openable: in RED
    else if (j == 3) {
        printOpenable(i, j);
    }
    // If j is 3: print Title: in RED
    else if (j == 4) {
        printTitle(i, j);
    }
    // If j is 4: print Status: in RED
    else if (j == 5) {
        printStatus(i, j);
    } 
    // If j is 6: print User Score: in RED
    else if (j == 6) {
        printUserScore(i, j);
    }
    // If j is 7: print Potential Score: in RED
    else if (j == 7) {
        printPotentialScore(i, j);
    }

    // Print element in the column
    return;
}

// print helper functions
void BinaryHeap::printDueDate(int i, int j){
    std::cout << RED << "Due Date: " << RESET << heap[i]->data.second.first[j] << " ";
    return;
}

void BinaryHeap::printLessonType(int i, int j){
    std::cout << RED << "Lesson Type: " << RESET << heap[i]->data.second.first[j] << " ";
    return;
}

void BinaryHeap::printOpenable(int i, int j){
    std::cout << RED << "Openable: " << RESET << heap[i]->data.second.first[j] << " ";
    return;
}

void BinaryHeap::printTitle(int i, int j){
    std::cout << RED << "Title: " << RESET << heap[i]->data.second.first[j] << " ";
    return;
}

void BinaryHeap::printStatus(int i, int j){
    // just to avoid possibly printing the user's score  if the status is a stoi we need to skip
    if (heap[i]->data.second.first[j] == "unattempted" || heap[i]->data.second.first[j] == "attempted") {
        std::cout << RED << "Status: " << RESET << heap[i]->data.second.first[j] << " ";
    }
    return;
}

void BinaryHeap::printUserScore(int i, int j){
    std::cout << RED << "User Score: " << RESET << heap[i]->data.second.first[heap[i]->data.second.first.size() -3]  << " ";
    return;
}

void BinaryHeap::printPotentialScore(int i, int j){
    std::cout << RED << "Potential Score: " << RESET << heap[i]->data.second.first[heap[i]->data.second.first.size() -2]  << " ";
    return;
}

// function to print 1 of every lesson type
void BinaryHeap::printAllTypes() {
    // we are only going to print 1 of each lesson type (i.e. cpp, python, java, etc.)
    
    // call private helper function to print all types
    std::vector<std::string> types;
    int count = 0;
    printAllTypesHelper(types, count);
    int filtertype;
    // since we have all the types in the vector we can let the user pick which ones they want to filter by
    std::cout << "Please enter the number of the type you would like to filter by: ";
    std::cin >> filtertype;
    // we will now pass this into inorderTraversal to filter by the type - we will pass in 1 to filter by type
    printBinaryHeap(1, filtertype, types);
}

// helper function to print 1 of every lesson type
void BinaryHeap::printAllTypesHelper(std::vector<std::string> &types, int &count) {
    for (int i = 1; i < heapSize; i++) {
        if (heap[i]->data.first != 0) {
            for (int j = 0; j < heap[i]->data.second.first.size(); j++) {
                // make sure that j is 2 and that the type is not already in the vector
                if (j == 2 && std::find(types.begin(), types.end(), heap[i]->data.second.first[j]) == types.end()) {
                    types.push_back(heap[i]->data.second.first[j]);
                    std::cout << count << " - Type: [" << YELLOW << heap[i]->data.second.first[j] << RESET << "]" << std::endl;
                    count++;
                }
            }
        }
    }
}


void BinaryHeap::printKeyFront(int i, int filter, int specifier, std::vector<std::string> &types){
    // filtering the front of the key
    if (filter == 1 && types[specifier] == heap[i]->data.second.first[2]){
        std::cout << "Key: " << GREEN << heap[i]->data.first << RESET << " ["; 
    }  
    else if (filter == 2 && heap[i]->data.second.first[1] != "Unavailable") {
        std::cout << "Key: " << GREEN << heap[i]->data.first << RESET << " [";
    } 
    else if (filter == 3 && heap[i]->data.second.first.size() > 6) {
        std::cout << "Key: " << GREEN << heap[i]->data.first << RESET << " [";
    } 
    else if (filter == 4 && specifier == 1 && heap[i]->data.second.first[3] == "True") {
        std::cout << "Key: " << GREEN << heap[i]->data.first << RESET << " [";
    } 
    else if (filter == 4 && specifier == 0 && heap[i]->data.second.first[3] == "False") {
        std::cout << "Key: " << GREEN << heap[i]->data.first << RESET << " [";
    } 
    else if (filter == 5 && specifier == 1 && heap[i]->data.second.first[5] == "attempted") {
        std::cout << "Key: " << GREEN << heap[i]->data.first << RESET << " [";
    } 
    else if (filter == 5 && specifier == 0 && heap[i]->data.second.first[5] == "unattempted") {
        std::cout << "Key: " << GREEN << heap[i]->data.first << RESET << " [";
    } 
    // print key like normal
    else if (filter == 0) {
        std::cout << "Key: " << GREEN << heap[i]->data.first << RESET << " ["; 
    }
    return;
}


void BinaryHeap::printKeyBack(int i, int filter, int specifier, std::vector<std::string> &types){
    // filtering the front of the key
    if (filter == 1 && types[specifier] == heap[i]->data.second.first[2]){
        std::cout << "]" << std::endl << std::endl;
    }  
    else if (filter == 2 && heap[i]->data.second.first[1] != "Unavailable") {
        std::cout << "]" << std::endl << std::endl;
    } 
    else if (filter == 3 && heap[i]->data.second.first.size() > 6) {
        std::cout << "]" << std::endl << std::endl;
    } 
    else if (filter == 4 && specifier == 1 && heap[i]->data.second.first[3] == "True") {
        std::cout << "]" << std::endl << std::endl;
    } 
    else if (filter == 4 && specifier == 0 && heap[i]->data.second.first[3] == "False") {
        std::cout << "]" << std::endl << std::endl;
    } 
    else if (filter == 5 && specifier == 1 && heap[i]->data.second.first[5] == "attempted") {
        std::cout << "]" << std::endl << std::endl;
    } 
    else if (filter == 5 && specifier == 0 && heap[i]->data.second.first[5] == "unattempted") {
        std::cout << "]" << std::endl << std::endl;
    } 
    // print key like normal
    else if (filter == 0) {
        std::cout << "]" << std::endl << std::endl;
    }
    return;
}