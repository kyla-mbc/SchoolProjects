// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 4 - Genetic Palindromes

#include <iostream>
#include <fstream>
#include "DNASeq.h"
#include "PalindromeFinder.h"

int main(int argc, char* argv[]) {
    //Check if sufficient command line arguments are provided. 
    if (argc < 2) {
        std::cout << "Please run again with full command line arguments." << std::endl;
        return 1;
    }

    std::ifstream inputFile(argv[1]);
    if (!inputFile) {
        std::cout << "There was an error opening file." << std::endl;
        return 1;
    }

    //Object to handle palindrome finding operations. 
    PalindromeFinder finder;
    std::string line; //Variable to store each line from the input file. 

    //Read each line from the input file. 
    while (std::getline(inputFile, line)) {
        if (line == "END") break; //Stop reading if "END" is found. 

        DNASeq sequence(line); //Create DNASeq object for the current line. 
        
        // Print the line directly from the input file to retain invalid characters
        std::cout << line;
        
        // Check if sequence is valid
        if (!sequence.isValid()) {
            std::cout << " - INVALID" << std::endl;
            continue; // Skip further processing for invalid sequences
        }

        // Proceed with palindrome checks if sequence is valid
        bool isPalindrome = sequence.isGeneticPalindrome();
        std::cout << (isPalindrome ? " - Genetic Palindrome" : " - Not a Genetic Palindrome") << std::endl;

        // Find and print palindromic substrings for valid sequences only
        finder.findPalindromeString(sequence);
    }

    inputFile.close(); //Close the input file when done. 
    return 0;
}
