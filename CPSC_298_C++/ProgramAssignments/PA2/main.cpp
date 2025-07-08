// #include <iostream>
// using namespace std;

// //Global arrays to store contacts and phone numbers.
// string* names = new string[100]; 
// unsigned long* phoneNumbers = new unsigned long[100];

// //Function to add a new contact or revise and already existing one. 
// bool addContact(string name, unsigned long phoneNumber){
//     for (int i = 0; i < 100; i++){ //iterate through the stored contacts and update any phone numbers
//         if (names[i] == name){
//             phoneNumbers[i] = phoneNumber; //changes old phone number to new input. 
//             return false; // contact updated.
//         }
//     }
//     //Finds an empty slot to add the new contact information.
//     for (int i = 0; i < 100; i++){ 
//         if (names[i] == "" && phoneNumbers[i] == 0){ //if the name and phone number does not exist, code will run.
//             names[i] = name; //adds name
//             phoneNumbers[i] = phoneNumber; //adds phone number
//             return true; // contact added. 
//         }
//     }
// }

// //Function to search for a contact by name and return the phone number.
// unsigned long searchContact(string name){
//     for (int i = 0; i < 100; i++){ // starts to iterate through a for loop until the maximum amount of stored numbers is reached.
//         if (names[i] == name && phoneNumbers[i] != 0){ //iterates and checks for a matching name and phone number.
//             return phoneNumbers[i]; //If contact is found, phone number is returned. 
//         }
//     }
//     return 0; // Contact is not found. 
// }

// //Function to display all contacts.
// void displayContacts(){
//     int contacts = 0;
//     for (int i = 0; i < 100; i++){
//         if (names[i] != "" && phoneNumbers[i] != 0){
//             cout << names[i] << ": " << phoneNumbers[i] << endl; //if names and phone numbers are present, they will print out. 
//             contacts++; //goes to the next contact and proceeds to print out in the format of the preivious line. 
// 		}else{
// 			if (contacts == 0){ //will run if no contacts have been stored yet.
// 				cout << "No contacts found" << endl;
// 				return;
// 			}	
// 		}
//     }
// }

// // Main function to interact with the user. 
// int main(int argc, char** argv){

//     string contactname;
//     unsigned long number;

//     const string menu = "------------------------------\n"
//     "Please select the number from the following options:\n"
//     " 1) Add contact\n 2) Search contact\n"
//     " 3) Display all contacts\n 4) Quit\n"
//     "------------------------------"; // Menu options

//     int inputOption;
//     do {
//         cout << menu << endl; // Printing the menu
//         cin >> inputOption; // Getting the user input number
//         cin.ignore(); // Ignore trailing input
//         if (inputOption == 1){ //adds contact.
//             cout << "What is the new contact's name?" << endl; 
//             getline(cin, contactname); //gets user input for contact's name.
//             cout << "What is the contact's phone number?" << endl;
//             cin >> number; // gets user input for contact's number. 
//             cin.ignore();
//             if (addContact(contactname, number)){
//                 cout << "Successfully added new contact!" << endl; //contact will be added.
//             } else {
//                 cout << "Replaced " << contactname << "'s phone number with " << number << "." << endl; //if contact already exists, contact will be revised. 
//             }
//         } else if (inputOption == 2) { //Searches for contact
//             cout << "What is the name of the contact you're searching for?: " << endl;
//             getline(cin, contactname); //takes in user input for name being searched. 
//             unsigned long pNumber = searchContact(contactname);
//             if (pNumber != 0){ //if contact is found, this if block will run and contact information will be printed. 
//                 cout<< contactname << ": " << pNumber << endl;
//             } else{ // if no contact is found, the code will inform the user. 
// 				cout << "No contact found for \"" << contactname << "\"" << endl;

// 			}
//         } else if (inputOption == 3) { // display contacts
// 			displayContacts();
//         } else if (inputOption == 4) { //exits the program. 
//             cout << "Exiting program..." << endl;
//             break; // exits the while loop
//         } else { // if user prints a number not in the options, code in else block will run. 
//             cout << "Not a valid option, please try again." << endl;
//         }
//     } while (true);

//     //Cleans up memory so my arrays are not stored in my professor's computer.  
//     delete[] names;
//     delete[] phoneNumbers;

//     return 0; //always return 0 at the end of the main function.
// }
