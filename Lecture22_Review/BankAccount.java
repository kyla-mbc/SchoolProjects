
import java.util.*;

public class BankAccount {
  // int m_accountNo: a unique account number (8 digits long)
  int m_accountNo;
  // double m_balance: the amount of money in the account
  double m_balance;
  // String m_firstName: the first name of the owner of the account
  String m_firstName;
  // String m_lastName: the last name of the owner of the account
  String m_lastName;
  // LinkedList<Transaction> m_transactions: a linked list that holds
  // transactions.
  // a Transaction is a class that has the following member variables:
  // String m_payee;
  // Double m_amount;
  // LocalDate m_date;
  // assume that this Transaction class already exists and has a constructor that
  // takes in a string for
  // the payee and a double for the amount of the transaction. The date is
  // automatically generated.

  LinkedList<Transaction> m_transactions;

  /*
   * OVERLOADED CONSTRUCTOR
   * Create an overloaded constructor that takes in values for the first & last
   * name and
   * the starting balance. Randomly generate an 8-digit long account number. Make
   * sure
   * to also initialize the m_transactions linked list to an empty list.
   */
  public BankAccount(String first, String last, double startingBalance) {

    Random random = new Random();
    // int i = random.nextInt();
    int min = 10000000;
    int max = 99999999;
    int randomNumber = random.nextInt(max - min + 1) + min;

    m_accountNo = randomNumber;

    m_firstName = first;
    m_lastName = last;
    m_balance = startingBalance;

    m_transactions = new LinkedList<Transaction>();

  }

  /*
   * COPY CONSTRUCTOR
   * Create a copy constructor that takes in an existing bank account
   * and creates a deep copy of it. You can assume there is a copy constructor
   * in the Transaction class.
   */
  public BankAccount(BankAccount b) {
    this.m_firstName = b.m_firstName;
    m_lastName = b.m_lastName;
    m_balance = b.m_balance;
    m_accountNo = b.m_accountNo;

    m_transactions = new LinkedList<Transaction>();
    // for (int i = 0; i < b.m_transactions.size(); ++i){
    // Transaction bT = b.m_transactions.get(i);
    // Transaction newT = new Transaction(bt);
    // m_transactions.add(newT);
    // }
    // same as:
    // m_transactions = b.m_transactions; // shallow copy! we need to iterate thru
    // and copy each individually
    for (Transaction t : b.m_transactions) {
      Transaction newT = new Transaction(t);
      m_transactions.add(newT);
    }

  }

  /*
   * ADD TRANSACTION
   * Write a method that takes in a payee and an amount then creates
   * a Transaction with that data and adds it to m_transactions
   * Then, decrease the m_balance as necessary.
   */
  public void addTransaction(String payee, double amount) {
    Transaction newT = new Transaction(payee, amount);
    m_transactions.add(newT);
    m_balance -= amount;

  }

  /*
   * TO STRING METHOD
   * Create a toString method that displays all the information of the bank
   * account
   * including all the transactions. You can assume that the Transaction class
   * has a toString method that displays the payee, amount, and date of the
   * Transaction
   */
  public String toString() {
    String s = "";
    s += "--------------------";
    s += "\n| ACCOUNT DETAILS | \n";
    s += "--------------------\n";
    s += "Account owner: " + m_firstName + " " + m_lastName + "\n";
    s += "Account number: " + m_accountNo + "\n";
    s += "Current balance: " + m_balance + "\n";

    s += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n";
    s += "~~~~~~~~~~~~~~~~~ TRANSACTIONS ~~~~~~~~~~~~~~~~~~\n";
    s += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n";
    for (Transaction t : m_transactions) {
      s += t.toString();
    }
    s += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n";
    return s;
  }

  /*
   * EQUALS METHOD
   * create an equals method that returns true if the object coming in
   * is equal in first name, last name, and account balance and false
   * otherwise.
   */
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }

    if (!(o instanceof BankAccount)) {
      return false;
    }

    BankAccount b = (BankAccount) o;
    return (m_firstName.equals(b.m_firstName)
        && m_lastName.equals(b.m_lastName)
        && m_balance == b.m_balance);
  }

  /*
   * GET PAYEE TOTALS
   * Create a method that returns a HashMap of each unique payee
   * in the Bank Account's transactions and computes the total
   * money paid out to each payee
   * 
   * e.g. if there are the following transactions:
   * Equinox 219.0
   * Chipotle 13.90
   * Equinox 219.0
   * Equinox 219.0
   * Equinox: 657.0
   * Chipotle: 13.9
   */
  public HashMap<String, Double> getPayeeTotals() {
    HashMap<String, Double> payeeTotals = new HashMap<String, Double>();
    for (Transaction t : m_transactions) { // t is each transaction. 
      if (payeeTotals.containsKey(t.getPayee())) { // we have seen the payee before so we add to their balance
        payeeTotals.put(t.getPayee(), payeeTotals.get(t.getPayee()) + t.getAmount());
      } else { // first transaction w payee
        payeeTotals.put(t.getPayee(), t.getAmount());
      }
    }
    return payeeTotals;
  }
}



