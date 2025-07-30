// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 4 - Genetic Palindromes

#ifndef PALINDROME_FINDER_H
#define PALINDROME_FINDER_H

#include "DNASeq.h" //Include DNASeq class to interact with DNA sequences.

//Class responsible for finding and handling palindromic substrings within a DNA sequence. 
class PalindromeFinder {
public:
    PalindromeFinder(); //Default Constructor
    void findPalindromeString(const DNASeq& sequence);
};

#endif
