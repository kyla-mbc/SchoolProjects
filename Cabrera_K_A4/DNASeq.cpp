// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 4 - Genetic Palindromes

#include "DNASeq.h"
#include <iostream>

DNASeq::DNASeq() : sequence() {} //Constructor to initialize an empty DNA sequence from a string. 
DNASeq::~DNASeq(){} //Destructor for the DNASeq class. 

//Constructor that uses parameters to initialize a DNA Sequence if there are valid nucelotides.
DNASeq::DNASeq(const std::string& seq) : validSequence(true) {
    for (char c : seq) {
        if (vNucleotide(c)) { //check if character is a valid nucleotide. 
            sequence.addBack(c); //Append valid nucleotide to sequence. 
        } else {
            validSequence = false; //if sequence is invalid, it will be marked. 
            sequence = DblList<char>(); // Re-initialize the list to remove any invalid characters. 
            break; // Exit the loop early since the sequence is already invalid
        }
    }
}

//Generates and returns the complement of the DNA Sequence. 
DNASeq DNASeq::complement() const {
    DNASeq seqComplement; //Creates a new DNA sequence for the complement. 
    ListNode<char>* current = sequence.getFront(); //Start from the first or 'front' node. 

    //Go through each nucleotide to find and append its complement. 
    while (current != nullptr) {
        char charComplement;
        switch (current->m_data) {
            case 'A':
                charComplement = 'T';
                break;
            case 'T':
                charComplement = 'A';
                break;
            case 'C':
                charComplement = 'G';
                break;
            case 'G':
                charComplement = 'C';
                break;
        }
        seqComplement.sequence.addBack(charComplement); //add complement to a new sequence. 
        current = current->m_next; //Move to the next node. 
    }
    return seqComplement;
}

//Checks if the DNA sequence is a genetic palindrome. 
bool DNASeq::isGeneticPalindrome() const {
    DNASeq complementSequence = complement(); //Get the complement sequence. 
    ListNode<char>* originalPointer = sequence.getFront(); //Point pointer to start of the original sequence. 
    ListNode<char>* complementPointer = complementSequence.sequence.getBack(); //Point pointer to end of the complement sequence. 

    //Compare original and complement sequence from opposite ends. 
    while (originalPointer != nullptr && complementPointer != nullptr) {
        if (originalPointer->m_data != complementPointer->m_data) {
            return false; //Not a palindrome if characters do not match. 
        }
        originalPointer = originalPointer->m_next; //Move forward in original sequence. 
        complementPointer = complementPointer->m_prev; //Move backward in complement sequence.
    }
    return true; //Once all characters are matched, the sequence is a palindrome. 
}

//Returns a substring from the DNA sequence given start and end indices. 
DNASeq DNASeq::substring(int start, int end) const {
    DNASeq subSeq;// New DNASeq object to store the substring. 
    ListNode<char>* current = sequence.getFront(); //Start at the beginning of the sequence. 
    for (int i = 0; i < end && current != nullptr; ++i) {
        if (i >= start) { //Add characters within specified range to subSeq. 
            subSeq.sequence.addBack(current->m_data);
        }
        current = current->m_next; // Move to the next node. 
    }
    return subSeq;
}

//Prints the DNA sequence to the console. 
void DNASeq::printSequence() const {
    ListNode<char>* current = sequence.getFront(); //Start at the beginning of the sequence. 
    while (current != nullptr) {
        std::cout << current->m_data; //Print each nucleotide. 
        current = current->m_next; //Move to the next node. 
    }
}
//Checks if character is a valid nucleotide. 
bool DNASeq::vNucleotide(char c) const {
    return c == 'A' || c == 'C' || c == 'T' || c == 'G';
}
//Returns the size of the DNA Sequence. 
int DNASeq::getSize() const {
    return sequence.getSize();
}
//Check if the entire sequence contains only valid nucleotides. 
bool DNASeq::isValid() const {
    ListNode<char>* current = sequence.getFront(); //Start at the beginning of the sequence. 
    while (current != nullptr) {
        if (current->m_data != 'A' && current->m_data != 'C' &&
            current->m_data != 'T' && current->m_data != 'G') {
            return false; // Found an invalid character
        }
        current = current->m_next;
    }
    return validSequence; // Sequence is only valid if all characters are valid. 
}