
/*
Write a program that reads integers from a file called numbers.txt, sums them up, and writes the result to a file called sum.txt.
*/

#include <iostream>   // Include the iostream library for input/output operations
#include <fstream>    // Include the fstream library to handle file input/output

int main(){
    std::ifstream inFile("numbers.txt");
    std::ofstream outFile("sum.txt");

    int number, sum = 0;


    if(inFile.is_open()){
        while (inFile >> number){
            sum += number; 
        }
        inFile.close(); //always remember to close your file.
    } else {
        std::cout << "Something went wrong when opening the input file!" << std::endl;
        return 1;
    }

    if (outFile.is_open()){
        outFile << "Sum: " << sum << std::endl;
        outFile.close();
    }else{
        std::cout << "Something went wrong when opening the output file! here is the sum:" << sum << std::endl;
    }

    return 0;
}

