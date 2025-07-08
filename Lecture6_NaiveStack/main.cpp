#include "NaiveCharStack.h"
#include <iostream>
using namespace std;

int main(){
    NaiveCharStack myStack(10);
    myStack.push('h');
    myStack.push('e');
    myStack.push('l');
    myStack.push('l');
    myStack.push('o');

    cout << myStack.actualSize() << endl << endl;
    cout << myStack.peek() << endl << endl;; //o, Last in is first out. LIFO

    //empty out the stack
    while(!myStack.isEmpty()){
        cout << myStack.pop() << endl;
    }
    
    cout << endl;
    cout << myStack.actualSize() << endl;
    cout << endl;
    
    return 0;
}