#include <iostream> //allows ofr input and output.
#include <cstdlib> //standard library
#include <ctime> //seed of random number generator

/*
    You need to create a C++ program with three main parts. First, write a sumRows() 
    function that takes a matrix of integers (as a pointer to an array of pointers)
     and a one-dimensional array (as a pointer). This function will calculate the sum of each row 
     in the matrix and store these sums in the one-dimensional array. 
     
     Next, create a randomMatrix() function that accepts the number of rows and columns as input, 
     then fills a dynamically allocated matrix with random integers. 
     
     Finally, in the main() function, prompt the user to input the dimensions of the matrix, 
     allocate memory for it, and use randomMatrix() to fill it with random values. After displaying the matrix, 
     call sumRows() to compute and display the sum of each row. 
     Remember tofree the allocated memory before the program exits to avoid memory leaks.
*/


// Function to fill an array with the sum of each row of the matrix

void sumRows (int** matrix, int* rowSums, int rows, int cols){ 
    for(int i = 0; i < rows; i++){
        int sum = 0; //once we're done with one row, we go back to 0
        for (int j = 0; j < cols; j++){
            sum += matrix [i][j];
        }
        rowSums[i] = sum; //after the nested loops, we should have rowSum filled out. 
    }
}


// Function to create a matrix with random integers
void randomMatrix(int** matrix, int rows, int cols){
    for(int i = 0; i < rows; i++){
        for (int j = 0; j < cols; j++){
            matrix[i][j] = std :: rand() % 100; // random numbers from 0 - 99.
        }
    }
}


int main() {
    std::srand(static_cast<unsigned>(std::time(0))); //generates different random numbers every time it runs. 
    //get dimentions from user
    int rows, int cols;
    std::cout << "Enter the num of rows: ";
    std::cin >> rows;
    std::cout << "Enter the num of cols";
    std::cin >> cols;

    //dynamically allocate a matrix 
    int** matrix = new int*[rows];
    for (int i = 0; i < rows; i++){
        matrix[i] = new int [cols];
    } //we cannot gurantee everything is 0 so we always have to initialize the matrix. 

    int* rowSums = new int [rows];

    randomMatrix(matrix, rows, cols); //set each value to a rand num from 0 - 99.

    //print the values of the matrix
    for (int i = 0; i < rows: i++){
        for (int j = 0; j < cols; j++){
            std::cout << "\n";
        }
    }

    sumRows(matrix, rowSums, rows, cols);
    for (int i = 0; i < rows; i++){
        std::cout << "Row" << i+1 << ":" << rowSums[i] << std::endl;
    }

    for(int i = 0; i < rows; i++){
        delete[] matrix[i]; // deleting the inner arrays
    }

    delete[] rowSums; 
    delete[] matrix; //delete the other shell arrays

    return 0;
}
