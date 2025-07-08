// #include <iostream>

// using namespace std;

// int main(int argc, char** argv){
//     int original_variable = 42;

//     // reference variable
//     int& reference_variable = original_variable;
//     reference_variable = 50;

//     cout << original_variable << endl;

//     // dereferencing, pointing
//     int* my_pointer = nullptr;

//     my_pointer = &(original_variable); 

//     cout << my_pointer << endl;

//     *my_pointer = 30;  //dereference to access object, the pointer is basically an arrow that is to just point at you. 

//     cout << original_variable << endl;
//     cout << *my_pointer << endl;

//     int* heap_int = new int(55);
//     string* heap_string = new string("my str");
//     delete heap_int;
//     delete heap_string;


//     // arrays
//     int stack_arr [50]{1,2,3,4,5};// array of 50 integers
//     int* heap_arr = new int[50]; // heap array of 50 integers
//     delete[] heap_arr;

//     // iterating the stack array
//     // int stack_arr = new int[10];
//     // int* heap_arr = new int[10];

//     cout<< "Stack Array" << endl;
//     for (int i = 0; i < 10; i++){
//         cout<< stack_arr[i] << endl;
//     }

//     cout<< "Heap Array" << endl;
//     for (int i = 0; i < 10; i++){
//         cout<< heap_arr[i] << endl;
//     }


//     return 0;
// }


// // Stack is short term memory and stores local variables 
// // Heap is long term memory
// // In Java, primitives are stored on stack and objects are on heap
// // In C++, you can choose where to store them