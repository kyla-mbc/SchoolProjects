// Full name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course number and section: CPSC-350-03
// Assignment: Programming Assignment 6 - Kruzkal's

#include <iostream>
#include <fstream>
#include "WGraph.h"

int main(int argc, char* argv[]) {
    // Ensure the correct number of arguments is provided
    if (argc != 2) {
        std::cout << "You did not give full command line arguments. Please run again with full command line arguments." << std::endl;
        return 1;
    }

    // Open the specified input file
    std::ifstream inputFile(argv[1]);
    if (!inputFile) {
        std::cout << "Error, unable to open file." << std::endl;
        return 1;
    }

    // Read the number of nodes (N) in the graph
    int numNodes;
    inputFile >> numNodes;

    // Validate the number of nodes
    if (numNodes <= 0) {
        std::cout << "Error, invalid number of nodes in the graph." << std::endl;
        return 1;
    }

    // Create the graph, G
    WGraph<int> G(numNodes);

    // Add vertices to the graph
    for (int i = 0; i < numNodes; ++i) {
        G.addVertex(i);
    }

    // Read adjacency matrix and add edges to the graph
    for (int i = 0; i < numNodes; ++i) {
        for (int j = 0; j < numNodes; ++j) {
            double weight;
            inputFile >> weight;

            // Add valid edges (non-zero, finite weights)
            if (weight > 0 && weight != std::numeric_limits<double>::max()) {
                G.addEdge(i, j, weight);
            }
        }
    }

    // Close the input file
    inputFile.close();

    // Compute and output the MST
    G.computeMST();

    return 0;
}
