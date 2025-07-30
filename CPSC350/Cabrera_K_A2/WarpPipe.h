// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 2 - Not so Super Mario Bros.

#ifndef WARPPIPE_H
#define WARPPIPE_H

#include "GameObject.h" // Include the header file for the GameObject class

// Declaration of the WarpPipe class, which inherits from GameObject
class WarpPipe: public GameObject{
    public:
        WarpPipe(); //Constructor
        ~WarpPipe(); //Destructor

         // Override the getCharacter method from the GameObject class
        char getCharacter() override;

        // Override the instancesOf method from the GameObject class
        int instancesOf() override;
    private:
        char character = 'w'; //warp pipe character
};

#endif
