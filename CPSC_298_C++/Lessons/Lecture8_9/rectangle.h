// // Header File


// #ifndef RECTANGLE_H //header guards protect code from crashing if there are a lot of the same imports. 
// #define RECTANGLE_H

// class Rectangle{
//     private: //make member variables private so that we can control them within functions. This includes keeping w and h positive.
//         double width; // member variables
//         double height; // member variables
//     public:
//         Rectangle(double width, double height); //Constructor 
//         ~Rectangle(); //Destructor --> this helps with 'delete object;' //no arguments inside 

//         // Member functions 
//         double getWidth(); //getter (a.k.a accessor)
//         double getHeight();

//         void setWidth(double width); // lets you change the initial values, but it does not return anything and so it is void. 
//         void setHeight(double height);

//         double area(); // we do not need to pass in values since we already have variables. 
//         double perimeter();

//         void print();


//     };


// #endif