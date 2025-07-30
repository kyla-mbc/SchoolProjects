//Three of the most common consonants of the English language are R, S and T. 
// Write a program that gets a string as input from the user and prints the number of times 
// these letters occur (in total) in the string. Be sure to account for case.


// import java.util.Scanner;

// public class Exam1 {
//     public static void main(String[] args) {
//         int letterR = 0;
//         int letterS = 0;
//         int letterT = 0;

//         Scanner userInput = new Scanner(System.in);
//         System.out.println("Give me a string: ");
//         String name = userInput.nextLine();

//         for (int i = 0; i < name.length(); i++) {
//             char currentChar = Character.toLowerCase(name.charAt(i));
//             if (currentChar == 'r') {
//                 letterR += 1;
//             } else if (currentChar == 's') {
//                 letterS += 1;
//             } else if (currentChar == 't') {
//                 letterT += 1;
//             }
//         }

//         System.out.println("No. of R: " + letterR + " Number of S: " + letterS + " Number of T: " + letterT);
//     }
// }


//Write a program that gets a string as input from the user and creates a string of every other character from the string.


// import java.util.Scanner;
// public class Exam1{
//     public static void main (String[] args){
//         Scanner scnr= new Scanner(System.in);
//         System.out.println("Input String Here: ");
//         String input = scnr.next();

//         String newString = "";

//         for (int i = 0; i < input.length(); i += 2){
//             newString += input.charAt(i);
//         }

//         System.out.println("New String: " + newString);
//     }

// }

public class CallPerson {
   public static void main(String [] args) {
      String aFirstName;
      String anotherFirstName;
      String aLastName;
      String anotherLastName;

      aFirstName = "Sam";
      anotherFirstName = "Bob";
      aLastName = "Stark";
      anotherLastName = "Banner";

      Person person1 = new Person();
      Person person2 = new Person();
      
      person1.setLastName(aLastName);
      person2.setLastName(anotherLastName);
      person1.setFirstName(aFirstName);
      person2.setFirstName(anotherFirstName);

      System.out.println("You are " + person1.getFullName());
      System.out.println("I am " + person2.getFullName());
   }
}
