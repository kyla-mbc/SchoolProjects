// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 1 - Robber Language Translation

//Header Guards
#ifndef FILEPROCESSOR_H
#define FILEPROCESSOR_H

// Include the string library for using std::string
#include <string>

// Declaration of the FileProcessor class
class FileProcessor {

    public:
        FileProcessor(); //Default constructor
        ~FileProcessor(); //Destructor 
        //Method to process input and output files. 
        void processFile(std::string inputFile, std::string outputFile);

};

#endif //End of the include guard