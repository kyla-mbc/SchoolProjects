// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 3 - Do You See What I See?


#include "SpeakerView.h"
#include <fstream>
#include <iostream>

// The SpeakerView class is used to process the information within the input file
// and uses MonoStack to calculate the visibility of each audience member.
SpeakerView::SpeakerView() : rows(0), cols(0), aHeight(nullptr) {}

// Destructor frees the dynamically allocated 2D array for aHeight.
SpeakerView::~SpeakerView() {
    // Check if the 2D array 'aHeight' is allocated
    if (aHeight) {
        // Loop through each row of the array
        for (int i = 0; i < rows; ++i) {
            // Free the memory allocated for each row (array of columns)
            delete[] aHeight[i]; // Free each row
        }
        // Free the memory allocated for the array of pointers (rows)
        delete[] aHeight; // Free the array of pointers
    }
}

void SpeakerView::processFile(std::string inputFile) {
    // Open the input file
    std::ifstream inFile(inputFile);
    if (!inFile.is_open()) {
        // If the file couldn't be opened, print an error message and exit the function
        std::cout << "Error: Unable to open the input file: " << inputFile << std::endl;
        return;
    }

    std::string line;
    bool readHeight = false; // Flag to indicate when to start reading audience heights
    int rowIdx = 0; // Row index for counting rows

    // First pass through the file to determine the number of rows and columns
    while (std::getline(inFile, line)) {
        // If we find the "BEGIN" marker, we start reading heights
        if (line == "BEGIN") {
            readHeight = true;
            continue;
        }

        // If we encounter the "END" marker, we stop processing the file
        if (line == "END") {
            break;
        }

        if (readHeight) {
            // For the first row, we determine the number of columns by counting the numbers in the line
            if (rowIdx == 0) {
                int colNum = 0; // Variable to count columns (numbers in a row)
                for (size_t i = 0; i < line.size(); ++i) {
                    // If we detect a digit or a decimal point, we consider it the start of a number
                    if (isdigit(line[i]) || line[i] == '.') {
                        while (i < line.size() && (isdigit(line[i]) || line[i] == '.')) {
                            ++i;
                        }
                        // Each number is treated as a column
                        ++colNum;
                    }
                }
                cols = colNum; // Store the total number of columns
            }

            // Count rows by counting each valid line
            ++rowIdx;
        }
    }

    rows = rowIdx; // Store the total number of rows
    inFile.close(); // Close the file after the first pass

    // Reopen the file to read the audience heights and fill the 2D array
    inFile.open(inputFile);
    if (!inFile.is_open()) {
        // If reopening fails, print an error message and exit
        std::cout << "Error: Unable to reopen the input file: " << inputFile << std::endl;
        return;
    }

    // Allocate memory for a 2D array to store audience heights (rows x cols)
    aHeight = new double*[rows]; // Allocate memory for rows
    for (int i = 0; i < rows; ++i) {
        aHeight[i] = new double[cols]; // Allocate memory for each row (columns)
    }

    rowIdx = 0; // Reset the row index to start filling the array
    readHeight = false; // Reset the flag for the second pass

    // Second pass through the file to fill the aHeight array
    while (std::getline(inFile, line)) {
        // Start reading heights after the "BEGIN" marker
        if (line == "BEGIN") {
            readHeight = true;
            continue;
        }

        // Stop reading after the "END" marker
        if (line == "END") {
            break;
        }

        if (readHeight) {
            int colIdx = 0; // Column index for the current row
            std::string number = ""; // Temporary string to build numbers

            // Loop through each character in the line to extract numbers
            for (size_t i = 0; i < line.size(); ++i) {
                // If we find a digit or decimal point, add it to the current number string
                if (isdigit(line[i]) || line[i] == '.') {
                    number += line[i];
                } 
                // If we hit a space or the end of the line, process the built number
                else if (line[i] == ' ' || i == line.size() - 1) {
                    if (!number.empty()) {
                        // Convert the number string to a double and store it in the array
                        aHeight[rowIdx][colIdx] = std::stod(number);
                        number = ""; // Reset the number string for the next number
                        colIdx++; // Move to the next column
                    }
                }
            }

            // If there's a number left at the end of the line, process it
            if (!number.empty()) {
                aHeight[rowIdx][colIdx] = std::stod(number);
            }

            rowIdx++; // Move to the next row
        }
    }

    inFile.close(); // Close the input file after reading
    createView(); // Call createView to calculate visibility after processing the file
}

// createView calculates and prints how many people in each column can see the speaker.
// It uses a monotonically decreasing stack to ensure visibility is tracked correctly.
void SpeakerView::createView() {
    for (int col = 0; col < cols; ++col) {
        MonoStack<double> stack(rows, 'd'); // Monotonically decreasing stack for each column
        std::cout << "In column " << col << " there are ";

        int canSee = 0; // Counter for the number of people who can see the speaker
        std::string canSeeHeight; // String to store the heights of those who can see

        for (int row = 0; row < rows; ++row) {
            double height = aHeight[row][col]; // Get the height of the current audience member

            if (stack.isEmpty() || height > stack.peek()) {
                stack.push(height); // Push the height to the stack as this person can see the speaker
                canSee++; // Increment the visible count

                int intPart = static_cast<int>(height); // Get the integer part of the height
                int decimalPart = static_cast<int>((height - intPart) * 10 + 0.5); // Proper rounding for one decimal

                if (decimalPart == 0) {
                    canSeeHeight += std::to_string(intPart) + ", "; // No decimal if decimalPart is 0
                } else {
                    canSeeHeight += std::to_string(intPart) + "." + std::to_string(decimalPart) + ", ";
                }
            }
        }

        std::cout << canSee << " that can see. Their heights are: ";
        std::cout << canSeeHeight.substr(0, canSeeHeight.size() - 2); // Remove the last comma and space
        std::cout << " inches." << std::endl; // Add "inches" after all heights
    }
}