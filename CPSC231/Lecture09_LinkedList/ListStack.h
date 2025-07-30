#ifndef ListStack_H
#define ListStack_H


template <typename T> //create ListStack object. 

class ListStack{
    public:
        ListStack(); //No need for initial size cause this stack is perfectly dynamically. 
        ~ListStack();
        
        //interface:
        void push(T c); //add to the top
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
ListStack<T>::ListStack(int initialSize){
    //allocate the memory for the array.
    m_list = new DblList<T>();
}

template <typename T>
ListStack<T>::~ListStack(){
    delete stackArr;
}

template <typename T>
bool ListStack<T>::isEmpty(){
    return (count == 0);
}

template <typename T>
int ListStack<T>::actualSize(){
    return m_list->size;
}

template <typename T>
void ListStack<T>::push(char T){
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
char ListStack<T>::pop(){
    return m_list -> removeBack();
}

template <typename T>
char ListStack<T>::peek(){
    return m_list -> get(m_list -> size() - 1);
}

#endif
