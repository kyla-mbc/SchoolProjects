// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 2 - Not so Super Mario Bros.

#ifndef LEVEL_H
#define LEVEL_H
#include<iostream>

class Level{
    public:
        Level(); //constructor
        ~Level(); //destructor
        void setLevels(int levels); //sets number of levels
        int getLevels(); //gets number of levels
    private:
        int numLevels;
};

#endif