#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstdlib>
#include "avl.cpp"
#include "bh.cpp"
#include "st.cpp"
#include "node.cpp"
#include "node.h"
#include "avl.h"
#include "st.h"
#include "bh.h"

void clearTerminal();

int main(int argc, char* argv[]) {

    std::ifstream file("edstem/integration/edstem-data/data.txt");

    // Later we will implement the rest of the code hre

    std::string line;

    // stores the data for the current course
    std::vector<std::string> st_course_data;
    std::vector<std::string> bhavl_lesson_data;
    std::vector<int>course_ids;

    // create course key for splay tree
    int st_course_key;
    int bhavl_lesson_key;
    int test_count;
    int courseId;

    // Declare the data structures
    SplayTree* st = new SplayTree();
    BinaryHeap* bh = new BinaryHeap();
    AVLTree* avl = new AVLTree();


    while (std::getline(file, line)) {

        std::istringstream iss(line);

        std::string word;

        // check line to see if the first characters are st or bhavl
        if (line.substr(0, 2) == "st") {

            
            // check if there is new course id
            if (line.substr(0, 12) == "st_course_id") {

                // if vector is empty
                if (!st_course_data.empty()) {
                    // create a new node
                    EATNode* node = new EATNode(st_course_key, st_course_data);
                    // insert the data into the splay tree
                    st->insert(node);
                    st_course_data.clear();
                }

                // create the new course key
                st_course_key = std::stoi(line.substr(15, line.length() - 2));           
            }
        
            std::stringstream streamline(line);
            std::string word;
            std::string phrase;
            bool in_quotes = false;

            // iterate through the line - we iterate through the line to get the data in the quotes
            for (char c : line) {
                if (c == '\'') {
                    in_quotes = !in_quotes;
                    if (!in_quotes && !phrase.empty()) {
                        
                        st_course_data.push_back(phrase);

                        phrase.clear();
                    }
                } 
                // if we are not in quotes we add the character to the phrase
                else if (in_quotes) {
                    phrase += c;
                }
            }
            
        
        } 
        
        else if (line.substr(0, 5) == "bhavl") {
            // Since we can't technically determine the next line we create the remaining splay tree node here
            if (!st_course_data.empty()) {
                // create a new node
                EATNode* node = new EATNode(st_course_key, st_course_data);
                // insert the data into the splay tree
                st->insert(node);
                st_course_data.clear();
            }

            
            // check if the line starts with bhavl_course_id
            if (line.substr(0, 15) == "bhavl_course_id") {
                // Extract the course id from the line
                size_t idStartIndex = line.find(":") + 3; // Find the position of ':' and add 2 to skip it and the space after it
                size_t idEndIndex = line.find('\n') - 2; // Find the position of newline character
                std::string courseIdStr = line.substr(idStartIndex, idEndIndex - idStartIndex); // Extract the substring containing the course id
                int courseId = std::stoi(courseIdStr); // Convert the substring to an integer

                // When we encounter the first course id the course_ids vector will be empty so we add the binary heap pointer to the SplayTree
                if(course_ids.empty()) {
                    // Add a dummy value to the course_ids vector
                    course_ids.push_back(courseId);
                    bh = new BinaryHeap();
                    st->add_bh_pointer(courseId, bh);
                }


                // Check if the course id is already in the vector - if it is not we add it
                if (std::find(course_ids.begin(), course_ids.end(), courseId) == course_ids.end()) {
                    // Add the new course id to the vector
                    
                    course_ids.push_back(courseId);
                    // Create a new BinaryHeap for this course id
                    bh = new BinaryHeap();

                    // Add the BinaryHeap pointer to the SplayTree
                    st->add_bh_pointer(courseId, bh);

                }

                // add course id to the AVL tree
                EATNode* node = new EATNode(bhavl_lesson_key, bhavl_lesson_data);
                avl->insert(node);
            }


            if (line.substr(0, 15) == "bhavl_lesson_id") {

                int idStartIndex = 18;
                int idLength = line.length() - idStartIndex - 1; // Adjusting to remove the trailing quote
                /* 
                    if vector is empty
                    create a new node
                    insert the data into the splay tree
                */
                if (!bhavl_lesson_data.empty()) {
                    
                    
                    EATNode* node = new EATNode(bhavl_lesson_key, bhavl_lesson_data);
                    bh->insert(node);
                    avl->insert(node);
                    bhavl_lesson_data.clear();
                }

                // creates the new lesson key
                bhavl_lesson_key = std::stoi(line.substr(idStartIndex, idLength));
                
                }
        
                std::stringstream streamline(line);
                std::string word;
                std::string phrase;
                bool in_quotes = false;

                // iterate through the line - we iterate through the line to get the data in the quotes
                for (char c : line) {
                    if (c == '\'') {
                        in_quotes = !in_quotes;
                        if (!in_quotes && !phrase.empty()) {
                            
                            bhavl_lesson_data.push_back(phrase);

                            phrase.clear();
                        }
                        
                    } 
                    // if we are not in quotes we add the character to the phrase
                    else if (in_quotes) {
                        phrase += c;
                    }
                }
        }
    }




    // We will ask the user to decide if they want to get the data for a specific course
    int user_input;
    std::string user_splaytree_str;
    int repeat_search = 1; 
    std::string filter_data;
    do{
        // if repeat search is 2 and the system is not windows
        if (repeat_search == 2) {
            clearTerminal();
        }

        // ask if they want to see the splay tree to view the course ids
        std::cout << "Would you like to see the splay tree to view the course ids? (y or n): ";
        std::cin >> user_splaytree_str;

        if (user_splaytree_str == "y") {
            st->printSplayTree();
        } else {
            std::cout << "You have chosen not to view the splay tree." << std::endl;
        }

        // ask the user if they want to view the binary heap for a specific course or the AVL tree or if they're done

        // user data structure type
        std::string user_ds_type;

        std::cout << "Would you like to view the binary heap for a specific course, the AVL tree to view all lesson data, or are you done? (bh, avl, or done): ";
        std::cin >> user_ds_type;

        // if the user wants to view the binary heap
        if (user_ds_type == "bh") {
            // ask the user for the course id
            int user_course_id;
            std::cout << "Please enter the course id you would like to view: ";
            std::cin >> user_course_id;
            // get the binary heap pointer from the splay tree
            BinaryHeap* bh = (BinaryHeap*)st->get_bh_pointer(user_course_id);

            // we ask the user if they want to filter the data.
            std::cout << "Would you like to filter the data? (y or n): ";
            std::cin >> filter_data;
            if (filter_data == "y") {
                bh->printFilters();
                int filter;
                std::cout << "Please enter the number of the filter you would like to apply: ";
                std::cin >> filter;
                // to make sure the user enters a valid filter
                while (filter < 0 || filter > 5) {
                    std::cout << "Invalid filter. Please enter a number between 1 and 5: ";
                    std::cin >> filter;
                }
                bh->filterBinaryHeap(filter);
            } 
            
            else {
                bh->filterBinaryHeap(0);
            }
        } 
        
        else if (user_ds_type == "avl") {
            // we ask the user if they want to filter the data.
            std::cout << "Would you like to filter the data? (y or n): ";
            std::cin >> filter_data;
            // we call a function to list options for filtering
            if (filter_data == "y") {
                avl->printFilters();
                int filter;
                std::cout << "Please enter the number of the filter you would like to apply: ";
                std::cin >> filter;
                // to make sure the user enters a valid filter
                while (filter < 0 || filter > 5) {
                    std::cout << "Invalid filter. Please enter a number between 1 and 5: ";
                    std::cin >> filter;
                }
                avl->printAVLTree(filter);
            } 
            // if the user does not want to filter the data
            else {
                avl->printAVLTree(0);
            }
            std::cout << "Checking if the AVL tree is balanced..." << std::endl;
            // check if the AVL tree is balanced
            if (avl->isBalanced()) {
                std::cout << "The AVL tree is balanced." << std::endl;
            } else {
                std::cout << "The AVL tree is not balanced." << std::endl;
            }

            // Ask the user if they would like to visualize the AVL tree
            std::string visualize_avl;
            std::cout << "Would you like to visualize the AVL tree? (y or n): ";
            std::cin >> visualize_avl;
            if (visualize_avl == "y") {
                std::cout << "Visualizing the AVL tree..." << std::endl;
                // If the user has GraphViz installed on their system the AVL tree will be visualized
                try {
                    avl->visualize();
                } catch (...) {
                    std::cout << "There was an error visualizing the AVL tree." << std::endl;
                    std::cout << "Please ensure you have GraphViz installed on your system." << std::endl;
                }
            } else {
                std::cout << "You have chosen not to visualize the AVL tree." << std::endl;
            }
            
        } else {
            std::cout << "" << std::endl;
        }

        // Ask the user if they would like to continue. If they do we will clear the terminal and start back at the splay tree
        std::cout << "Would you like to continue searching? \n(1 for yes, 0 for no, 2 for yes and clear the terminal, 3 for no and clear the terminal)\nInput: ";
        std::cin >> repeat_search;
    } while (repeat_search == 1 || repeat_search == 2);

    // if the user wants to clear the terminal
    if (repeat_search == 3) {
        clearTerminal();
    }

    // clear the vectors
    course_ids.clear();

    // delete the splay tree
    delete st;
    // delete the binary heap
    delete bh;
    delete avl;

    return 0;
}


// function to clear terminal
void clearTerminal(){
        // If the system is unix/linux/mac
    try{
        system("clear");
    } 
    // If the system is windows run cls
    catch (...) {
        system("cls");
    }
}
