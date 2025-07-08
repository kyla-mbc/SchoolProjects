// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 2 - Not so Super Mario Bros.

#ifndef GRID_H
#define GRID_H

// Include the header files for various game objects and classes used in the grid
#include "Boss.h"
#include "Koopas.h"
#include "Mushroom.h"
#include "Coin.h"
#include "WarpPipe.h"
#include "Level.h"
#include "Mario.h"
#include "Goombas.h"
#include "Nothing.h"

#include <fstream>   // For file input and output operations.
#include <iostream>  // For standard input/output operations
#include <cstdlib>   // For standard library functions like random number generation

class World;  // Forward declaration of the World class

class Grid {

    public:
        Grid();  // Default constructor
        ~Grid();  // Destructor
        Grid(std::string fileName, std::string logFileName);  // Constructor with file name and log file name parameters
        void setPercentages(std::string fileName);  // Sets the percentages of all members based on the input file
        void print(Level *L, int row, int column, std::ofstream &output);  // Prints the world to the output file
        void insertCharacter(GameObject *o, int level, char*** grid);  // Inserts a character into the grid at a random position
        void randomPosition(char c, int level, char*** grid);  // Selects a random position for the character on the grid
        int getGridSize();  // Returns the grid dimension

    private:
        GameObject* k;  // Pointer to Koopas object
        GameObject* b;  // Pointer to Boss object
        GameObject* c;  // Pointer to Coin object
        GameObject* w;  // Pointer to WarpPipe object
        GameObject* m;  // Pointer to Mushroom object
        GameObject* n;  // Pointer to Nothing object (empty space)
        World* world;   // Pointer to the World object
        Level* L;       // Pointer to the Level object
        Mario* H;       // Pointer to the Mario object
        GameObject* g;  // Pointer to Goombas object

        char*** grid;   // 3D array representing the grid (level, row, and column)
        int row, column, value;  // Row, column, and value information for the grid
        std::ifstream percentageFile;  // Input file stream for reading percentage data from a file
        int gridDimension;  // Grid dimension (size of the grid)
};

#endif
