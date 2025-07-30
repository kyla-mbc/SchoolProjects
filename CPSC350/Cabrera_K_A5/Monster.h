/*
Full Name: Kyla Monique B. Cabrera | Manuel Pangelinan
Student ID: 2445213 | 2450241
Chapman Email: kycabrera@chapman.edu | mpangelinan@chapman.edu
Course Number & Section: CPSC-350-03
Assignment Or Exercise Number: PA5: Scare Games
*/

#ifndef MONSTER_H
#define MONSTER_H

#include <string> // Provides std::string for handling monster names.

// Class representing a Monster with a name and scream power level.
class Monster {
    public:
        // Constructor: Initializes a Monster object with a name and power level.
        Monster(std::string name, int screamPowerLevel);

        // Getter methods: Provide access to Monster's name and scream power level.
        std::string getName() const;
        int getScreamPowerLevel() const;

        // Static comparison functions: Define ordering and equality based on scream power level.
        static bool isLess(const Monster& a, const Monster& b);
        static bool isGreater(const Monster& a, const Monster& b);
        static bool isEqual(const Monster& a, const Monster& b);

    private:
        std::string name; // Name of the monster.
        int screamPowerLevel; // Power level of the monster's scream.
};

#endif