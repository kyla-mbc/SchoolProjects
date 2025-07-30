// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 1 - Robber Language Translation

#ifndef TRANSLATOR_H  // Header guard to prevent multiple inclusions of the same header file
#define TRANSLATOR_H

#include <string> // Include the string library for using std::string

// Declaration of the Translator class
class Translator {
    
    public:
    Translator();  // Constructor declaration
    ~Translator(); // Destructor declaration

    // Method to translate a single English word
    std::string translateEnglishWord(std::string EnglishWord);

    // Method to translate an entire English sentence
    std::string translateEnglishSentence(std::string EnglishSentence);

};

#endif // End of the header guard
