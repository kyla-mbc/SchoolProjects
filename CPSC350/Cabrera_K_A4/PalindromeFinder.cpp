// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 4 - Genetic Palindromes

#include "PalindromeFinder.h"
#include <iostream>

//Constructor
PalindromeFinder::PalindromeFinder() {}

// Method to find and print all palindromic substrings of a DNA sequence.
void PalindromeFinder::findPalindromeString(const DNASeq& sequence) {
    int length = sequence.getSize(); //Get the length of the DNA sequence. 

     // Loop to vary the substring length, starting from 5.
    for (int subLength = 5; subLength < length; ++subLength) {
        // Loop through each possible starting point for a substring of current length
        for (int start = 0; start <= length - subLength; ++start) {
            // Extract a substring of specified length from the DNA sequence
            DNASeq subSequence = sequence.substring(start, start + subLength);

            // Check if the substring is a genetic palindrome
            if (subSequence.isGeneticPalindrome()) {
                std::cout << "\tSubstring ";
                subSequence.printSequence(); // Print the palindromic substring
                std::cout << " - Genetic Palindrome" << std::endl;
            }
        }
    }
}
