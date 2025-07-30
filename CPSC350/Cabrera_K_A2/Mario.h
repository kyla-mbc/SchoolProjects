// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 2 - Not so Super Mario Bros.

#ifndef MARIO_H
#define MARIO_H

#include <iostream>  // Include the iostream library for input/output
#include <fstream>   // Include the fstream library for file input/output

class Mario {
    public:
        Mario();  // Constructor for the Mario class
        ~Mario();  // Destructor for the Mario class

        int instancesOf();  // Method to get the number of instances of Mario
        void collectCoin();  // Method for collecting coins
        void currPowerLevel(std::ofstream &output);  // Outputs Mario's current power level to a file
        char move(char*** &grid, int gridDimension, int currLevel, std::ofstream &output);  // Handles Mario's movements
        void currCordinates(std::ofstream &output);  // Outputs Mario's current coordinates to a file
        char warp(int x, int y, char*** &grid, int currLevel, std::ofstream &output);  // Warps Mario to a new level and coordinate
        bool fightEnemy(char c, std::ofstream &output);  // Handles fighting an enemy
        bool fightBoss(std::ofstream &output);  // Handles fighting a boss
        void endGame(std::ofstream &output, int turnsTaken);  // End game outro
        void powerUp();  // Method to power up Mario
        void move();  // Overloaded move method

    private:
        char character = 'H';  // Character representation of Mario
        int numLives;  // Number of lives Mario has
        int coins;  // Number of coins Mario has collected
        int powerLevel;  // Mario's current power level
        int coordinates[2] = {0, 0};  // Mario's current coordinates (x, y)
        int gridDimension;  // Grid dimension
        bool wonGame;  // Flag indicating if Mario has won the game
        int enemyDefeated;  // Number of enemies defeated

    public:
        // Helper functions
        void setLives(int lives);  // Sets the number of lives
        char getCharacter();  // Returns the character representation of Mario
        int getLives();  // Returns the number of lives
        void removeLive();  // Decreases the number of lives by one
        int getCoins();  // Returns the number of coins
        void setXCoordinate(int x);  // Sets the x-coordinate
        void setYCoordinate(int y);  // Sets the y-coordinate
        int getXCoord();  // Returns the x-coordinate
        int getYCoord();  // Returns the y-coordinate
        void setWonGame(bool wonGame);  // Sets the game won status
        bool getWonGame();  // Returns the game won status
};

#endif

