/*
Full Name: Kyla Monique B. Cabrera | Manuel Pangelinan
Student ID: 2445213 | 2450241
Chapman Email: kycabrera@chapman.edu | mpangelinan@chapman.edu
Course Number & Section: CPSC-350-03
Assignment Or Exercise Number: PA5: Scare Games
*/

#include "RunScareGame.h" // Includes the header file for the RunScareGame class, which manages the tournament logic.
#include <iostream> // Provides input-output stream objects for console operations.
#include <string> // Provides the std::string class for string manipulation.

int main(int argc, char* argv[]) {
    // Check if the correct number of command-line arguments is provided.
    if (argc != 4) {
        std::cout << "You did not give full command line arguments. Please run again with full command line arguments." << std::endl;
        return 1; // Exit the program with an error code.
    }

    // Extract command-line arguments.
    std::string inputFile = argv[1]; // The path to the input file containing monster data.
    std::string outputFile = argv[2]; // The path to the output DOT file for the tournament tree.
    std::string tournamentType = argv[3]; // The type of tournament: "single" or "double".

    // Determine if the tournament is double elimination based on the third argument.
    bool doubleElimination = (tournamentType == "double");

    // Create an instance of RunScareGame with the provided arguments.
    RunScareGame game(inputFile, outputFile, doubleElimination);
    // Run the tournament simulation.
    game.runTournament();

    return 0;
}