// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 3 - Do You See What I See?


#ifndef MONO_STACK_H
#define MONO_STACK_H
#include <iostream> 

template <typename T>
class MonoStack {
    public:
        MonoStack(int initialSize, char stackOrder); // Constructor to ensure monotonic stack conditions
        ~MonoStack();
        void push(T c); // Add to the top while ensuring a monotonic stack
        T pop(); // Remove from the top of stack
        T peek(); // Return the top without removing
        bool isFull();
        bool isEmpty();
        int size();

    private:
        T* stackArr; // Dynamic array to store stack elements
        int count; // The number of items currently in the stack
        int maxSize; // The max capacity of the stack
        int top; // Index of the current top of the stack
        char stackOrder; // 'i' used for increasing, 'd' used for decreasing.
};

// Constructor now includes the 'stackOrder' parameter to specify increasing or decreasing stack
template <typename T>
MonoStack<T>::MonoStack(int s, char o) : stackOrder(o) {
    stackArr = new T[s]; // Dynamically allocate array based on initial size
    maxSize = s;
    count = 0; // No elements in stack initially
    top = -1; // Top is set to -1 when stack is empty
}

template <typename T>
MonoStack<T>::~MonoStack() {
    delete[] stackArr; // Free memory when the stack is destroyed
}

template <typename T>
bool MonoStack<T>::isFull() {
    return (count == maxSize); // Stack is full if count matches maxSize
}

template <typename T>
bool MonoStack<T>::isEmpty() {
    return (count == 0); // Stack is empty if count is 0
}

template <typename T>
int MonoStack<T>::size() {
    return count; // Return the number of elements in the stack
}


//Push method ensures the stack remains monotonic. If the stack is full, it dynamically resizes by doubling its capacity.
template <typename T>
void MonoStack<T>::push(T c) {
    if (isFull()) {
        T* temp = new T[2 * maxSize]; // Size doubles when stack is full. 
        for (int i = 0; i < maxSize; ++i) {
            temp[i] = stackArr[i]; // Copy old elements to the new stack
        }
        maxSize *= 2;
        delete[] stackArr; // Free old memory
        stackArr = temp;// Reassign to the new memory block
    }

   //Maintain the monotonic property based on the stack order from stackOrder. 
    while (!isEmpty() && ((stackOrder == 'i' && stackArr[top] > c) || (stackOrder == 'd' && stackArr[top] < c))) {
        pop(); //runs the while loop and pops out the value when a person can not see. 
    }

    stackArr[++top] = c; // Place the new element on top
    ++count; // Increase the stack size
}

template <typename T>
T MonoStack<T>::pop() {
    --count;
    return stackArr[top--]; // Return the top element and move the top pointer down
}

template <typename T>
T MonoStack<T>::peek() {
    return stackArr[top]; // Return the top element without removing it
}

#endif
