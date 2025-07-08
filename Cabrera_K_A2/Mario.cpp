// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 2 - Not so Super Mario Bros.

#include "Mario.h"

Mario::Mario(){
    coins = 0; 
    powerLevel = 0; 
}
Mario::~Mario(){}

void Mario::collectCoin(){

    if(coins == 20){ //If Mario earns twenty coins, he gains a life
        numLives++; 
        coins = 0;
    } else {
        coins++;
    }
}

void Mario::currPowerLevel(std::ofstream &output){
    output << "Mario is at power level " << powerLevel << ". "; //Returns Mario's power level
}

char Mario::move(char*** &grid, int gridDimension, int currLevel, std::ofstream &output){
    char currentWorldChar;

    output << " Mario will "; //Where Mario will go on the grid. 

    //If Mario wins or loses the game, he will stay put and not move. 
    if(wonGame == true || numLives == -1){
        output << "STAY PUT.";

        return currentWorldChar; //Returns empty char
    }
    int gridDirection = rand() % 4; //Selects a way for Mario to move in (up, down, left, right)

    switch(gridDirection){
        //UP
        case 0:
            if(getXCoord() == 0){ //If mario is at the top edge, it will re-direct him to the bottom edge
                setXCoordinate(gridDimension - 1);
            }else{
                setXCoordinate(getXCoord() - 1); //Removing 1, allows mario to shift up
            }
            currentWorldChar = grid[currLevel][getXCoord()][getYCoord()]; //Saves the world character before replacing the grid space with Mario
            grid[currLevel][getXCoord()][getYCoord()] = getCharacter(); //Mario is added to the grid

            output << "move UP.";
            break;
        //DOWN
        case 1:
            if(getXCoord() == gridDimension - 1){ //If mario is at the bottom edge, it will re-direct him to the top edge
                setXCoordinate(0);
            } else {
                setXCoordinate(getXCoord() + 1); //Adding 1, allows mario to shift down
            }
            currentWorldChar = grid[currLevel][getXCoord()][getYCoord()]; //Saves the world character before replacing the grid space with Mario
            grid[currLevel][getXCoord()][getYCoord()] = getCharacter(); //Mario is added to the grid

            output << "move DOWN. ";
            break;
        //LEFT
        case 2:
            if(getYCoord() == 0){ //If mario is at the left edge, it will re-direct him to the right edge. This allows him to "wrap" around the grid.
                setYCoordinate(gridDimension - 1);
            }else{
                setYCoordinate(getYCoord() - 1); //Removing 1, allows mario to shift left
            }
            currentWorldChar = grid[currLevel][getXCoord()][getYCoord()]; //Saves the world character before replacing the grid space with Mario
            grid[currLevel][getXCoord()][getYCoord()] = getCharacter(); //Mario is added to the grid

            output << "move LEFT. ";
            break;
        //RIGHT
        case 3:
            if(getYCoord() == gridDimension - 1){ //If mario is at the right edge, it will re-direct him to the left edge
                setYCoordinate(0);
            }else{
                setYCoordinate(getYCoord() + 1); //Adding 1, allows mario to shift right
            }
            currentWorldChar = grid[currLevel][getXCoord()][getYCoord()]; //Saves the world character before replacing the grid space with Mario
            grid[currLevel][getXCoord()][getYCoord()] = getCharacter(); //Mario is added to the grid

            output << "move RIGHT. ";
            break;
    }
    return currentWorldChar;

}

char Mario::warp(int x, int y, char*** &grid, int currLevel, std::ofstream &output){
    setXCoordinate(x); 
    setYCoordinate(y);
    char worldChar;

    worldChar = grid[currLevel][getXCoord()][getYCoord()]; //Saves the world character before it's replaces with Mario
    grid[currLevel][getXCoord()][getYCoord()] = getCharacter(); //Places Mario on the grid

    output << " Mario will WARP.";
    return worldChar;
}

void Mario::currCordinates(std::ofstream &output){
    output << "(" << getXCoord() << "," << getYCoord() << "). "; //Prints Mario's coordinates
}

void Mario::powerUp(){
    if(powerLevel == 2){ //If Mario is power level 2, he will not level up further
        powerLevel = 2;
    }else{
        powerLevel++;
    }
}

bool Mario::fightEnemy(char c, std::ofstream &output){
    int winPercent;

    output << "Mario fought a ";

    switch(c){ //Verifies if Mario is fighting a Koopa or Goomba
        case 'k':
            winPercent = 80; //Sets win percent
            output << "koopa and";
            break;
        case 'g':
            winPercent = 65; //Sets win percent
            output << " goomba and";
            break;
    }

    int randNum = rand() % 100 + 1; 

    if(randNum <= winPercent){ //If the random number is within win percent
        output << " won. "; //Mario wins!
        if(enemyDefeated == 7){ //if mario defeated 7 enemies, he gains a life
            ++numLives; 
            enemyDefeated = 0;
        }else{ 
            ++enemyDefeated;
        }
        return true;

    }else{
        //Mario loses
        if(powerLevel > 0){
            --powerLevel;
        }else if(numLives > -1 && powerLevel == 0){
            --numLives;
        }
        enemyDefeated = 0; //enemy defeated resets 
        output << " lost. ";
        return false;
    }
}

bool Mario::fightBoss(std::ofstream &output){
    output << "Mario has encountered a boss and";
    int winPercent = 50; //Boss win percent

    while(numLives > -1){ //Loops until Mario no longer has lives. 

        int randNum = rand() % 100; 

        if(winPercent > randNum){
            //Mario WINS!
            output << " won. ";
            return true;

        }else{
            //Mario LOSES!
            if(powerLevel >= 2){ // If Mario is at power level 2 or higher, decrease power level by 2
                powerLevel -= 2;
            } else if (powerLevel == 1) { // If Mario is at power level 1, decrease power level by 1 and decrement lives.
                powerLevel -= 1;
                numLives--;
            } else { // Mario has no power left, decrement lives.
                numLives--;
            }
        }
    }
    output << " lost. ";
    return false;
}

void Mario::setWonGame(bool wonGame){
    this->wonGame = wonGame; //returns whether Mario has won or not.
}
void Mario::endGame(std::ofstream &output, int turnsTaken){

    if(wonGame){ //Mario WINS THE GAME!
        output << "Mario saved the princess." << std::endl;
    }else{ //Mario loses the game
        output << "Mario has lost. Game ended." << std::endl;
    }
    output << "TURNS TAKEN: " << turnsTaken << std::endl;
}

bool Mario::getWonGame(){
    return wonGame;
}

void Mario::setXCoordinate(int x){
    coordinates[0] = x;
} 

void Mario::setYCoordinate(int y){
    coordinates[1] = y;
}

int Mario::getXCoord(){
    return coordinates[0];
}

int Mario::getYCoord(){
    return coordinates[1];
}

void Mario::setLives(int lives){
    numLives = lives;
}

int Mario::instancesOf(){
    return 1; //one instance of Mario
}
char Mario::getCharacter(){
    return 'H'; //Mario character
}

int Mario::getLives(){
    return numLives;
}

void Mario::removeLive(){
    --numLives;
}

int Mario::getCoins(){
    return coins;
}



