/*
Full Name: Kyla Monique B. Cabrera | Manuel Pangelinan
Student ID: 2445213 | 2450241
Chapman Email: kycabrera@chapman.edu | mpangelinan@chapman.edu
Course Number & Section: CPSC-350-03
Assignment Or Exercise Number: PA5: Scare Games
*/

#ifndef RUN_SCARE_GAME_H
#define RUN_SCARE_GAME_H

#include "TournamentTree.h" // Defines TournamentTree for managing the game logic.
#include "Monster.h" // Defines the Monster class used in the game.
#include <vector> // Provides std::vector for storing competitors.
#include <string> // Provides std::string for file names and data handling.

// Manages the scare game tournament.
class RunScareGame {
public:
    // Constructor: Initializes the game with input/output file paths and elimination mode.
    RunScareGame(const std::string& inputFile, const std::string& outputFile, bool doubleElimination);
    // Executes the tournament.
    void runTournament();

private:
    std::string inputFile;  // Path to the input file containing monsters' data.
    std::string outputFile; // Path to the output DOT file.
    bool doubleElimination; // Indicates if the game uses double elimination rules.
    std::vector<Monster*> competitors; // List of Monsters participating in the tournament.

    // Loads monsters from the input file.
    void loadMonsters();

    // Saves tournament results to the output file.
    void saveResults(TournamentTree<Monster>& tournament);
};

#endif