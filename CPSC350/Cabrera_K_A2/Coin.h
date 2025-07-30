// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 2 - Not so Super Mario Bros.

#ifndef COIN_H
#define COIN_H
#include "GameObject.h" //Include the header fie for GameObject 

class Coin : public GameObject {
    public:
        Coin(); //Constructor
        ~Coin(); //Destructor
        char getCharacter() override;   
    private:
        char character = 'c'; //coin character
    
};
#endif