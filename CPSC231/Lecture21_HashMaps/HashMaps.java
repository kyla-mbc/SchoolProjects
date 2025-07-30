import java.util.LinkedList;
import java.util.ArrayList;
import java.util.HashMap;

public class HashMaps{
    public static main void (String [] args){
        //create an array list of Strings
        ArrayList<String> al = new ArrayList<String>();
        // create a linked list of whole numbers
        LinkedList<Integer> ll = new LinkedList<Integer>(); // make sure to use integer and not int

        al.add("Hi!");
        al.add("This");
        al.add("is");
        al.add("Kyla!!!");

        System.out.println(al.get(3)); //Kyla!!!

        // print each element and its index number
        // enhanced for loop:
        int index = 0;
        for (String element: al){
            System.out.println(index + ":\t" + element);
            ++index;
        }

        //regular for loop:
        for (int i  = 0; i < al.size(); i++){
            System.out.println(i + ":\t" + element);
        }

        /*
        * HASH MAP SYNTAX
        */
        HashMap<String, Ingteger> salaries = new HashMap<String, Integer>();
        salaries.put("Mark", 100000);
        salaries.put("Andrew", 45000);
        salaries.put("Stephaine", 250000);
        salaries.put("Erik", 98000);

        //get a value associated to a key?
        System.out.println(salaries.get("Stephanie"));
        System.out.println(salaries.get(2)); // error? No Java will just retun null.

        System.out.println(salaries.get("Elia")); // error? No Java will just retun null.

        //iterate thru the hm?
        for (String key: salaries.keySet()){
            System.out.println(key + "\t" + salarioes.get(key));
        }

        for (Integer val: salaries.values()){
            
        }   




    }
}