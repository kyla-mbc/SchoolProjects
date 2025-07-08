// #include <iostream>
// #include <string.h>

// using namespace std;

// int main(int argc, char** argv){
//     //STRINGS
//     string my_str = "String";
//     cout << "First character of my_str is: " << my_str[0] << endl;
//     my_str += "String2";
//     //"String String2"
//     my_str[6] = '_';
//     //"String String2"
//     cout << "Length of my_str: " << my_str.length() << endl;
//     cout << "Length of my_str: " << my_str.size() << endl; //alternative

//     //----------
//     //(0,0,0,0,0,0,0,0,0,0,0,0,0,0)
    
//     //ARRAYS
//     int my_arr[10];
//     cout << "First element of my_arr: " << my_arr[0] << endl;
//     my_arr[2] = 298;


//     int arr_length = sizeof(my_arr) / sizeof(my_arr[0]); // 40
//     // 40 / 4 = 10

//     // -----------
//     // STRINGS ARE ARRAYS BECAUSE THEY ARE A SERIES OF THINGS TOO!

//     // char*c_str = "Hello World!";
//     /*
//     char**
//     ["./a.out"]
//     */
    
//     cout << "Length of argv[0]: " << strlen(argv[0]) << endl;    
    
//     // for loop arguments
//     for (int i = 0; i < argc; i++) {
//         char* current_arg = argv[i];
//         for (int j = 0; j < strlen(current_arg); j++){
//             cout << current_arg[j] << "_";
//         }
//         cout << endl;
//     }
// }
