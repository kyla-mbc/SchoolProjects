// #include <iostream>
// #include "rectangle.h" //only include header in cpp, but not the other way around. 

// using namespace std;

// //Constructor Definition
// // :: scope resolution operator tells cpp to take from a specific library.
// Rectangle::Rectangle(double width, double height){
//     this->setWidth(width);
//     this->setHeight(height);
// }

// //Destructor Definition
// Rectangle::~Rectangle(){

// }

// double Rectangle::getWidth(){
//     return width;
// }

// double Rectangle::getHeight(){
//     return height;
// }

// void Rectangle::setWidth(double width){
//     if (width < 0){
//         width = - width;
//     }
//     this->width = width; //this->width refers to the member variable
// }

// void Rectangle::setHeight(double height){
//     if (height < 0){
//         height = -height;
//     }
//     this->height = height;
// }

// //area
// double Rectangle::area(){
//     return width * height;
// }

// //perimeter
// double Rectangle::perimeter(){
//     return 2 * (width + height);
// }

// void Rectangle::print(){
//     cout << "The rectangle has dimensions of " << height << "x" << width << endl;
//     double perimeter = this->perimeter(); //Works
//     perimeter = Rectangle::perimeter(); //Works
//     // double perimeter = perimeter(); //DONES NOT WORK
//     cout << "Perimeter: " << perimeter << endl;
//     cout << "Area: " << this->area() << endl;
// }