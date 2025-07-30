/*
Full Name: Kyla Monique B. Cabrera | Manuel Pangelinan
Student ID: 2445213 | 2450241
Chapman Email: kycabrera@chapman.edu | mpangelinan@chapman.edu
Course Number & Section: CPSC-350-03
Assignment Or Exercise Number: PA5: Scare Games
*/

#ifndef TOURNAMENT_TREE_H
#define TOURNAMENT_TREE_H

#include "TournamentNode.h" // Provides the TournamentNode class used for tree structure.
#include <vector> // Provides std::vector for storing competitors.
#include <string> // Provides std::string for file name handling.
#include <fstream> // Provides file handling for saving DOT files.
#include <iostream> // Provides input-output operations.
#include "DOTFileGeneratorMethods.cpp" // Provides methods for generating DOT file representation of the tree.

// Represents a tournament tree structure for organizing and simulating competitions.
template <typename T>
class TournamentTree {
public:
    // Constructor: Initializes the tree with competitors and elimination mode (single/double).
    TournamentTree(std::vector<T*>& competitors, bool doubleElimination = false);
    // Destructor: Frees memory by deleting all nodes in the tree.
    ~TournamentTree();

    // Executes the single-elimination tournament simulation.
    void singleElimination();
    // Executes the double-elimination tournament simulation.
    void doubleElimination();
    // Saves the tree structure as a DOT file for visualization.
    void saveTreeAsDot(const std::string& filename);

private:
    TournamentNode<T>* root; // Root node of the tournament tree.
    std::vector<T*> competitors; // List of competitors participating in the tournament.
    bool isDoubleElimination; // Indicates whether the tournament uses double elimination rules.

    // Builds the tree for a single-elimination tournament.
    void buildSingleEliminationTree();
    // Builds the tree for a double-elimination tournament.
    void buildDoubleEliminationTree();
    // Advances the tournament to the next round by simulating matches.
    void advanceNext(std::vector<TournamentNode<T>*>& currentRound);
    // Simulates a match between two nodes and determines the winner.
    TournamentNode<T>* simulateMatch(TournamentNode<T>* node1, TournamentNode<T>* node2);
    // Recursively deletes all nodes in the tree starting from the given node.
    void deleteTree(TournamentNode<T>* node);
};

// Implementation of TournamentTree methods

// Constructor
// Initializes the tournament tree with a list of competitors and the elimination type.
template <typename T>
TournamentTree<T>::TournamentTree(std::vector<T*>& competitors, bool doubleElimination)
    : competitors(competitors), isDoubleElimination(doubleElimination), root(nullptr) {
    // Builds the appropriate tree type based on the elimination rule.
    if (doubleElimination) {
        buildDoubleEliminationTree();
    } else {
        buildSingleEliminationTree();
    }
}

// Destructor
// Frees all dynamically allocated nodes in the tree.
template <typename T>
TournamentTree<T>::~TournamentTree() {
    deleteTree(root);
}

// Recursively deletes all nodes in the tree.
template <typename T>
void TournamentTree<T>::deleteTree(TournamentNode<T>* node) {
    if (node != nullptr) {
        deleteTree(node->left);
        deleteTree(node->right);
        delete node;
    }
}

// Runs a single-elimination tournament by simulating matches in each round.
template <typename T>
void TournamentTree<T>::singleElimination() {
    std::vector<TournamentNode<T>*> currentRound;
    // Initialize the first round with competitors.
    for (auto* competitor : competitors) {
        currentRound.push_back(new TournamentNode<T>(competitor));
    }

    // Continue advancing rounds until only one node remains (the champion).
    while (currentRound.size() > 1) {
        advanceNext(currentRound);
    }

    root = currentRound[0]; // Set the final champion as the root node.
}

// Runs a double-elimination tournament by handling both main and losers' brackets.
template <typename T>
void TournamentTree<T>::doubleElimination() {
    buildDoubleEliminationTree(); // Builds the initial double-elimination structure.

    TournamentNode<T>* mainBracketChampion = root->left; // Main bracket champion
    TournamentNode<T>* losersBracketChampion = root->right; // Losers' bracket champion

    // If the main and losers' bracket champions are different, perform a final match
    if (losersBracketChampion->getWinner() != mainBracketChampion->getWinner()) {
        root = simulateMatch(mainBracketChampion, losersBracketChampion);
    }
}

// Saves the tournament tree structure as a DOT file.
template <typename T>
void TournamentTree<T>::saveTreeAsDot(const std::string& filename) {
    std::ofstream file(filename);
    if (!file.is_open()) {
        std::cout << "Failed to open file for DOT output: " << filename << "\n";
        return;
    }

    file << "digraph TournamentTree {\n";
    int nodeID = 0;
    saveTreeAsDotHelper(root, file, nodeID); // Calls the helper function to traverse the tree.
    file << "}\n";
    file.close();
}

// Builds the tree for a single-elimination tournament.
template <typename T>
void TournamentTree<T>::buildSingleEliminationTree() {
    std::vector<TournamentNode<T>*> currentRound;
    // Initialize the first round with all competitors.
    for (auto* competitor : competitors) {
        currentRound.push_back(new TournamentNode<T>(competitor));
    }

    // Continue advancing rounds until the champion is determined.
    while (currentRound.size() > 1) {
        advanceNext(currentRound);
    }

    root = currentRound[0]; // Set the root to the final champion.
}

// Builds the tree for a double-elimination tournament.
template <typename T>
void TournamentTree<T>::buildDoubleEliminationTree() {
    std::vector<TournamentNode<T>*> mainBracket; // Main bracket for winners
    std::vector<TournamentNode<T>*> losersBracket; // Losers bracket for eliminated competitors

    // Initialize the main bracket with all competitors
    for (auto* competitor : competitors) {
        mainBracket.push_back(new TournamentNode<T>(competitor));
    }

    // Process rounds in the main bracket, moving losers to the losers' bracket
    while (mainBracket.size() > 1) {
        std::vector<TournamentNode<T>*> nextMainRound;

        for (size_t i = 0; i < mainBracket.size(); i += 2) {
            if (i + 1 < mainBracket.size()) {
                // Simulate match between two competitors
                TournamentNode<T>* matchNode = simulateMatch(mainBracket[i], mainBracket[i + 1]);
                nextMainRound.push_back(matchNode);

                // Move the loser to the losers' bracket
                TournamentNode<T>* loserNode = (matchNode->getWinner() == mainBracket[i]->getWinner())
                                               ? mainBracket[i + 1]
                                               : mainBracket[i];
                losersBracket.push_back(loserNode);
            } else {
                // Odd competitor advances automatically
                nextMainRound.push_back(mainBracket[i]);
            }
        }
        mainBracket = nextMainRound;
    }

    // At this point, mainBracket has only one node left, which is the main bracket champion
    TournamentNode<T>* mainChampionNode = mainBracket[0];

    // Process rounds in the losers' bracket until one competitor remains
    while (losersBracket.size() > 1) {
        advanceNext(losersBracket);
    }

    // The last remaining node in the losers' bracket becomes the losers' bracket champion
    TournamentNode<T>* losersChampionNode = losersBracket[0];

    // Set up the final match between the main and losers' bracket champions
    root = new TournamentNode<T>(nullptr); // Root to store the final winner
    root->left = mainChampionNode;
    root->right = losersChampionNode;
}

// Advances the tournament by simulating matches for the current round.
template <typename T>
void TournamentTree<T>::advanceNext(std::vector<TournamentNode<T>*>& currentRound) {
    std::vector<TournamentNode<T>*> nextRound;

    // Pair competitors for matches and advance winners to the next round.
    for (size_t i = 0; i < currentRound.size(); i += 2) {
        if (i + 1 < currentRound.size()) {
            TournamentNode<T>* matchNode = simulateMatch(currentRound[i], currentRound[i + 1]);
            nextRound.push_back(matchNode);
        } else {
            nextRound.push_back(currentRound[i]);
        }
    }

    currentRound = nextRound;
}

// Simulates a match between two nodes and determines the winner.
template <typename T>
TournamentNode<T>* TournamentTree<T>::simulateMatch(TournamentNode<T>* node1, TournamentNode<T>* node2) {
    T* winner = (T::isGreater(*node1->getWinner(), *node2->getWinner())) ? node1->getWinner() : node2->getWinner();
    
    TournamentNode<T>* matchNode = new TournamentNode<T>(winner);
    matchNode->left = node1;
    matchNode->right = node2;
    matchNode->setWinner(winner);

    return matchNode;
}

#endif