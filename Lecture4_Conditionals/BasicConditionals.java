import java.util.Scanner;
public class BasicConditionals{
    public static void main (String[] args){
        /*
        *CONDITIONALS - IF STATEMENTS
        *Execute different blocks of code depending on different conditions
        *python:if-elif-else
        *java:if-else if-else
        *Syntax:
        *if (condition1){
            // do this if condition 1 is true
        *}else (condition2){
            // do this if condition 2 is true
        *}else if (condition3){
            // do this if condition 3 is true
        *else
            // do this if none of the code is true
        }
        */
        
        Scanner sin = new Scanner(System.in);
        System.out.println("What is your age?");
        int userAge = sin.nextInt();

        if (userAge > 21){
            System.out.println("Your best days are over");
        } else if (userAge < 21);
            System.out.println("You are no fun yet!");
        } else{
            System.out.println("yay! we party now!");
    }       
}