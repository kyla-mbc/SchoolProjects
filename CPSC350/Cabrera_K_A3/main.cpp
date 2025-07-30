// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 3 - Do You See What I See?

#include <iostream>
#include "SpeakerView.h"

int main(int argc, char* argv[]) {

   //Check if the user provided the correct number of command-line arguments. Which is N+2 lines. 
    if (argc != 2) {
        std::cout << "Please input full command line arguments." << std::endl;
        return 1;
    } else {
        //Call processFile method of SpeakerView, passing the input file name from the command-line argument.
        SpeakerView view;
        view.processFile(argv[1]);  // Pass the input file name as an argument
    }

    return 0;
}
