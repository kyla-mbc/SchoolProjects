// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 1 - Robber Language Translation

//Include the header file for the FileProcessor class
#include "FileProcessor.h"
// Include the input-output stream library for using std::cout
#include <iostream>

//Main function that accepts command line arguments. 
int main(int argc, char* argv[]){
    if (argc != 3){ //Checks if the commands in the command line arguments is not equivalent to 3. 
        //Provides error message if 3 command line arguments are not identified. 
        std::cout << "You did not provide all required arguments. Try running again." << std::endl;
        return 1; //Exit the program indicating an error. 
    } else{ //Will run if 3 command line arguments are found. 
        std::cout << "File successfully created!\nFile Name: " << argv[0] << std::endl; //Prints successful message
        std::string inputFile = argv[1]; // Get the input file name from the command-line arguments
        std::string outputFile = argv[2]; // Get the output file name from the command-line arguments

        FileProcessor FileProcessing; //Creates an instance of the FileProcessor class. 
        FileProcessing.processFile(inputFile, outputFile);  // Call the processFile method to process the files
    }
   
    return 0; // Exit the program with a zero status indicating success
}