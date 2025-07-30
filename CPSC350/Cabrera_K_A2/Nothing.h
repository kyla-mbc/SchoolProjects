// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 2 - Not so Super Mario Bros.

#ifndef NOTHING_H
#define NOTHING_H
#include "GameObject.h"

class Nothing: public GameObject{
    public:
        Nothing(); //Constructor
        ~Nothing(); //Destructor
        char getCharacter() override;

    private:
        char character = 'x'; //nothing character
};

#endif