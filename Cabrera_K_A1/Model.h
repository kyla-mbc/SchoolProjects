// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 1 - Robber Language Translation

//Header Guards 
#ifndef MODEL_H
#define MODEL_H

//Include library to use strings in code. 
#include <string>

class Model {

    public:
        Model(); //constructor 
        ~Model(); //deconstructor 
        std::string translateSingleConsonant(char consonant); // Translates single conosonant character to its specific characterization. 
        std::string translateSingleVowel(char vowel); // Translates single vowel to its specific charactertization. 
};

//end of the header guard
#endif 

