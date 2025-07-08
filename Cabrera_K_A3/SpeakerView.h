// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 3 - Do You See What I See?



//SpeakerView class processes audience heights from an input file and computes visibility in columns. It uses MonoStack to track the visibility of each audience member.
#ifndef SPEAKER_VIEW_H
#define SPEAKER_VIEW_H

#include <iostream>
#include <fstream>
#include <string>
#include "MonoStack.h"

class SpeakerView {
public:
    SpeakerView();  // Default constructor
    ~SpeakerView(); // Destructor 
    void processFile(std::string inputFile);  // Processes input file and computes view

private:
    int rows; // Number of rows in the audience
    int cols; // Number of columns in the audience
    double** aHeight; // 2D array for audience heights

    void createView();  // Method to compute and display the results
};

#endif

