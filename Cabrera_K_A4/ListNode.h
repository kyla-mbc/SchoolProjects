// Full Name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course Number and Section: CPSC 350-03
// Assignment or Exercise Number: Programming Assignment 4 - Genetic Palindromes

#ifndef LIST_NODE_H
#define LIST_NODE_H
#include <cstdlib>

//Templated ListNode class to represent a node in a doubly linked list. 
template<typename T>
class ListNode{
    public:
    ListNode(T data);//Constructor that initializes a node with the given data. 
    virtual ~ListNode(); //Destructor
    T m_data; //Data element of the node (templated type T)
    ListNode<T>* m_next; //Pointer to the next node in the list.
    ListNode<T>* m_prev; //Pointer to the previous node in the list. 
};

//Constructor implementation: initializes the node's data and sets pointers to null. 
template<typename T>
ListNode<T>::ListNode(T data){
    m_data = data;
    m_next = NULL; //Initialize next pointer to null (end of list).
    m_prev = NULL; //Initialize previous pointer to null (start of list).
}

//Destructor that resets pointers to null. 
template<typename T>
ListNode<T>::~ListNode(){
    m_next = NULL; //Clear next pointer. 
    m_prev = NULL; //Clear previous pointer. 
}

#endif


