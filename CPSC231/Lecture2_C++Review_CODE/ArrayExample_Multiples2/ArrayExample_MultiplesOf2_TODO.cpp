/*
Write the C++ code to prompt the user for the length, n, of an array, arr. 
Dynamically allocate the array to be of size n and initialize the contents to 
the first n multiples of 2. Finally, deallocate the array.
*/

#include <iostream>
using namespace std; //we don't want it to always default to this and import all the extensions. 

int main(){
    int n;
    std::cout << "Ener the size: ";
    std::cin >> n;

    int* myArr = new int[n]; //this is a dynamically allocated array 
    for (int i = 0; i < n; i++){
        myArr[i] = 2*i;
    }

    std::cout << myArr << std::endl; // this prints the memory address of the first element of myArr

    for(int i = 0; i < n; i++){
        std::cout << myArr[i] << " ";
    }
    std::cout << std::endl;

    delete[] myArr; // this is a deconstructor. This deallocates the array.

    return 0; //always return 0, return -1 if there is an error in the code. 


}

