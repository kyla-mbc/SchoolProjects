import java.util.ArrayList;
import java.util.LinkList;

// import java.util.* // Bad programming practice since it imports ALL libraries inside of java.util, this takes up too much irrelevant space. 

public class BetterArrayDriver {
    public static void main(String[] args) {
        BetterArray myBetterArray = new BetterArray(3);
        System.out.println("Current Size: " + myBetterArray.getCurrentSize()); // 0
        System.out.println("Max Size: " + myBetterArray.getMaxSize()); // 3

        myBetterArray.add("Hello");
        myBetterArray.add("Hi");
        myBetterArray.add("Howdy");
        System.out.println(myBetterArray);
        System.out.println("Current Size: " + myBetterArray.getCurrentSize()); //3
        System.out.println("Max Size: " + myBetterArray.getMaxSize()); //3


        myBetterArray.add("Will this get added?");
        System.out.println(myBetterArray);
        System.out.println("Current Size: " + myBetterArray.getCurrentSize()); //4
        System.out.println("Max Size: " + myBetterArray.getMaxSize()); // 6

        /**
         * the BetterArray class we created is just like Java's ArrayList
         * an ArrayList is a java object that is built upon an array
         * it has a nice interface for us to work with. 
         * 1. can only hold objects (no primitives)
         * 2. should only hold one type of object at a time. 
         * 
         * ArrayLists have te same benefits and drawbacks as regular arrays.
         */

        //copy this into an ArrayList: BetterArray myBetterArray = new BetterArray(3);
        ArrayList<String> myArrayList = new ArrayList<String>(3);
        myArrayList.add("Hi!");
        myArrayList.add("This is an Array List");
        myArrayList.add("It works a lot like our Better Array object");

        myArrayList.add("Will this actually get added?");
        //will get added! the array inside of the ArrayList object will "grow" just like our BetterArray did.
    
        System.out.println(myArrayList);
        System.out.println(myArrayList.get(2)); //get and print index 2 of myArrayList
        System.out.println(myArrayList.size());

        /**ArrayLists can only hold objects (NO PRIMITIVES)
         * Wrapper Classes for primitives will allow us to represent all primitves as objects
         * so that we can store them in the heap/in collections such as out ArrayList
         * 
         * int -> Integer()
         * float -> Float()
         * bool -> Boolean()
         * ... wrapper class names are the same as the primitive fully spelled out and with a capital 1st letter.
         * Array lists already have an allocated amount of stuff to be stored. -- This is why we have a number in the parentheses representing the size of the array. 
         */

        // ArrayList<int> intAL = new ArrayList<int>(); // ERROR: cannot hold primitves in the ArrayList
        ArrayList<Integer> intAL = new ArrayList<Integer>();
        intAL.add(5);

        int x = 82934
        intAL.add(x); //allowed due to AUTOBOXING (automatically turning a primitve into its wrapper type)

        int y = intAL.get(0); //allowed due to AUTOUNBOXING (automatically turning a primitve into its primitive type)

        // create an array and arrayList of chars
        char[] charArr = new char[100]; //an array that can fit 100 chars

        //need to use Character (the wrapper class) and not char because ArrayLists can only hold objects (no primitives)
        ArrayList<Character> charAL = new ArrayList<Character>(100); //initial capacity argument is optional. In this case it is 100. 

        // a linked list of characters
        /*
         * LINKED Lists: 
         * perfectly dynamically sized lists -- we do not need to give an initial size in the parentheses.
         * the list will grow and shrink as we add and remove elements. 
         * Linked lists are often represented with arrows and memory locations will be allocated after we add stuff in. 
         */
        LinkList<Character> charLL = new LinkedList<Character>(); //linked list is in the same format as array lists. Remember to import import java.util.LinkList;

        charAL.add('A');
        charLL.add('A');

        charAL.add('B');
        charLL.add('B');

        charAL.add('C');
        charLL.add('C');

        System.out.println(charAL.get(1));
        System.out.println(charLL.get(1));    

        System.out.println(charAL);
        System.out.println(charLL);

        System.out.println(charAL.size());
        System.out.println(charLL.size());   
        
        //We use an array list when we already know the capacity of what we are storing, but a linked list is used when we 
}