// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 2 - Not so Super Mario Bros.

#ifndef KOOPAS_H
#define KOOPAS_H

#include "GameObject.h"

class Koopas: public GameObject{

    public:
        Koopas(); //Constructor
        ~Koopas(); //Destructor
        char getCharacter() override;
    private:
        char character = 'k'; //koopa character represented by 'k'
};

#endif