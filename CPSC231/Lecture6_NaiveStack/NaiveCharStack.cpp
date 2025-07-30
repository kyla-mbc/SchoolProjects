#include "NaiveCharStack.h"

NaiveCharStack::NaiveCharStack(int initialSize){
    //allocate the memory for the array.
    stackArr = new char[initialSize];
    maxSize = initialSize;
    count = 0;
    top = -1;
}

NaiveCharStack::~NaiveCharStack(){
    delete[] stackArr;
}

bool NaiveCharStack::isFull(){
    return (count == maxSize);
}

bool NaiveCharStack::isEmpty(){
    return (count == 0);
}

int NaiveCharStack::actualSize(){
    return count;
}


void NaiveCharStack::push(char c){
    if(isFull()){
        //increase size of stackArr
        char* temp = new char[2*maxSize];
        for(int i = 0; i < maxSize; ++i){
            temp[i] = stackArr[i];
        }
        maxSize *= 2;
        delete[] stackArr;
        stackArr = temp;
    }
    stackArr[++top] = c;
    ++count;
}

char NaiveCharStack::pop(){
    --count;
    return stackArr[top--];
}

char NaiveCharStack::peek(){
    return stackArr[top];
}