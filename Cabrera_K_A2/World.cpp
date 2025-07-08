// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 2 - Not so Super Mario Bros.

#include "World.h"  // Include the header file for the World class

World::World() {}  // Default constructor

World::~World() {}  // Destructor

World::World(char*** grid, int gridDimension, Mario* H, Level* L, std::ofstream &outputFile) {
    setGrid(grid);  // Sets the grid for future use
    setDimension(gridDimension);  // Sets the grid dimension value for future use

    char x = 'E';  // Allows replacing/keeping certain characters on the grid; 'E' for Error
    currLevel = 0;  // Starting level

    // Random row & column
    int randRow = rand() % gridDimension; 
    int randCol = rand() % gridDimension;

    // Sets random row & column
    H->setXCoordinate(randRow); 
    H->setYCoordinate(randCol);

    // Saves the current world character
    currentWorldChar = worldGrid[currLevel][randRow][randCol];

    outputFile << "Mario is starting in position: ";
    H->currCordinates(outputFile);  // Outputs Mario's coordinates
    outputFile << std::endl;

    // Places Mario on the grid
    worldGrid[currLevel][randRow][randCol] = H->getCharacter();    
    outputFile << "===============================" << std::endl;

    while (endGame == false) {  // Loops until the game has ended
        bool won;
        printWorld(currLevel, outputFile);  // Prints the current level world

        outputFile << "Level: " << currLevel << ". ";  // Current level
        outputFile << "Mario is at position: ";
        H->currCordinates(outputFile);  // Mario's current coordinates

        // Mario's position 
        switch (currentWorldChar) {
            // Searches to see what game object Mario is interacting with
            case 'w': 
                // Warp pipe
                outputFile << "Mario found a warp pipe. ";
                currLevel++;  // Mario moves onto next level
                break;

            case 'x':
                // Nothing happens
                outputFile << "Mario visited an empty space. ";
                x = 'x';
                break;

            case 'm':
                // Mushroom
                outputFile << "Mario ate a mushroom. ";
                H->powerUp();  // Mario gains a power level
                x = 'x';
                break;

            case 'k':
                // Koopa
                won = H->fightEnemy(currentWorldChar, outputFile);  // Mario fights the enemy
                if (won) {
                    x = 'x';  // If he wins, the spot is replaced with nothing
                } else {
                    // Mario loses the fight
                    x = 'k';  // Koopa remains on the grid
                }
                if (H->getLives() == -1) {
                    // Mario has lost all lives; end the game
                    H->setWonGame(false);
                    endGame = true;
                }
                break;

            case 'g':
                // Goomba
                won = H->fightEnemy(currentWorldChar, outputFile);  // Mario fights the enemy
                if (won) {
                    x = 'x';  // If he wins, the spot is replaced with nothing
                } else {
                    // Mario loses the fight
                    x = 'g';  // Goomba remains on the grid
                }
                if (H->getLives() == -1) {
                    // Mario has lost all lives; end the game
                    H->setWonGame(false);
                    endGame = true;
                }
                break;

            case 'c':
                // Coin
                outputFile << "Mario collected a coin. ";
                H->collectCoin();  // Adds a coin
                x = 'x';  // Replaces the spot with nothing
                break;

            case 'b':
                // Boss
                endGame = H->fightBoss(outputFile);  // Mario fights the boss
                if (endGame && L->getLevels() - 1 == currLevel) {  // If Mario won and it's the last level
                    H->setWonGame(endGame);
                } else if (!endGame && L->getLevels() - 1 == currLevel) {  // If Mario lost
                    H->setWonGame(endGame);
                    endGame = true;  // Game over
                    x = 'x';
                } else if (endGame && L->getLevels() - 1 > currLevel) {  // If Mario won but it's not the last level
                    currLevel++;  // Next level
                    endGame = false;  // Game is not yet over
                    x = 'x';
                }
                break;
        }

        H->currPowerLevel(outputFile);  // Mario's current power level
        outputFile << "Mario has " << H->getLives() << " lives left. ";  // Outputs Mario's remaining lives
        outputFile << "Mario has " << H->getCoins() << " coins.";  // Outputs Mario's current coin count

        worldGrid[currLevel][H->getXCoord()][H->getYCoord()] = x;  // Replaces the grid space with 'x', 'k', or 'g'

        if (currentWorldChar == 'w') {  // If Mario encountered a warp pipe
            currentWorldChar = H->warp(randomXCoord(), randomYCoord(), grid, currLevel, outputFile);  // Mario warps
            outputFile << std::endl;
        } else {
            currentWorldChar = H->move(grid, gridDimension, currLevel, outputFile);  // Mario moves in the next direction
            outputFile << std::endl;
        }
        outputFile << "===============================" << std::endl;

        if (H->getLives() == -1) {
            H->setWonGame(false);
            endGame = true;
        }
        turnsTaken++;
    }
    H->endGame(outputFile, turnsTaken);  // End game actions
}

void World::printWorld(int currLevel, std::ofstream &output) {
    for (int r = 0; r < gridDimension; ++r) {
        for (int c = 0; c < gridDimension; ++c) {
            output << worldGrid[currLevel][r][c];  // Print each cell in the grid
        }
        output << std::endl;  // New line for each row
    }
    output << "===============================" << std::endl;
}

void World::setGrid(char*** worldGrid) {
    this->worldGrid = worldGrid;  // Set the world grid
}

void World::setDimension(int gridDimension) {
    this->gridDimension = gridDimension;  // Set the grid dimension
}

int World::randomXCoord() {
    int randRow = rand() % this->gridDimension;  // Get a random row
    return randRow;  // Return the random row
}

int World::randomYCoord() {
    int randCol = rand() % this->gridDimension;  // Get a random column
    return randCol;  // Return the random column
}
