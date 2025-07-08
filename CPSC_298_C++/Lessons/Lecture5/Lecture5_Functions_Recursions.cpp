// #include <iostream>

// using namespace std;

// void passByValue(int value) {

//     value += 10; // Wouldn't affect the original variable

// }

// void passByReference(int& reference) {

//     reference += 10; // This WOULD affect the original variable

// }

// // 'const' is like a final; it's constant and doesn't change
// void passByReferenceAndValue(const int& reference) {

//     // reference += 10; // This does not work

// }

// void printIntArray(const int* arr, int size) {

//     for (int i = 0; i < size; i++) {
//         cout << arr[i] << " ";
//     }
//     cout << endl;

// }

// // Recursion
// // n * (n - 1) * (n - 2) * ... * 1
// int factorial(int n) {

//     if (n == 0 || n == 1) {
//         return 1;
//     }
//     return n * factorial(n - 1);

// }

// // Multiple arguments, with default values
// // void displayMessage(string message, int times = 1) WORKS
// // void displayMessage(string message = "", int times = 1) WORKS
// // void displayMessage(string message = "", int times) DOESN'T WORK
// // displayMessage(10) DOESN'T WORK
// void displayMessage(string message, int times = 1) {

//     for (int i = 0; i < times; i++) {
//         cout << message << endl;
//     }

// }

// // Function declaration
// void a(); // Function/Method signature

// void b() {
//     a();
// }

// void a() {
//     // Do nothing
// }

// // 'int' is the return type
// int main(int argc, char** argv) {

//     int i = 14;
//     passByReference(i);
//     // passByReference(10); // Doesn't work
//     cout << i << endl;

//     return 0;
// }