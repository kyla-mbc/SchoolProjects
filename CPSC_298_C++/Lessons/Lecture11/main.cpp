// #include <iostream>
// #include "HeapContainer.h"

// using namespace std;

// int main(int argc, char** argv){
//     HeapContainer<int> stackContainer1(1);
//     HeapContainer<int> stackContainer2(3);

//     HeapContainer<int> result = stackContainer1 + stackContainer2;

//     cout << stackContainer1 << " + " << stackContainer2 << " = " << result << endl;
    
//     HeapContainer<double>* heapContainer1 = new HeapContainer<double>(1.5);
//     HeapContainer<double>* heapContainer2 = new HeapContainer<double>(2.5);

//     HeapContainer<double> heapResult = *heapContainer1 + *heapContainer2;

//     cout << "Heap result of addition: " << heapResult << endl;

//     delete heapContainer1;
//     delete heapContainer2;

//     return 0;
// }