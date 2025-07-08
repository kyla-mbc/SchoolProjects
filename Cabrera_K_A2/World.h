// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 2 - Not so Super Mario Bros.

#ifndef WORLD_H
#define WORLD_H

#include <stdlib.h>  // Include for standard library functions like rand()
#include <fstream>   // Include for file input/output
#include "Mario.h"   // Include the Mario class header
#include "Level.h"   // Include the Level class header

class World {
    public:
        World();  // Default constructor
        ~World();  // Destructor
        // Constructor that initializes the world with a grid, dimension, Mario object, Level object, and output file stream
        World(char*** grid, int gridDimension, Mario* H, Level* L, std::ofstream &output); 
        // Prints the current Mario world level
        void printWorld(int currLevel, std::ofstream &output); 
        // Sets the grid for future use
        void setGrid(char*** worldGrid); 
        // Sets the grid dimension for future use
        void setDimension(int gridDimension); 
        // Generates a random X coordinate within the grid
        int randomXCoord();
        // Generates a random Y coordinate within the grid
        int randomYCoord();
        
    private:
        bool endGame = false;  // Indicates whether the game has ended
        char*** worldGrid;  // 3D array representing the grid of the world
        int gridDimension;  // The size of the grid (number of rows/columns)
        char currentWorldChar;  // Character representing the current position in the world
        int currLevel = 0;  // Current level in the game
        int turnsTaken;  // Number of turns taken in the game
};

#endif
