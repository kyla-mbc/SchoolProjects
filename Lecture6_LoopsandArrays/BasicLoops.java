import java.util.Scanner; 
public class Loops{
    public static void main(String[] args){
    /*
        CHECKING FOR EQUALITY 
            Use == when comparing primitives 
            Use .equals() when comparing anything else (objects) e.g. Strings 
        */
        int a = 3; 
        int b = 3; 
        System.out.println(a == b);
        // System.out.println(a .equals(b)); // NO 

        String name1 = "Elia";
        String name2 = "Elia"; 
        System.out.println(name1 == name2); // checking memory locations/ addresses // true
        System.out.println(name1.equals(name2));  // checking for equality // true

        Scanner scnr = new Scanner (System.in);
        System.out.println("Name: ");
        String name3 = scnr.nextLine(); 
        System.out.println(name1.equals(name3)); // true if user inputs Elia
        System.out.println(name1 == name3); // false always 


        // FOR LOOP 
        /*
            When should we use a for loop?
            - when we know exactly how many times we want to repeat something 
            - iteration!!! 
                - going through something 
                - looking at every element of a collection e.g. an array, String 
        */
        String s = "hello there how are you?";
        /*
        create an int var called i and initialize to 0, 
        run the code under this loop clause and increment i by 
        1 at the end and stop adding 1/ running the loop once i 
        reaches the length of the string s
        */
        for (int i = 0; i < s.length(); ++i){ 
            System.out.println(s.charAt(i)); 
        }
        // only print out vowels in s 
        System.out.println("only print out vowels in s");

        // 1. we need a value for s 
        // 2. iterate thru string to evaluate each char individually - for loop 
        // 3. check if current letter is a vowel or not - case statement 
        for (int i = 0; i < s.length(); ++i){
            char letter = s.charAt(i); 
            switch (letter){
                case 'a':
                case 'e':
                case 'i':
                case 'o':
                case 'u':
                    System.out.println(i);
                    break;
                default:
                    // nothing - left blank intentionally  
            }
        }

        // 1. control var: int i starting at 0 
        // 2. condition: when i reaches s.length()
        // 3. update control var: ++i; // incrementing i by 1 

        int i = 0; 
        while(i < s.length()){
            char letter = s.charAt(i); 
            switch (letter){
                case 'a':
                case 'e':
                case 'i':
                case 'o':
                case 'u':
                    System.out.println(i);
                    break;
                default:
                    // nothing - left blank intentionally  
            }
            ++i; // same as i += 1, or i = i + 1
        }


        // WHILE LOOPS
            // use when we don't know how many iterations we will need 
            // when we want certain code to run until a condition is no longer met 
        

        /*
        SYNTAX 
        // declare / initialize a control variable to be used in "condition"
        while ( condition ){
            // code to be executed 
            // update control variable / change the state of the control var - or else = infinite loop 
        }
        */

        // ask the user for an integer until they give us an odd number

        System.out.println("give me a number: ");
        // declare and initialize the control var
        int num = scnr.nextInt(); 
        while ( num % 2 == 0 ){ // while it's still even, keep asking for a number 
            System.out.println("give me a number: ");
            // changing state of control var 
            num = scnr.nextInt();
        }

        // DO WHILE LOOP 
        // always runs at least one time 
        int num; 
        do {
            System.out.println("give me a number: ");
            // changing state of control var 
            num = scnr.nextInt();
        } while (num % 2 == 0);

		
    }
}