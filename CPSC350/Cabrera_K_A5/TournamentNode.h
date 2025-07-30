/*
Full Name: Kyla Monique B. Cabrera | Manuel Pangelinan
Student ID: 2445213 | 2450241
Chapman Email: kycabrera@chapman.edu | mpangelinan@chapman.edu
Course Number & Section: CPSC-350-03
Assignment Or Exercise Number: PA5: Scare Games
*/

#ifndef TOURNAMENT_NODE_H
#define TOURNAMENT_NODE_H

template <typename T>
class TournamentTree;  // Forward declaration of TournamentTree for friend access

// Represents a node in the tournament tree.
template <typename T>
class TournamentNode {
public:
    // Constructor: Initializes a node with a competitor.
    TournamentNode(T* competitor);
    // Destructor: Frees memory for left and right child nodes.
    ~TournamentNode();

    // Getters and setters for the winner and child nodes.
    T* getWinner() const;
    void setWinner(T* winner);

    // Accessor methods for children (optional)
    TournamentNode<T>* getLeft() const;
    TournamentNode<T>* getRight() const;

private:
    T* winner; // Pointer to the winner at this node.
    TournamentNode<T>* left; // Left child node.
    TournamentNode<T>* right; // Right child node.

    // Allow TournamentTree to access private members.
    friend class TournamentTree<T>;
};

// Implementation of templated methods

template <typename T>
TournamentNode<T>::TournamentNode(T* competitor)
    : winner(competitor), left(nullptr), right(nullptr) {}

template <typename T>
TournamentNode<T>::~TournamentNode() {
    delete left;
    delete right;
}

template <typename T>
T* TournamentNode<T>::getWinner() const {
    return winner;
}

template <typename T>
void TournamentNode<T>::setWinner(T* winner) {
    this->winner = winner;
}

template <typename T>
TournamentNode<T>* TournamentNode<T>::getLeft() const {
    return left;
}

template <typename T>
TournamentNode<T>* TournamentNode<T>::getRight() const {
    return right;
}

#endif