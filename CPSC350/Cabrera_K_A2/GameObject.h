// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 2 - Not so Super Mario Bros.

#ifndef GAMEOBJECT_H
#define GAMEOBJECT_H //define if not already defined

class Grid;

class GameObject{

    public:
        GameObject(); //constructor
        virtual ~GameObject(); //destructor
        double getPercentage(); //Method to access the percentage value. 
        void setPercentage(int newPercentage, int gridDimension); //sets percentage and calculate grid spaces
        virtual int instancesOf(); //Calculates the instances of GameObject
        virtual char getCharacter() = 0;
    private:
        double percentage;   // Private member variable storing the percentage of the grid occupied by the GameObject
        int instances;       // Private member variable storing the number of instances of the GameObject
        char character;      // Private member variable storing the character representation of the GameObject
        int gridDimension;   // Private member variable storing the total number of grid spaces (grid dimension squared)
};

#endif