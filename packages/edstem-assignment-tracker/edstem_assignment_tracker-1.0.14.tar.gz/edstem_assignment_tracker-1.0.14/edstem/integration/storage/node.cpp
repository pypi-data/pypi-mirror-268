#include "node.h"

// O(1) - Constructor 
EATNode::EATNode(int key, std::vector<std::string> contents) {
    data = std::make_pair(key, std::make_pair(contents, nullptr));
    left = nullptr;
    right = nullptr;
    parent = nullptr;
}

// O(1) - Destructor
EATNode::~EATNode() {
    // Nothing to do here
}
