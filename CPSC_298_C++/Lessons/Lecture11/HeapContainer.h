// #include <iostream>

// using namespace std;

// #ifndef HEAPCONTAINER_H
// #define HEAPCONTAINER_H

// template <typename T>
// class HeapContainer{
//     public:
//         HeapContainer();
//         HeapContainer(T obj);
//         ~HeapContainer();

//         void set(T obj);
//         T* get();

//         template <typename U>
//         friend ostream& operator <<(ostream& os, const HeapContainer<U>& obj); // To override "<<"

//         /*
//         cout << HeapContainer<int>(5); // 0x198246
//         */
//         HeapContainer<T> operator +(const HeapContainer<T>& obj) const; //addition

//     private:
//         T* ptr;
// };

// //template classes always need implementation in the same file
// template <typename T>
// HeapContainer<T>::HeapContainer(){
//     ptr = nullptr;
// }

// template <typename T>
// HeapContainer<T>::HeapContainer(T obj){
//     ptr = new T(obj); //declaring it on the heap
// }

// //destructor
// template <typename T>
// HeapContainer<T>::~HeapContainer(){
//     delete ptr;
// }

// template <typename T>
// void HeapContainer<T>::set(T obj){
//     delete ptr;
//     ptr = new T(obj);
// }

// /*
// a = HeapContainer(5)
//     ------> new int(5);
// a = HeapContainer(8)

// */

// template <typename T>
// T* HeapContainer<T>::get(){
//     return ptr;
// }

// template <typename U>
// ostream& operator<<(ostream& os, const HeapContainer<U>& obj){
//     os << *(obj.ptr);
//     /*
//     cout << obj
//     cout is the ostream
//     */
// }

// template <typename T>
// HeapContainer<T> HeapContainer<T>::operator+(const HeapContainer<T>& obj) const{
//     T sum = *(this -> ptr) + *(obj.ptr);
//     return HeapContainer<T> (sum);
// }


// #endif