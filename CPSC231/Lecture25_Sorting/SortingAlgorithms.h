
#include <iostream>
using namespace std;
//sort ints
void bubbleSort(int* arr, int n){
  for(int i = 0; i < n-1; ++i){
    for(int j = 0; j < n-i-1; ++j){ // we do not care to see the last value in the array since the big number has already bubbled to the front. 
      if(arr[j] > arr[j+1]){ //number of comps
        //SWAP
        int temp = arr[j];
        arr[j] = arr[j+1]; //number of swaps
        arr[j+1] = temp;
      }
    }
    if (!keepGoing){
        return;
    }
  }
}

//selection sort - pick min each time and put in position at front of the array || SELECTING the next minimum thing to the right. 
void selectionSort(int* arr, int n){
  int currMinIdx;
  for(int j = 0; j < n-1; ++j){
    currMinIdx = j;
    for(int k = j+1; k < n; ++k){
        //find the minimum value to the right of j(marker)
      if(arr[k]< arr[currMinIdx]){ 
        //swap
        currMinIdx = k;
      }
    }
    double temp = arr[j];
    arr[j] = arr[currMinIdx];
    arr[currMinIdx] = temp;
  }
}

//insertion sort - moves the array throuh every insertion. 
void insertionSort(int* arr, int n){
  for(int j = 1; j < n; ++j){
    double temp = arr[j];
    int k = j;
    while(k >0 && arr[k-1] >= temp){ //stop shifting when you find the value you want to insert at. 
      //shift
      arr[k] = arr[k-1];
      --k;
    }
    arr[k] = temp;
  }
}
 