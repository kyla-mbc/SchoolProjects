#include <iostream>
using namespace std; 

// SIMPLE SEARCH
// return the first index of the array that contains value "key"
// how bad is the performance of this algo?
    // worst case, I need to iterate thru the entire arr bc "key" is the last 
        // element. So we'd have to do "len" amount of comparisons -> Oh(n)
    // best case, "key" is the first element so constant -> Omega(1)
int simpleSearch(int* arr, int len, int key ){
    //if key is not found, we want to return -1
    int idx = -1;
    int comparisons = 0;
    for(int i = 0; i < len; i++){
        if (arr[i] == key){
            idx = i; //we have found the key
            break; 
        }
 
    }
    cout << "I did " << comparisons << " comparisons in simple search" << endl;
    return idx;
} 

// BINARY SEARCH 
// assumes array is ordered/ sorted!!! 
// return the first index of the array that contains value "key"
// worst case -> Oh(log n)
// best case -> Omega(1) // if key is in "middle" the first time 
int binarySearch(int* arr, int len, int key){
    int right = len; // tp start off the right bound of arr is at len
    int left = 0; //to start off the left bound of arr is 0
    
    int idx = -1;
    int comparisons = 0;

    while (right >= left){ //this ensires that our values don't cross over. 
        ++comparisons;
        int middle = (right + left) / 2; //find and update the middle marker 

        //checl whether the key is in the middle marker 
        if (arr[middle] == key){
            idx = middle;
            break;
        }

        //if not found, check whether we should look left or right of middle 
        if (key < arr[middle]){
            //look left, move the right marker left
            right = middle - 1; //we already know key is not in middle so we skip it. 
        } else{
            //look right, move the left marker right
            left = middle + 1; //we already know key is not in middle so we skip it. 
        }
    }
    return idx;
}


int main(){
    cout << "Populating array." << endl;
    int len = 10000;
    int key = 8000;

    int* myArr = new int[len];
    for (int i = 0; i < len; ++i){
        myArr[i] = i*2;
    }
    cout << "Starting simple search..." << endl;
    cout << "Found the key " << key << " at index " << simpleSearch(myArr, len, key) << endl;
    cout << "Ending simple search..." << endl;

    cout << "Starting binary search..." << endl;
    cout << "Found the key " << key << " at index " << binarySearch(myArr, len, key) << endl;
    cout << "Ending binary search..." << endl;

    delete[] myArr; // clean up after yourself :) 
    return 0;
}