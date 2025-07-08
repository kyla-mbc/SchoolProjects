// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 2 - Not so Super Mario Bros.

#ifndef GOOMBAS_H
#define GOOMBAS_H
#include "GameObject.h"

class Goombas: public GameObject{

    public:
        Goombas(); //Constructor
        ~Goombas(); //Destructor
        char getCharacter() override; //access character
    private:
        char character = 'g'; //goomba character represented by 'g'
};

#endif