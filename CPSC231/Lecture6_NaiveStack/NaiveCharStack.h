#ifndef NaiveCharStack_H
#define NaiveCharStack_H

class NaiveCharStack{
    public:
        NaiveCharStack(int initialSize);
        ~NaiveCharStack();
        
        //interface:
        void push(char c); //add to the top
        char pop(); //remove from the top
        char peek(); //return the top without removing

        //helper methods:
        bool isFull(); 
        bool isEmpty();
        int actualSize();
        int maxsize();

    private:
        char* stackArr;
        int count; //number of items currently in the stack
        int maxSize; //max number of things in the stack
        int top; //index of the current top of the stack
};

#endif