// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 2 - Not so Super Mario Bros.

#include "Level.h"  // Include the header file for the Level class

// Constructor for the Level class
Level::Level(){}

// Destructor for the Level class
Level::~Level(){}

// Takes an integer input and assigns it to the numLevels variable
void Level::setLevels(int levels){
    numLevels = levels;  // Set the number of levels
}

// Returns the value stored in the numLevels variable
int Level::getLevels(){
    return numLevels;  // Return the number of levels
}
