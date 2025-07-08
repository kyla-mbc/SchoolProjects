// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 2 - Not so Super Mario Bros.

#include "WarpPipe.h"

WarpPipe::WarpPipe(){} //Construtor

WarpPipe::~WarpPipe(){} //Destructor

int WarpPipe::instancesOf(){
    return 1; //one instance of warp pipe
}

char WarpPipe::getCharacter() {
    return 'w'; //warp pipe character
}