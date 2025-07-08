import java.util.Scanner; // USER INPUT STEP 1: import Scanner 
public class Basic{
    public static void main(String[] args){
        //output hello world to the terminal
        //python: print("hello world")
        //java:
        System.out.println("Hello, World");


        //tell the user hello by their name
        // get user input for their name
        // python: "user_name = input ("What is your name?")"
        
        //java:
        // USER INPUT STEP 2: create Scanner object
        Scanner scnr = new Scanner(System.in);
        // USER INPUT STEP 3: Prompt the user
        System.out.println("What is your name?");
        // USER INPUT STEP 4: get user input and save into a variable
        String userName = scnr.nextLine();
        // display message
        System.out.println("Hello " + userName + " ,you're cute!");


        int age = 18;
        int yearsToRetire = 65 - age;
        System.out.println(yearsToRetire);
    }   
}