// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 4 - Genetic Palindromes

#ifndef DBL_LIST_H
#define DBL_LIST_H
#include <iostream>
#include <cstdlib>

#include "ListNode.h"

//Template class for a doubly linked list. 
template <typename T>
class DblList {
public:
    DblList(); //Constructor initializes empty list
    virtual ~DblList(); //Deconstructor
    int size() const; //Returns number of elements in the list.
    bool isEmpty() const; //Checks if the list is empty. 

    void addFront(T data); //Adds an element to the front of the list.
    void addBack(T data); //Adds an element to the back of the list. 
    void add(int pos, T data); //Adds a new element to a particular part of the list.
    
    T get(int pos) const;
    T removeFront(); //Removes element from the front of the list. 
    T removeBack(); //Removes element from the back of the list. 
    T remove(int pos); //Removes element from particular part of the list. 
   
    ListNode<T>* getFront() const; // Returns pointer to the front node
    ListNode<T>* getBack() const;  // Returns pointer to the back node
    int getSize() const;           // Returns the size of the list

private:
    ListNode<T>* m_front;
    ListNode<T>* m_back;
    int m_size;
    void clear(); // helper for destructor to free memory
};

// Constructor
template<typename T>
DblList<T>::DblList() : m_front(nullptr), m_back(nullptr), m_size(0) {}

// Destructor
template<typename T>
DblList<T>::~DblList() {
    clear();
}

// Helper function to free all nodes in the list
template<typename T>
void DblList<T>::clear() {
    ListNode<T>* current = m_front;
    while (current != nullptr) {
        ListNode<T>* toDelete = current;
        current = current->m_next;
        delete toDelete;
    }
    m_front = nullptr;
    m_back = nullptr;
    m_size = 0;
}

// Return size of the list
template<typename T>
int DblList<T>::size() const {
    return m_size;
}

template <typename T>
ListNode<T>* DblList<T>::getFront() const {
    return m_front;
}

template <typename T>
ListNode<T>* DblList<T>::getBack() const {
    return m_back;
}

template <typename T>
int DblList<T>::getSize() const {
    return m_size;
}


// Check if list is empty
template<typename T>
bool DblList<T>::isEmpty() const {
    return (m_size == 0);
}

// Add element at the front
template <typename T>
void DblList<T>::addFront(T data) {
    ListNode<T>* newNode = new ListNode<T>(data);
    if (!isEmpty()) {
        newNode->m_next = m_front;
        m_front->m_prev = newNode;
    } else {
        m_back = newNode;
    }
    m_front = newNode;
    ++m_size;
}

// Add element at the back
template<typename T>
void DblList<T>::addBack(T data) {
    ListNode<T>* newNode = new ListNode<T>(data);
    if (!isEmpty()) {
        newNode->m_prev = m_back;
        m_back->m_next = newNode;
    } else {
        m_front = newNode;
    }
    m_back = newNode;
    ++m_size;
}

// Add element at a specific position
template<typename T>
void DblList<T>::add(int pos, T data) {
    if (pos < 0 || pos > m_size) {
        std::cout << "Position out of range for add operation." << std::endl;
    }
    if (pos == 0) {
        addFront(data);
    } else if (pos == m_size) {
        addBack(data);
    } else {
        ListNode<T>* current = m_front;
        for (int i = 0; i < pos; ++i) {
            current = current->m_next;
        }
        ListNode<T>* newNode = new ListNode<T>(data);
        current->m_prev->m_next = newNode;
        newNode->m_prev = current->m_prev;
        newNode->m_next = current;
        current->m_prev = newNode;
        ++m_size;
    }
}

// Get element at a specific position
template<typename T>
T DblList<T>::get(int pos) const {
    if (pos < 0 || pos >= m_size) {
        std::cout << "Position out of range for get operation." << std::endl;
    }
    ListNode<T>* current = m_front;
    for (int i = 0; i < pos; ++i) {
        current = current->m_next;
    }
    return current->m_data;
}

// Remove element from the front
template<typename T>
T DblList<T>::removeFront() {
    if (isEmpty()) {
        std::cout << "Cannot remove from an empty list." << std::endl;
    }
    T data = m_front->m_data;
    if (m_size == 1) {
        delete m_front;
        m_front = nullptr;
        m_back = nullptr;
    } else {
        ListNode<T>* currFront = m_front;
        m_front = m_front->m_next;
        m_front->m_prev = nullptr;
        delete currFront;
    }
    --m_size;
    return data;
}

// Remove element from the back
template<typename T>
T DblList<T>::removeBack() {
    if (isEmpty()) {
        std::cout << "Cannot remove from an empty list." << std::endl;
    }
    T data = m_back->m_data;
    if (m_size == 1) {
        delete m_back;
        m_front = nullptr;
        m_back = nullptr;
    } else {
        ListNode<T>* currBack = m_back;
        m_back = m_back->m_prev;
        m_back->m_next = nullptr;
        delete currBack;
    }
    --m_size;
    return data;
}

// Remove element from a specific position
template<typename T>
T DblList<T>::remove(int pos) {
    if (isEmpty()) {
        std::cout << "Cannot remove from an empty list." << std::endl;
    }
    if (pos < 0 || pos >= m_size) {
        std::cout << "Position out of range for remove operation." << std::endl;
    }
    T data;
    if (pos == 0) {
        data = removeFront();
    } else if (pos == m_size - 1) {
        data = removeBack();
    } else {
        ListNode<T>* current = m_front;
        for (int i = 0; i < pos; ++i) {
            current = current->m_next;
        }
        data = current->m_data;
        current->m_prev->m_next = current->m_next;
        current->m_next->m_prev = current->m_prev;
        delete current;
        --m_size;
    }
    return data;
}

#endif
