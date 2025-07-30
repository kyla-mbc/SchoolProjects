#include <iostream>
#include "DblList.h"
#include "ListStack.h"
#include "ListQueue.h"
using namespace std;

int main(){
   
    DblList<int> myList;
    for(int i = 0; i < 10; ++i){
        myList.add(i,i);
    }

    myList.add(5,222);
    myList.addFront(14);
    myList.addBack(28);

    for(int i = 0; i < myList.size(); ++i){
        cout << myList.get(i) << endl;
    }

    cout << "===============" << endl;

    myList.removeFront();
    myList.removeBack();
    myList.remove(5);

    for(int i = 0; i < myList.size(); ++i){
        cout << myList.get(i) << endl;
    }

    

   ListStack<int>* ls = new ListStack<int>();
   ls->push(10);
   ls->push(20);
   ls->push(30);
   cout << ls->size() << endl;
   while(!ls->isEmpty()){
    cout << ls->pop() << endl;
   }
   cout << "Size: " << ls->size() << endl;
   

   ListQueue<int> lq;
   lq.add(10);
   lq.add(20);
   lq.add(30);
      while(!lq.isEmpty()){
    cout << lq.remove() << endl;
   }
   cout << "Size: " << lq.size() << endl;
}