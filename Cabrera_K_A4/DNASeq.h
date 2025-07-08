// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 4 - Genetic Palindromes

#ifndef DNASEQ_H
#define DNASEQ_H

#include "DblList.h"

class DNASeq {
public:
    DNASeq(); // Default constructor
    ~DNASeq(); //Destructor
    DNASeq(const std::string& seq); // Constructor to initialize from a string
    DNASeq complement() const; // Generates a complement DNASeq
    bool isGeneticPalindrome() const; // Checks if the sequence is a genetic palindrome
    DNASeq substring(int start, int end) const; // Extracts a substring as a DNASeq
    void printSequence() const; // Outputs the sequence to the console
    bool isValid() const; // Checks if sequence only contains A, C, T, G
    int getSize() const; // Returns the size of the sequence


private:
    DblList<char> sequence;
    bool validSequence;
    bool vNucleotide(char c) const; // Helper for nucleotide validation
};

#endif
