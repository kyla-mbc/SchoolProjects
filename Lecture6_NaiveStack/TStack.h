#ifndef TSTACK_H
#define TSTACK_H


template <typename T> //create TStack object. 

class TStack{
    public:
        TStack(int initialSize);
        ~TStack();
        
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


template <typename T>
TStack<T>::TStack(int initialSize){
    //allocate the memory for the array.
    stackArr = new char[initialSize];
    maxSize = initialSize;
    count = 0;
    top = -1;
}

template <typename T>
TStack<T>::~TStack(){
    delete[] stackArr;
}

template <typename T>
bool TStack<T>::isFull(){
    return (count == maxSize);
}

template <typename T>
bool TStack<T>::isEmpty(){
    return (count == 0);
}

template <typename T>
int TStack<T>::actualSize(){
    return count;
}

template <typename T>
void TStack<T>::push(char T){
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

template <typename T>
char TStack<T>::pop(){
    --count;
    return stackArr[top--];
}

template <typename T>
char TStack<T>::peek(){
    return stackArr[top];
}

#endif
