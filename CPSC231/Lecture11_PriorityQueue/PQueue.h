//FIX THIS FILE, IT IS NOT COMPLETE

#ifndef P_QUEUE_H
#define P_QUEUE_H

#include "DblList.h"


template <typename T>
class PQueue: private DblList<T>{
    public: 
        PQueue(bool isMin);
        virtual ~PQueue();
        T remove();
        int size();
        bool isEmpty();
        T peek();

    private:
        bool isminQ;
    
}


template <typename T>
PQueue<T>::PQueue(bool isMin){
    isMinQ = isMin;
}

template <typename T>
PQueue<T>::~PQUeue(){

}

template <typename T> 
void PQueue<T>::add(T data){

}

template<typename T>
bool PQueue<T>::isEmpty(){
    return DblList<T>::isEmpty();
}

template<typename T>
int PQueue<T>::size(){
    return DblList<T>::size();
}

template <typename T> 
T PQueue<T>::remove(){
    if(isMinQ){
        return DblList<T>::removeFront();
    } else {
        return DblList<T>::removeBack();
    }
}

template <typename T> 
T PQueue<T>::peek(){
    if(isMinQ){
        return DblList<T>::get(0);
    } else {
        return DblList<T>::removeBack(DblList<T>m_size - 1);
    }
}

#endif