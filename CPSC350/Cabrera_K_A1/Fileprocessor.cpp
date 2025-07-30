// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 1 - Robber Language Translation

#include "Translator.h" // Include the header file for the Translator class
#include "FileProcessor.h" // Include the header file for the FileProcessor class
#include <fstream> // Include the library for file input and output operations
#include <iostream> // Include the library for input and output operations

// Default constructor for the FileProcessor class
FileProcessor::FileProcessor(){} 
// Destructor for the FileProcessor class
FileProcessor::~FileProcessor(){}

// Method to process the input file and generate the output file
void FileProcessor::processFile(const std::string inputFile, const std::string outputFile) {
    std::ifstream inFile(inputFile); //Open the input file for reading 
    std::ofstream outFile(outputFile); //Open the output file for writing

    //Checks if both of those files opened. 
    if (inFile.is_open() && outFile.is_open()) {
        Translator translator; //Create an instance of the translator class. 
        std::string line; //Create a string named line to hold each line from the input file. 

        //Initial HTML structure to the output file. 
        outFile << "<!DOCTYPE html>\n<html>\n<head>\n<title>English to Robber Translation</title>\n</head>\n<body>\n";

         // Loop to read each line from the input file and write it as a paragraph in bold
        while (std::getline(inFile, line)) {
            outFile << "<p><b>" << line << "</b><br></p>\n";
        }
        // Placeholder for additional space in the HTML file. 
        outFile << "<p><b></b><br></p>\n";

        inFile.close(); //Close the input file. 
        inFile.open(inputFile); //Reopen the input file to read again. 

        //Check if the file opened again. 
        if (inFile.is_open()) {
            // Loop to read each line again and translate it into the Robber language
            while (std::getline(inFile, line)) {
                //Translate the current line into robber language. 
                std::string rovarspraketLine = translator.translateEnglishSentence(line);
                // Write the translated line in italics in the HTML file
                outFile << "<p><i>" << rovarspraketLine << "</i><br></p>\n";
            }
            inFile.close(); //Close the input file after processing. 
        } else {
            std::cout << "Error re-opening files!" << std::endl; //Print out error message if the file does not successfully re-open.
        }
        outFile << "<p><i></i><br></p>\n</body>\n</html>\n"; //Finalize the HTML structure.
        
        //Close both files after both processes are complete. 
        inFile.close();
        outFile.close();
    } else {
        //Error message prints if files could not be opened initially. 
        std::cout << "Error opening files!" << std::endl;
    }
}
