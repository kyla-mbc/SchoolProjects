// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 2 - Not so Super Mario Bros.

#include "Boss.h" //Include the header file

Boss::Boss(){} //Constructor for the Boss class

Boss::~Boss(){} //Destructor for the Boss class

int Boss::instancesOf(){
    return 1; //one instance of boss per grid
}

char Boss::getCharacter(){
    return 'b'; //boss character is represented by 'b'
}