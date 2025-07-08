import java.util.*;
public class BankAccountDriver {
    public static void main (String[] args){
        BankAccount x = new BankAccount("Elia", "Eiroa", 1000);
        x.addTransaction("Starbucks", 10.50);
        x.addTransaction("Lululemon", 218.99);
        x.addTransaction("Netflix", 15.0);
        System.out.println(x);

        BankAccount y = new BankAccount(x); // deep copy of x
        System.out.println(y);

        System.out.println("x.equals(y): " + x.equals(y)); // true 

        BankAccount z = new BankAccount("Stephanie", "Alvarez", 4500); 
        z.addTransaction("Equinox", 219.0);
        z.addTransaction("Chipotle", 13.90);
        z.addTransaction("Equinox", 219.0);
        z.addTransaction("Equinox", 219.0);
        System.out.println(z);

        HashMap<String, Double> payeeTotals = z.getPayeeTotals();
        System.out.println("Payee Totals for account z: \n" + payeeTotals); 

        System.out.println("x.equals(z): " + x.equals(z)); // false 
   
    }
}