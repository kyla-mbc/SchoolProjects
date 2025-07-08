// #include <iostream>
// #include <fstream> //file reading and writing
// #include <stdexcept> //errors/exceptions

// using namespace std;

// double divide(double numerator, double denominator){
//     if (denominator == 0){
//         throw invalid_argument("Division by zero error."); //throw is keyword
//         //doesn't return anything, but causes the program to break
//     }
//     return numerator / denominator;
// }

// void readDataandPrint(string filename){
//     ifstream inputFile(filename);
//     if (!inputFile.is_open()){
//         throw invalid_argument("Missing file.");
//     }
//     string line;
//     while (getline(inputFile, line)){
//         cout << line << endl;
//     }
//     inputFile.close();
// }

// void writeToFile(string filename){
//     ofstream outputFile(filename);
//     //I already have a file named "helloworld.txt"
//     ifstream checkIfExists(filename);
//     if (!checkIfExists.is_open()){
//         throw runtime_error("File already exists");
//     }

//     outputFile << "Line 1" << endl;
//     outputFile << "Line 2" << endl; //Line 1 Line 2
// }

// int main(int argc, char** argv){
//     try{ // try is a keyword
//         double d = divide(1,2);
//         cout << d << endl;
//         double d1 = divide(1,0); //error prone case
//         cout << d1 << endl;
//     } catch (invalid_argument& e){
//         cout << e.what() << endl;
//         return 1; // 1 error code is bad
//     } catch (runtime_error& e){
//         cout << e.what() << endl;
//         return 1; 
//     } catch (...){
//         cout << "Unknown error has occured" << endl;
//         return 1; 

//     }

//     return 0; 
// }