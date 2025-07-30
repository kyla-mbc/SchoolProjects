// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 2 - Not so Super Mario Bros.

#ifndef BOSS_H //Ensure the header is only used once. 
#define BOSS_H //Define BOSS_H if it's not only already defined. 

#include "GameObject.h" //Include header file for base class GameObject.

class Boss : public GameObject{
    public:
        Boss();
        ~Boss();
        char getCharacter() override; //get boss character
        int instancesOf() override; //returns the number of instances of boss on grid
    private:
        char character = 'b'; //private member variable representing the boss class. 
    
};

#endif