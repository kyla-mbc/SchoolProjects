// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 2 - Not so Super Mario Bros.

#include "Grid.h"
#include "World.h"
#include <cstdlib>  // Include for rand() and srand()
#include <ctime>    // Include for time()
#include <iostream> // Include for std::cerr
#include <string>   // Include for std::string
#include <fstream>  // Include for std::ofstream

Grid::Grid() {}

Grid::~Grid() {
    // Deletes the grid(world) and all members
    for (int l = 0; l < L->getLevels(); ++l) {
        for (int r = 0; r < row; ++r) {
            delete[] grid[l][r];
        }
        delete[] grid[l];
    }

    delete[] grid;

    delete k;
    delete b;
    delete c;
    delete w;
    delete m;
    delete n;
    delete L;
    delete H;
    delete g;
}

Grid::Grid(std::string fileName, std::string logFileName) {
    // Initialize all members
    k = new Koopas(); // Koopa
    b = new Boss();   // Boss
    c = new Coin();   // Coins
    w = new WarpPipe(); // Warp
    m = new Mushroom(); // Mushroom
    n = new Nothing();  // Nothing
    L = new Level();    // Level
    H = new Mario();    // Mario
    g = new Goombas();  // Goomba

    // File for Mario output file
    std::ofstream outputFile;
    outputFile.open(logFileName);

    // Resets random
    srand(static_cast<unsigned int>(time(nullptr)));

    // Sets the percentages of all characters, Mario's lives, grid dimension and number of levels.
    setPercentages(fileName);

    // Populates the grid with x's
    grid = new char**[L->getLevels()];
    for(int l = 0; l < L->getLevels(); ++l) {
        grid[l] = new char*[row];

        for(int r = 0; r < row; ++r) {
            grid[l][r] = new char[column];

            for(int c = 0; c < column; ++c) {
                grid[l][r][c] = 'x';
            }
        }
    }
    // Inserts all the characters into the grid
    for(int l = 0; l < L->getLevels(); ++l) {
        insertCharacter(n, l, grid);
        insertCharacter(k, l, grid);
        insertCharacter(c, l, grid);
        insertCharacter(m, l, grid);
        insertCharacter(g, l, grid);
        insertCharacter(b, l, grid);

        // Checks that it is not the last level to insert a warp
        if(L->getLevels() - 1 != l)
            insertCharacter(w, l, grid);
    }
    // Prints all the worlds
    print(L, row, column, outputFile);

    // Starts the game/world
    world = new World(grid, row, H, L, outputFile);

    // Closing file
    outputFile.close();

    // Deallocating the files.
    delete world;
    delete[] grid;
}

void Grid::setPercentages(std::string fileName) {
    std::string fileString; // Allows code to read the contents of the file.
    int set = -1; // Sets all the values for percentages, lives, levels and dimensions.

    percentageFile.open(fileName); // Opens the file
    if (percentageFile.fail()) { // If file fails to open, error is thrown
        std::cerr << "File does not exist." << std::endl;
    } else {
        while (percentageFile) { // While there is contents within the file
            set++; // Increases to ensure all values are set
            percentageFile >> fileString; // Reads the file
            value = std::stoi(fileString); // Converts the string to an int value

            switch(set) {
                case 0: 
                    L->setLevels(value); // Sets number of levels
                    break;
                case 1:
                    row = value; // Sets row value
                    column = row; // Sets column value
                    break;
                case 2:
                    H->setLives(value); // Sets Mario's lives
                    break;
                case 3:
                    c->setPercentage(value, row); // Sets percentage of coins
                    break;
                case 4:
                    n->setPercentage(value, row); // Sets percentage of nothing
                    break;
                case 5:
                    g->setPercentage(value, row); // Sets percentage of goombas
                    break;
                case 6:
                    k->setPercentage(value, row); // Sets percentage of koopas
                    break;
                case 7: 
                    m->setPercentage(value, row); // Sets percentage of mushrooms
                    break;
            }
        }
    }
}

int Grid::getGridSize() {
    return row * column; // Grid dimension 
}

void Grid::randomPosition(char c, int level, char*** grid) {
    int randRow, randCol;

    // Looks for a random position within the grid
    do {
        randRow = rand() % row;
        randCol = rand() % column;
    } while(grid[level][randRow][randCol] != 'x'); // Ensures that the space selected is empty 

    grid[level][randRow][randCol] = c; // Sets the character to the selected index of the grid
}

void Grid::insertCharacter(GameObject* o, int level, char*** grid) {
    int instanceOfCharacter = o->instancesOf(); // Gets the instances of the object based on percentage and grid dimension

    while(instanceOfCharacter > 0) { 
        randomPosition(o->getCharacter(), level, grid); // Places the character in a random position until there are no instances left
        --instanceOfCharacter;
    }
}

void Grid::print(Level *L, int row, int column, std::ofstream &output) {
    // Prints the world/grid
    for(int l = 0; l < L->getLevels(); ++l) {
        for(int r = 0; r < row; ++r) {
            for(int c = 0; c < column; ++c) {
                output << grid[l][r][c]; 
            }
            output << std::endl; // Use std::endl to end the line
        }
        output << "===============================" << std::endl; // Use std::endl for clarity
    }
}
