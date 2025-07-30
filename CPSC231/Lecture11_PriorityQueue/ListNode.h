#ifndef LIST_NODE_H
#define LIST_NODE_H
#include <cstdlib>

template<typename T>
class ListNode{
    public: //allows us not to have to use setters and getters. 
    ListNode(T data);
    virtual ~ListNode();
    T m_data;
    ListNode<T>* m_next; //recursive data structure b/c it points to instances of itself. Within the ListNode, we are pointing to the ListNode. 
    ListNode<T>* m_prev;
};

template<typename T>
ListNode<T>::ListNode(T data){
    m_data = data;
    m_next = NULL;
    m_prev = NULL;
}

template<typename T>
ListNode<T>::~ListNode(){
    m_next = NULL;
    m_prev = NULL;
}

#endif