/*
Full Name: Kyla Monique B. Cabrera | Manuel Pangelinan
Student ID: 2445213 | 2450241
Chapman Email: kycabrera@chapman.edu | mpangelinan@chapman.edu
Course Number & Section: CPSC-350-03
Assignment Or Exercise Number: PA5: Scare Games
*/

#include "RunScareGame.h"
#include <fstream> // Provides file handling functionality.
#include <sstream> // Provides std::istringstream for parsing input lines.
#include <iostream> // Provides input-output operations.

// Constructor
// Initializes the game with file paths and elimination mode.
RunScareGame::RunScareGame(const std::string& inputFile, const std::string& outputFile, bool doubleElimination)
    : inputFile(inputFile), outputFile(outputFile), doubleElimination(doubleElimination) {}

// Main function to run the tournament.
void RunScareGame::runTournament() {
    loadMonsters(); // Load all competitors from the input file.

    // Create a tournament tree and execute the game.
    TournamentTree<Monster> tournament(competitors, doubleElimination);

    // Select the appropriate elimination method.
    if (doubleElimination) {
        tournament.doubleElimination();
    } else {
        tournament.singleElimination();
    }

    saveResults(tournament); // Save the tournament results to a DOT file.
}

// Loads competitors from the input file.
void RunScareGame::loadMonsters() {
    std::ifstream file(inputFile);
    if (!file.is_open()) {
        std::cout << "Error opening input file: " << inputFile << std::endl;
        return;
    }

    std::string line;
    while (std::getline(file, line)) {
        std::istringstream ss(line);
        std::string name;
        int screamPowerLevel;

        if (ss >> name >> screamPowerLevel) {
            // Validate scream power level and add a new Monster if valid.
            if (screamPowerLevel >= 0 && screamPowerLevel <= 1000) {
                competitors.push_back(new Monster(name, screamPowerLevel));
            } else {
                std::cout << "Invalid scream power level for " << name << ": " << screamPowerLevel << std::endl;
            }
        } else {
            std::cout << "Invalid line format: " << line << std::endl;
        }
    }

    file.close();
}

// Saves tournament results to the output file and frees allocated memory.
void RunScareGame::saveResults(TournamentTree<Monster>& tournament) {
    tournament.saveTreeAsDot(outputFile);

    // Free dynamically allocated memory for all Monsters.
    for (Monster* monster : competitors) {
        delete monster;
    }
    competitors.clear();
}