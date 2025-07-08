// #include <iostream>
// #include "rectangle.h"

// using namespace std;

// int main(){ //no arguments means no aruguments can be passed.
//     //stack
//     Rectangle rect1(5, 3);
    
//     cout << "Width: " <<rect1.getWidth() << endl;
//     cout << "Height: " <<rect1.getHeight() << endl;

//     rect1.print();

//     rect1.setHeight(6);

//     rect1.print();

//     //heap 
    
//     Rectangle* rect2 = new Rectangle(5,3);
//     rect2->setHeight(6); // -> arrow notation is for the pointers. 

//     (*rect2).print();

//     delete rect2;

//     Rectangle tempR(1,2);
//     Rectangle* rect3 = &(tempR);

//     rect3->print();
//     (*rect3).print();
//     tempR.print();

//     //delete rect3 is not allowed
//     Rectangle (1,2) + Rectangle(3,4);

//     return 0;
// }