/*
Full Name: Kyla Monique B. Cabrera | Manuel Pangelinan
Student ID: 2445213 | 2450241
Chapman Email: kycabrera@chapman.edu | mpangelinan@chapman.edu
Course Number & Section: CPSC-350-03
Assignment Or Exercise Number: PA5: Scare Games
*/

#include <fstream> // Provides file handling functionality.
#include <iostream> // Provides input-output operations.
#include "TournamentNode.h" // Defines TournamentNode, used for the tournament tree structure.

// Function to save the tree as a DOT file.
// Creates a DOT representation of the tournament tree and saves it to the specified file.
template <typename T>
void saveTreeAsDot(const std::string& filename, TournamentNode<T>* rootNode) {
    // Open the file for writing; checks for successful operation.
    std::ofstream file(filename);
    if (!file.is_open()) {
        std::cout << "Failed to open file: " << filename << "\n";
        return;
    }

    // Write the DOT graph header and recursively save tree nodes.
    file << "digraph TournamentTree {\n";
    int nodeID = 0;
    saveTreeAsDotHelper(rootNode, file, nodeID);
    file << "}\n";
    file.close();
}

// Recursive helper function for DOT file generation.
// Writes nodes and edges of the tree in DOT format.
template <typename T>
void saveTreeAsDotHelper(TournamentNode<T>* node, std::ofstream& file, int& nodeID) {
    if (node == nullptr) return;

    // Assign a unique ID to the current node and write its label.
    int currentID = nodeID++;
    file << "    node" << currentID << " [label=\"" << node->getWinner()->getName()
         << " (Power: " << node->getWinner()->getScreamPowerLevel() << ")\"];\n";

    // Recursively process left and right children if they exist.
    if (node->getLeft()) {
        int leftID = nodeID;
        saveTreeAsDotHelper(node->getLeft(), file, nodeID);
        file << "    node" << currentID << " -> node" << leftID << ";\n";
    }

    if (node->getRight()) {
        int rightID = nodeID;
        saveTreeAsDotHelper(node->getRight(), file, nodeID);
        file << "    node" << currentID << " -> node" << rightID << ";\n";
    }
}