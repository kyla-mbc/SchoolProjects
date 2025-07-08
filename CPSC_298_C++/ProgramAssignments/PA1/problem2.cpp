// #include <iostream>
// using namespace std;

// int main(int argc, char** argv){
//     string userInput; // Create a variable userInput that stores the user input of a sentence.
//     cout << "Input a sentence: "; // prompt the user to input a sentence to corrupt.
//     getline(cin, userInput); //
//     if (userInput != ""){ // checks if the user has inputted anything to the prompt.
//         userInput[0] = '?'; //Changes the first character of the sentence inputted to '?'.
//         cout << "You inputted: " << "\"" << userInput << '!' << "\"" << endl; //Print out the new sentence with the altered first character. 
//         cout << "Successfully read " << (userInput.length() - 1) << " out of " << (userInput.length()) << " characters" << endl; // Prints out how many proper characters have been read from the original sentence.
//     }
//     else{
//         cout << "There was no input data to corrupt." << endl; //If there was no data inputted by the user, the code will print out an error message to the user. 
//     }
//     return 0;
// }