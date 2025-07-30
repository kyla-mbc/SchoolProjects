// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 1 - Robber Language Translation

#include "Translator.h" //Include the translator header guard. 
#include "Model.h" //Inclide the Model header file which contains methods for translating vowels and consonants. 
#include <cctype> // Include cctype for character handling functions like isalpha

Translator::Translator(){} //Constructor for the Translator class. 
Translator::~Translator(){} //Deconstructor for the Translator class. 

// Method to translate a single English word
std::string Translator::translateEnglishWord(std::string EnglishWord){
    Model model; //Create an instance of the model class. 
    std:: string wordresult; //String to store the translated result of the world. 
    for (char x : EnglishWord) {
        // Check if the character is a vowel (both lowercase and uppercase)
        if (x == 'a' || x == 'e' || x == 'i' || x == 'o' || x == 'u' ||x == 'A' || x == 'E' || x == 'I' || x == 'O' || x == 'U' ){
            wordresult += model.translateSingleVowel(x);  // Translate the vowel using Model's method
        } else {
            wordresult += model.translateSingleConsonant(x); // Translate the consonant using Model's method
        }
    }
    return wordresult;  // Return the translated word
}

// Method to translate an entire English sentence
std::string Translator::translateEnglishSentence(std::string EnglishSentence){
    Model model; // Create an instance of the Model class
    std::string sentenceresults; // String to store the translated result of the sentence
    for (char x : EnglishSentence){ // Loop through each character in the input English sentence
        if (isalpha(x)){ // Check if the character is an alphabetic letter
            // Check if the character is a vowel (both lowercase and uppercase)
            if (x == 'a' || x == 'e' || x == 'i' || x == 'o' || x == 'u' ||x == 'A' || x == 'E' || x == 'I' || x == 'O' || x == 'U' ){
                sentenceresults += model.translateSingleVowel(x); // Translate the vowel using Model's method
            } else{
                sentenceresults += model.translateSingleConsonant(x);  // Translate the consonant using Model's method
            }
        }else {
            sentenceresults += x; // If the character is not alphabetic, add it unchanged
        }
    }
    return sentenceresults; // Return the translated sentence
}

