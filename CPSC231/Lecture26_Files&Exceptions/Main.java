
import java.util.Scanner;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.io.FileWriter;
import java.io.File;

public class Main {
  public static void main(String[] args) {

    Scanner scnr = new Scanner(System.in);

    // try/ catch syntax
    // EXAMPLE 1
    while (true){
      try{
        System.out.print("Numerator: ");
        int numerator = scnr.nextInt();
        System.out.print("Denominator: ");
        int denominator = scnr.nextInt();
        int division;
        // What could go wrong here?
        division = numerator / denominator;
        System.out.priintln("Division: " + division);
        break; //the division was carried out 
      } catch (ArithmeticException e) {
        System.out.println("Cannot divide by zero!");
      }
    }

    System.out.println("Division: " + division);



    
    // EXAMPLE 2
    int[] array = { 1, 2, 3, 4, 5 };
    System.out.print("Index: ");
    int index = scnr.nextInt();
    try { // What could go wrong here?
      System.out.println("Value at index " + index + " is " + array[index]);
    } catch (ArrayIndexOutOfBoundsException e) {
      System.out.println("Index out of bounds!");
      System.out.println("You tried to access index " + index + " it is out of bounds, I will assume          you said 0");
      System.out.println("Value at index 0 is " + array[0]);
    }

    // OPENING FILES TO READ AND WRITE
    /*
     * Trying to write out to a file without
     * using exception handling!
     * leads to a syntax error - unable to compile bc IOExceptions must be handles
     * - if something can lead to an IOException you must put that code in a
     * try/catch
     * 
     * MainFiles.java:25: error: unreported exception IOException; must be caught or
     * declared to be thrown
     * PrintWriter pw = new PrintWriter(new FileWriter("cpsc231test.txt")); ^
     */

    // // formatted output to soemthing --> FileWriter
    // // create print writer ob to help up print to file
    // PrintWriter pw = new PrintWriter(new FileWriter("cpsc231test.txt"));
    // // opening a connection to a file called cpsc231test.txt
    // pw.println("hi");
    // pw.println("this is text");
    // pw.println("coming from my program!");

    // // CLOSE FILE
    // // what could happen if we forget to close the file?
    // pw.close();

    /*
     * WRITING TO FILE CORRECTLY
     instead of write mode:
     //if the file does not exist, Java will create it for you
     // if the file does exist, Java will overwrite it
     */

    try {
      PrintWriter pw = new PrintWriter(new FileWriter("CPSC231_Test.txt"));
      pw.println("hi");
      pw.println("this is text");
      pw.println("coming from my program!");
      pw.close();
    } catch (IOException ioe) {
      System.err.println("couldn't output to file!");
      ioe.printStackTrace();
    }

    /*
     * APPENDING TO FILE CORRECTLY
     * instead of overwriting contents like with Write mode, we will
     * add/ append the new text at the end of the file
     * 
     */

    try {
      PrintWriter pw = new PrintWriter(new FileWriter("CPSC231_Test.txt", true)); //true makes this connection append mode instead of write mode:
      //if the file does not exist, Java will create it for you
      // if the file does not exist, Java will not overwrite it. 
      pw.println("hi");
      pw.println("this is text");
      pw.println("coming from my program!");
      pw.close();
    } catch (IOException ioe) {
      System.err.println("couldn't output to file!");
      ioe.printStackTrace();
    }

    /*
     * READING FROM FILE CORRECTLY
     */
    try {
      BufferedReader br = new BufferedReader(new FileReader("test.txt"));
      String contents = "";
      String line = "";
      // read thru each line of test.txt and add it to "contents"
      while ((line = br.readLine()) != null) { // while there is still a next line
        System.out.println("Content: " + line);
        contents += line;
      }
      br.close();
    } catch (FileNotFoundException fnfe) {
      System.err.println("oh-oh looks like that file doesn't exist. Please check your path.");
      fnfe.printStackTrace();
    } catch (IOException ioe) {
      System.err.println("something went wrong with your file!");
      ioe.printStackTrace();
    }

    /*
     * READING FROM FILE CORRECTLY WITH SCANNER
     */
    Scanner scanner = null;
    try {
      scanner = new Scanner(new File("test2.txt"));
      while (scanner.hasNext()) { // while there is a next line in the file
        System.out.println("Content Scanner:" + scanner.nextLine());

      }
    } catch (FileNotFoundException fnfe) {
      System.err.println("oh-oh looks like that file doesn't exist. Please check your path.");
      fnfe.printStackTrace();
    } finally {
      if (scanner != null) {
        System.out.println("CLOSING FILE");
        scanner.close();
      }
    }

  }

}