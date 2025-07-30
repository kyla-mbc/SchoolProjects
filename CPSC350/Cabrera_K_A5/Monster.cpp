/*
Full Name: Kyla Monique B. Cabrera | Manuel Pangelinan
Student ID: 2445213 | 2450241
Chapman Email: kycabrera@chapman.edu | mpangelinan@chapman.edu
Course Number & Section: CPSC-350-03
Assignment Or Exercise Number: PA5: Scare Games
*/

#include "Monster.h"

// Constructor
// Initializes a Monster with a name and scream power level.
Monster::Monster(std::string name, int screamPowerLevel)
    : name(name), screamPowerLevel(screamPowerLevel) {}

// Getters
// Returns the monster's name.
std::string Monster::getName() const {
    return name;
}

// Returns the monster's scream power level.
int Monster::getScreamPowerLevel() const {
    return screamPowerLevel;
}

// Static comparison functions
// Determines if the first Monster's scream power is less than the second's.
bool Monster::isLess(const Monster& a, const Monster& b) {
    return a.screamPowerLevel < b.screamPowerLevel;
}

// Determines if the first Monster's scream power is greater than the second's.
bool Monster::isGreater(const Monster& a, const Monster& b) {
    return a.screamPowerLevel > b.screamPowerLevel;
}

// Determines if the two Monsters have equal scream power levels.
bool Monster::isEqual(const Monster& a, const Monster& b) {
    return a.screamPowerLevel == b.screamPowerLevel;
}