// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 1 - Robber Language Translation

#include "Model.h" //Include the header file for the model class. 
#include <cctype> // Include cctype for character handling functions like tolower

Model::Model() {} //Constructor for the model class. 

Model::~Model(){} //Deconstructor for the model class. 

// Method to translate a single consonant into the Robber Language format
std::string Model::translateSingleConsonant(char consonant){
    std::string consonantresult; // String to store the translated result for the consonant. 
    consonantresult += consonant; //Add the original consonant. 
    consonantresult += 'o'; // Add the character 'o' after the consonant. 
    consonantresult += tolower(consonant); //Add the lowercase version of the consonant.
    return consonantresult; //return the translated consonant. 
}

std::string Model::translateSingleVowel(char vowel){
    std::string vowelresult; //String to reutrn the translated result of the vowel. 
    vowelresult += vowel; //Vowels remain unchanged in the robber language translation. 
    return vowelresult; //Return the untranslated vowel. 
    
} 