// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 2 - Not so Super Mario Bros.

#ifndef MUSHROOM_H
#define MUSHROOM_H

#include "GameObject.h"

class Mushroom: public GameObject{
    public:
        Mushroom(); //Constructor
        ~Mushroom(); //Destructor
        char getCharacter() override;

    private:
        char character = 'm'; //mushroom character
};

#endif