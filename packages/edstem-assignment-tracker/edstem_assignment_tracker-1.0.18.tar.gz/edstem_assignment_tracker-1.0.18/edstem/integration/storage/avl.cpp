#include "avl.h"


// Constructor
AVLTree::AVLTree() {
    root = nullptr;
}

// Destructor
AVLTree::~AVLTree() {
    // Call a helper function to delete all nodes in the AVL tree
    deleteAllNodes(root);
}


/// Helper function to insert a node into the AVL tree
EATNode* AVLTree::insert(EATNode* root, EATNode* node) {
    // perform a normal BST insertion
    if (root == nullptr) {
        return node;
    }
    
    if (node->data.first < root->data.first) {
        root->left = insert(root->left, node);
    } else if (node->data.first > root->data.first) {
        root->right = insert(root->right, node);
    } else {
        // Duplicate keys are not allowed in AVL tree
        return root;
    }

    // update height of this ancestor node
    root->height = 1 + std::max(getHeight(root->left), getHeight(root->right));

    // get the balance factor of this ancestor node to check whether this node became unbalanced
    int balance = getBalance(root);

    // if this node becomes unbalanced, then there are 4 cases

    // Left Left Case
    if (balance > 1 && node->data.first < root->left->data.first) {
        return rotateRight(root);
    }

    // Right Right Case
    if (balance < -1 && node->data.first > root->right->data.first) {
        return rotateLeft(root);
    }

    // Left Right Case
    if (balance > 1 && node->data.first > root->left->data.first) {
        root->left = rotateLeft(root->left);
        return rotateRight(root);
    }

    // Right Left Case
    if (balance < -1 && node->data.first < root->right->data.first) {
        root->right = rotateRight(root->right);
        return rotateLeft(root);
    }

    // return the (unchanged) root pointer
    return root;
}

// Public function to insert a node into the AVL tree
void AVLTree::insert(EATNode* node) {
    root = insert(root, node);
}


// Helper function to search for a node in the AVL tree
EATNode* AVLTree::search(EATNode* node, int key) {
    // if the root is null or the key is found at the root
    if (node == nullptr || node->data.first == key) {
        return node;
    }

    // if the key is greater than the root's key
    if (node->data.first < key) {
        return search(node->right, key);
    }

    // if the key is less than the root's key
    return search(node->left, key);
}

// Helper function to perform a right rotation on a node
EATNode* AVLTree::rotateRight(EATNode* node) {
    EATNode* leftChild = node->left;
    EATNode* rightChild = leftChild->right;

    // perform rotation
    leftChild->right = node;
    node->left = rightChild;

    // update heights
    node->height = std::max(getHeight(node->left), getHeight(node->right)) + 1;
    leftChild->height = std::max(getHeight(leftChild->left), getHeight(leftChild->right)) + 1;

    // return new root
    return leftChild;
}

// Helper function to perform a left rotation on a node
EATNode* AVLTree::rotateLeft(EATNode* node) {
    EATNode* rightChild = node->right;
    EATNode* leftChild = rightChild->left;

    // perform rotation
    rightChild->left = node;
    node->right = leftChild;

    // update heights
    node->height = std::max(getHeight(node->left), getHeight(node->right)) + 1;
    rightChild->height = std::max(getHeight(rightChild->left), getHeight(rightChild->right)) + 1;

    // return new root
    return rightChild;
}

// Helper function to get the height of a node
int AVLTree::getHeight(EATNode* node) {
    if (node == nullptr) {
        return 0;
    }
    return node->height;
}

// Helper function to get the balance factor of a node
int AVLTree::getBalance(EATNode* node) {
    if (node == nullptr) {
        return 0;
    }
    return getHeight(node->left) - getHeight(node->right);
}

// Helper function to perform an inorder traversal of the AVL tree
// Helper function to perform an inorder traversal of the AVL tree
void AVLTree::inorderTraversal(EATNode* node, int filter, int specifier, std::vector<std::string> &types) {
    if (node == nullptr) {
        return;
    }
    inorderTraversal(node->left, filter, specifier, types);
    // Skip printing nodes with a key of 0
    if (node->data.first != 0) {
        printKeyFront(node, filter, specifier, types);
        for (int i = 0; i < node->data.second.first.size(); i++) {
            // Filter out the data based on the filter
            if (filter == 0) { // no filter
                checkCol(node, i);
            }
            // if the filter is 1 and the current type is equal to the specifier
            else if (filter == 1 && types[specifier] == node->data.second.first[2]) { // filter by type
                checkCol(node, i);
            }
            // if the filter is 2 and the current due date is not equal to unavailable
            else if (filter == 2 && node->data.second.first[1] != "Unavailable") { // filter by due_date
                checkCol(node, i);
            }
            // if the filter is 3 and the user's current score is not equal to 0 or the potential score is not equal to 0
            else if (filter == 3 && node->data.second.first.size() > 6) {
                checkCol(node, i);
            }
            // if the filter is 4 and the user specifies 1 or 2 we print out either true or false
            else if (filter == 4 && specifier == 1 && node->data.second.first[3] == "True") { // filter by open
                checkCol(node, i);
            }
            else if (filter == 4 && specifier == 0 && node->data.second.first[3] == "False") { // filter by open
                checkCol(node, i);
            }
            // if the filter is 5 and the user specifies 1 or 2 we print out either attempted or unattempted
            else if (filter == 5 && specifier == 1 && node->data.second.first[5] == "attempted") { // filter by attempted
                checkCol(node, i);
            }
            else if (filter == 5 && specifier == 0 && node->data.second.first[5] == "unattempted") { // filter by attempted
                checkCol(node, i);
            }

        }
        printKeyBack(node, filter, specifier, types);
        std::this_thread::sleep_for(std::chrono::milliseconds(50));
    }
    inorderTraversal(node->right, filter, specifier, types);
}

// Public function to search for a node in the AVL tree
EATNode* AVLTree::search(int key) {
    return search(root, key);
}

// Public function to print the contents of the AVL tree in order
void AVLTree::printAVLTree(int filter) {
    // we do each type of filter depending on the int passed in
    // 0 is no filter
    // filters are 1: type, 2: due_date, 3: grade, 4: open, 5: attempted.
    
    // create empty vector to store types
    std::vector<std::string> types;
    // specifier starts at -1
    int specifier = -1;

    // when the print tree is called and filter is 0 just print tree like normal
    if (filter == 0) {
        inorderTraversal(root, 0, specifier, types);
        std::cout << std::endl;
    }
    // when the print tree is called and filter is 1 filter by type
    else if (filter == 1) {
        printAllTypes();
        std::cout << std::endl;
    }
    // when the print tree is called and filter is 2 filter by due_date
    else if (filter == 2) {
        // tell them we are filtering out unavailable due dates
        std::cout << "Filtering out unavailable due dates" << std::endl;
        inorderTraversal(root, 2, specifier, types);
        std::cout << std::endl;
    }
    // when the print tree is called and filter is 3 filter by grade
    else if (filter == 3) {
        // add more things in the future here
        std::cout << "Filtering out ungraded assignments" << std::endl;
        inorderTraversal(root, 3, specifier, types);
        std::cout << std::endl;
    }
    // when the print tree is called and filter is 4 filter by open
    else if (filter == 4) {
        // Ask the user if they want to filter by open or closed
        std::cout << "Would you like to filter by open or closed? (1 for open, 0 for closed): ";
        std::cin >> specifier;
        inorderTraversal(root, 4, specifier, types);
        std::cout << std::endl;
    }
    // when the print tree is called and filter is 5 filter by attempted
    else if (filter == 5) {
        // Ask the user if they want to filter by attempted or unattempted
        std::cout << "Would you like to filter by attempted or unattempted? (1 for attempted, 0 for unattempted): ";
        std::cin >> specifier;
        inorderTraversal(root, 5, specifier, types);
        std::cout << std::endl;
    }
}

// Helper function to delete all nodes in the AVL tree
void AVLTree::deleteAllNodes(EATNode* node) {
    if (node == nullptr) {
        return;
    }
    deleteAllNodes(node->left);
    deleteAllNodes(node->right);
    delete node;
}


// Balance check function
bool AVLTree::isBalanced(EATNode* node) {
    if (node == nullptr) {
        return true;
    }
    int balance = getBalance(node);
    if (balance > 1 || balance < -1) {
        return false;
    }
    return isBalanced(node->left) && isBalanced(node->right);
}

// Public function to check if the AVL tree is balanced
bool AVLTree::isBalanced() {
    return isBalanced(root);
}

// Visualize the AVL tree
void AVLTree::visualize() {
    std::string folderPath = "edstem/integration/edstem-data/";

    std::ofstream file;
    file.open(folderPath + "avl.dot");
    file << "digraph AVL {" << std::endl;
    visualizeHelper(root, file);
    file << "}" << std::endl;
    file.close();
    system(("dot -Tpng " + folderPath + "avl.dot -o " + folderPath + "avl.png").c_str());
    system(("open " + folderPath + "avl.png").c_str());
}

// Helper function to visualize the AVL tree
void AVLTree::visualizeHelper(EATNode* node, std::ofstream& file) {
    if (node == nullptr || node->data.first == 0) {
        return;
    }
    if (node->left != nullptr && node->left->data.first != 0) {
        file << node->data.first << " -> " << node->left->data.first << ";" << std::endl;
    }
    if (node->right != nullptr && node->right->data.first != 0) {
        file << node->data.first << " -> " << node->right->data.first << ";" << std::endl;
    }
    visualizeHelper(node->left, file);
    visualizeHelper(node->right, file);
}

// Function to return the available filters for users
void AVLTree::printFilters() {
    std::cout << "Available filters: " << std::endl;
    std::cout << "1: " << BLUE << "type" << RESET << std::endl;
    std::cout << "2: " << BLUE << "due_date" << RESET << std::endl;
    std::cout << "3: " << BLUE << "grade" << RESET << std::endl;
    std::cout << "4: " << BLUE << "open" << RESET << std::endl;
    std::cout << "5: " << BLUE << "attempted" << RESET << std::endl;
    return;
}

// function to print 1 of every lesson type
void AVLTree::printAllTypes() {
    // we are only going to print 1 of each lesson type (i.e. cpp, python, java, etc.)
    
    // call private helper function to print all types
    std::vector<std::string> types;
    int count = 0;
    printAllTypesHelper(root, types, count);
    int filtertype;
    // since we have all the types in the vector we can let the user pick which ones they want to filter by
    std::cout << "Please enter the number of the type you would like to filter by: ";
    std::cin >> filtertype;
    // we will now pass this into inorderTraversal to filter by the type - we will pass in 1 to filter by type
    inorderTraversal(root, 1, filtertype, types);
}

// helper function to print 1 of every lesson type
void AVLTree::printAllTypesHelper(EATNode* node, std::vector<std::string> &types, int &count) {
    if (node == nullptr) {
        return;
    }
    printAllTypesHelper(node->left, types, count);
    // Skip printing nodes with a key of 0
    if (node->data.first != 0) {
        for (int i = 0; i < node->data.second.first.size(); i++) {
            // make sure that i is 2 and that the type is not already in the vector
            if (i == 2 && std::find(types.begin(), types.end(), node->data.second.first[i]) == types.end()) {
                types.push_back(node->data.second.first[i]);
                std::cout << count << " - Type: [" << YELLOW << node->data.second.first[i]<< RESET << "]" << std::endl;
                count++;
            }
        }
        // std::cout << std::endl;
    }
    printAllTypesHelper(node->right, types, count);
}

// print helper functions
void AVLTree::printDueDate(EATNode* node, int i){
    std::cout << RED << "Due Date: " << RESET << node->data.second.first[i] << " ";
    return;
}

void AVLTree::printLessonType(EATNode* node, int i){
    std::cout << RED << "Lesson Type: " << RESET << node->data.second.first[i] << " ";
    return;
}

void AVLTree::printOpenable(EATNode* node, int i){
    std::cout << RED << "Openable: " << RESET << node->data.second.first[i] << " ";
    return;
}

void AVLTree::printTitle(EATNode* node, int i){
    std::cout << RED << "Title: " << RESET << node->data.second.first[i] << " ";
    return;
}

void AVLTree::printStatus(EATNode* node, int i) {
    if (node->data.second.first[i] == "attempted") {
        std::cout << RED << "Status: " << RESET << node->data.second.first[i] << " ";
    } 
    else if (node->data.second.first[i] == "unattempted") {
        std::cout << RED << "Status: " << RESET << node->data.second.first[i] << " ";
    }
    return;
}

void AVLTree::printUserScore(EATNode* node, int i){
    std::cout << RED << "User Score: " << RESET << node->data.second.first[i] << " ";
    return;
}

void AVLTree::printPotentialScore(EATNode* node, int i){
    std::cout << RED << "Potential Score: " << RESET << node->data.second.first[i] << " ";
    return;
}

// print in order help function
void AVLTree::checkCol(EATNode* node, int i){
        if (i == 1) {
        printDueDate(node, i);
    }
    else if (i == 2) {
        printLessonType(node, i);
    }
    else if (i == 3) {
        printOpenable(node, i);
    }
    else if (i == 4) {
        printTitle(node, i);
    }
    else if (i == 5) {
        printStatus(node, i);
    } 
    else if (i == 6) {
        printUserScore(node, i);
    }
    else if (i == 7) {
        printPotentialScore(node, i);
    }
    return;
}

void AVLTree::printKeyFront(EATNode* node, int filter, int specifier, std::vector<std::string> &types){

    // if the condition is true then we can print, otherwise we will return nothing
    if (filter == 1 && types[specifier] == node->data.second.first[2]){
        std::cout << "Key: " << GREEN << node->data.first << RESET << " ["; 
    }  
    else if (filter == 2 && node->data.second.first[1] != "Unavailable") {
        std::cout << "Key: " << GREEN << node->data.first << RESET << " [";
    } 
    else if (filter == 3 && node->data.second.first.size() > 6) {
        std::cout << "Key: " << GREEN << node->data.first << RESET << " [";
    } 
    else if (filter == 4 && specifier == 1 && node->data.second.first[3] == "True") {
        std::cout << "Key: " << GREEN << node->data.first << RESET << " [";
    } 
    else if (filter == 4 && specifier == 0 && node->data.second.first[3] == "False") {
        std::cout << "Key: " << GREEN << node->data.first << RESET << " [";
    } 
    else if (filter == 5 && specifier == 1 && node->data.second.first[5] == "attempted") {
        std::cout << "Key: " << GREEN << node->data.first << RESET << " [";
    } 
    else if (filter == 5 && specifier == 0 && node->data.second.first[5] == "unattempted") {
        std::cout << "Key: " << GREEN << node->data.first << RESET << " [";
    } 
    // print key like normal
    else if (filter == 0) {
        std::cout << "Key: " << GREEN << node->data.first << RESET << " ["; 
    }
    return;
}

void AVLTree::printKeyBack(EATNode* node, int filter, int specifier, std::vector<std::string> &types){

    // if the condition is true then we can print, otherwise we will return nothing
    if (filter == 1 && types[specifier] == node->data.second.first[2]){
        std::cout << "]" << std::endl << std::endl;
    } 
    else if (filter == 2 && node->data.second.first[1] != "Unavailable") {
        std::cout << "]" << std::endl << std::endl;
    } 
    else if (filter == 3 && node->data.second.first.size() > 6) {
        std::cout << "]" << std::endl << std::endl;
    } 
    else if (filter == 4 && specifier == 1 && node->data.second.first[3] == "True") {
        std::cout << "]" << std::endl << std::endl;
    } 
    else if (filter == 4 && specifier == 0 && node->data.second.first[3] == "False") {
        std::cout << "]" << std::endl << std::endl;
    } 
    else if (filter == 5 && specifier == 1 && node->data.second.first[5] == "attempted") {
        std::cout << "]" << std::endl << std::endl;
    } 
    else if (filter == 5 && specifier == 0 && node->data.second.first[5] == "unattempted") {
        std::cout << "]" << std::endl << std::endl;
    } 
    // print key like normal
    else if (filter == 0) {
        std::cout << "]" << std::endl << std::endl;
    }
    return;
}