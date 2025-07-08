public class BasicArrays {
    public static void main(String[] args) {
        // CREATING AN ARRAY 
        // let's create an array that can hold 5 integers 
        int[] myArr = new int[5]; // create empty array that can hold 5 int; be default all elements =0 at declaration. 
      
        // int len = 20;
        // String [] strArray = new String [len]; // array of strings of length = 20.

        // ITERATING OVER AN ARRAY AND INITIALIZING VALUES 
        // now we can populate the array with, for example, multiples of 5: 
        // we know the array is of length 5 because we created it
        // but we can also get the length with .length -> myArr.length => 5
        for (int i = 0; i < myArr.length; ++i){ // iterate through 
            myArr[i] = 5 * i; // set each spot to a multiple of 5
        }

        // intArray[0] = 5; 
        // intArray[1] = 6; 
        // intArray[2] = 7; // tooooo long, do something better. 


        // INDEXING AN ARRAY
        // we can index the array "myArr" using POSITIVE index numbers 

        // the first element will always be at index 0
        System.out.println(myArr[0]); 

        // how do we know what the last index is? myArr.length
        // but if we use myArr.length we will be out of bounds! 
        // we need to subtract 1
        System.out.println(myArr[myArr.length - 1]); 
        // this will work no matter the size or length of the array! 


        // MODIFYING THE CONTENTS OF AN ARRAY 
        // just like indexing but we = the new value 
        // for example changing the element at index 1 to 1000
        myArr[1] = 1000;
        System.out.println(myArr[1]);

        // ITERATING OVER AN ARRAY AND PRINTING CONTENTS OF AN ARRAY
        // printing the contents of the array WRONG
        System.out.println("printing the variable in hopes of printing contents: "); 
        System.out.println(myArr); // this prints a memory address of where this array is stored
        
        // printing the contents of the array using a regular for loop
        System.out.println("printing the contents of the array using a regular for loop: "); 
        for (int i = 0; i < myArr.length; ++i){ // iterate through 
            System.out.println(myArr[i]); // index the array using i 
        }
        // printing the array contents using enhanced for loop
        System.out.println("printing the array contents using enhanced for loop: "); 
        for (int x: myArr){
            System.out.println(x);
        }


    }
}
