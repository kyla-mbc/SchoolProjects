//where arrays are bad, linked lists are good. 
//where linked lists are good, arrays are bad. For large lists, used a linked list. 


#ifndef DBL_LIST_H
#define DBL_LIST_H
#include <cstdlib>

#include "ListNode.h"

template <typename T>
class DblList{
    public:
        DblList();
        ~DblList();
        int size();
        bool isEmpty();

        void addFront(T data);
        void addBack(T data);
        void add(int pos, T data); //pos - position
       
        T removeFront();
        T removeBack();
        T remove(int pos);

    protected: //if we made this private, only this class can see it and its children. With protected, the other files have access to this. 
        ListNode<T>* m_front;
        ListNode<T>* m_back;
        int m_size;
};

template<typename T>
DblList<T>::DblList(){
    m_front = NULL;
    m_back = NULL;
    m_size = 0;
}

template<typename T>
DblList<T>::~DblList(){
    //todo - free memory - loop through and delete
    m_front = NULL;
    m_back = NULL;
    m_size = 0;
}

template<typename T>
int DblList<T>::size(){
    return m_size;
}

template<typename T>
bool DblList<T>::isEmpty(){
    return (m_size == 0);
}

template <typename T>
void DblList<T>::addFront(T data){
    ListNode<T>* newNode = new ListNode<T>(data); // create new node (aka newNode)
		// set newNode’s prev pointer to NULL (done in constructor)
    if (!isEmpty()){ // if linked list is not empty 
        newNode -> m_next = m_front; // set newNode’s next pointer to the old front (aka oldFront)
        m_front -> m_prev = newNode; // set oldFront’s prev pointer to newNode 
    } else { // if list is empty (newNode is 1st node) 
        m_back = newNode; // then set back to newNode too
    }
    m_front = newNode; // set front to newNode regardless 
    ++m_size; // add one to size 
}

template<typename T>
void DblList<T>::addBack(T data){
    ListNode<T>* newNode = new ListNode<T>(data);
    if(!isEmpty()){
        newNode->m_prev = m_back;
        m_back->m_next = newNode;
    }else{
        m_front = newNode;
    }
    m_back = newNode;
    ++m_size;
}

template<typename T>
void DblList<T>::add(int pos, T data){ //addmethod
    if(isEmpty()){
        addFront(data); //when linked list is empty, the only thing you can do is add. 
    }else if(pos == 0){ //addFront if position is at 0.
        addFront(data);
    }else if(pos >= m_size){
        addBack(data); //addBack when position is greater than or equal to size. 
    }else{
        ListNode<T>* current = m_front;
        int cPos = 0;
        while(cPos != pos){
            current = current->m_next;
            ++cPos;
        }
        ListNode<T>* newNode = new ListNode<T>(data); //Create new Node => Remember the ABCDE example. 
        current->m_prev->m_next = newNode; //Switch node positions around. D to C to E 
        newNode->m_prev = current->m_prev;
        current->m_prev = newNode;
        newNode->m_next = current;
        ++m_size;
    }
}

template<typename T> //returns a typename named T. 
T DblList<T>::removeFront(){
    //make sure not empty
    T data = m_front->m_data; //Keep track of the data we're going to return. Save the data to be deleted so we can return 
    if(m_size == 1){
        delete m_front; // call the destructor for the node at m_front. 
        m_front = NULL;
        m_back = NULL;
    }else{
        ListNode<T>* currFront = m_front; //Keep track of the current front. 
        m_front = currFront->m_next;
        m_front->m_prev = NULL;
        delete currFront;
    }
    --m_size;
    return data;
}

template<typename T>
T DblList<T>::removeBack(){
    //make sure not empty
     T data = m_back->m_data;
     if(m_size == 1){
        delete m_back;
        m_front = NULL;
        m_back = NULL; 
     }else{
        ListNode<T>* currBack = m_back;
        m_back = currBack->m_prev;
        m_back->m_next = NULL;
        delete currBack;
     }
     --m_size;
     return data;
}

template<typename T>
T DblList<T>::remove(int pos){
    //make sure not empty
    T data;
    if(pos == 0){
        data = removeFront();
    }else if(pos >= m_size -1){
        data = removeBack();
    }else{
        ListNode<T>* current = m_front;
        int cPos = 0; //current positon, you can also use a helper method. 
        while(cPos != pos){
            current = current->m_next;
            ++cPos;
        }
        data = current->m_data;
        current->m_prev->m_next = current->m_next;//connect B's next pointer to D  D's back pointer to B in order to remove C. 
        current->m_next->m_prev = current->m_prev;//connect D's back pointer to B in order to remove C. 
        delete current;
        --m_size;
    }
    return data;
}

template<typename T>
T DblList<T>::get(int pos){ //To get a certain position. 
    //is pos in range, etc. || Check for edge cases. 
    ListNode<T>* current = m_front;
    int cPos = 0;
    while(cPos != pos){
        current = current->m_next;
        ++cPos;
    }
    return current->m_data;
}


#endif