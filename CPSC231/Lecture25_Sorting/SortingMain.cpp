#include <iostream>
#include <cstdlib>
#include <ctime>
#include "SortingAlgorithms.h"

using namespace std; 
void printArray(int* arr, int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << "\t";
    }
    cout << endl;
}

void resetArray(int* arr, int size){
    // if size = 10, creates array: 4 2 1 0 10 3 13 16 15 18 
    srand(5923); // set the seed value to 5923 so that we all get the same numbers        
    for (int i = 0; i < size; i++) {
        arr[i] = rand() % 21; // values between 0 & 20
    } 
}
int main() {
    int array[10];
    
    // testing bubble sort
    cout << endl << "testing bubble sort" << endl;
    resetArray(array, 10);
    cout << "original array: " << endl;
    printArray(array, 10);
    cout << "sorted array: " << endl;
    bubbleSort(array, 10);
    printArray(array, 10);

    // testing selection sort
    cout << endl << "testing selection sort" << endl;
    resetArray(array, 10);
    cout << "original array: " << endl;
    printArray(array, 10);
    cout << "sorted array: " << endl;
    selectionSort(array, 10);
    printArray(array, 10);

    // testing insertion sort
    cout << endl << "testing insertion sort" << endl;
    resetArray(array, 10);
    cout << "original array: " << endl;
    printArray(array, 10);
    cout << "sorted array: " << endl;
    insertionSort(array, 10);
    printArray(array, 10);

/*
    // testing merge sort
    cout << endl << "testing merge sort" << endl;
    resetArray(array, 10);
    cout << "original array: " << endl;
    printArray(array, 10);
    cout << "sorted array: " << endl;
    mergeSort(array, 0, 9);
    printArray(array, 10);

    // testing quick sort 
    cout << endl << "testing quick sort" << endl;
    resetArray(array, 10);
    cout << "original array: " << endl;
    printArray(array, 10);
    cout << "sorted array: " << endl;
    quickSort(array, 0, 9);
    printArray(array, 10);

*/
  return 0;
  
}