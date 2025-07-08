public class Recursion {

  /////////////////////////////////////////////////////////////////
  // sayHello Example /////////////////////////////////////////////
  /////////////////////////////////////////////////////////////////
  /*
  a recursive methid is a method that calls upon itself. 
  a recursive method should always have a BASE CASE
  a base case is what tells java when to stop the recursive calls
  */

  public static void sayHello(int times){
    // // print hello times times
    // // iterative solution
    // for (int i = 0; i < times; ++i){
    //   System.out.println("Hello");
    // }
    // } 

    //recursive solution 
    if (times == 0){
      return;
    }
    System.out.println("Hello");
    --times;
    sayHello(times); // recursive call
  }


  /////////////////////////////////////////////////////////////////
  // factorial Example ////////////////////////////////////////////
  /////////////////////////////////////////////////////////////////

  public static int itFact(int n) {
    /*
      * FACTORIAL - ITERATIVE VERSION
      * 5! = 5*4*3*2*1
      * n! = n * (n-1) * (n-2)*...*1
      * 
      */

     int result = 1;
     for (;n > 0; --n){
      result *= n; // same as result = result * n
     }
    return result;
  }

  public static int recFact(int n) {
    /*
      * FACTORIAL - RECURSIVE VERSION
      * 5! = 5*4*3*2*1
      * n! = n * (n-1) * (n-2)*...*1
      * n! = n * (n-1)!
      * only works if we have a base case. 
      * usually slower that iterative problems
      * BASE CASE: n = 1, that's when we know we are done calculating the solution. 
      */

    int result = 0;
    // base case
    if (n == 0){
      result = 1;
    } else {
      result = n * recFact(n-1);
    }
    return result;

  }

  /////////////////////////////////////////////////////////////////
  // Fibonacci Example ////////////////////////////////////////////
  /////////////////////////////////////////////////////////////////
  public static long itFib(int n) {
      if (n <= 1) {
        return n;
      }
      int fib = 1;
      int prevFib = 1;
      for (int i = 2; i < n; i++) {
        int temp = fib;
        fib += prevFib;
        prevFib = temp;
      }
      return fib;
    }
  
  public static long recFib(int n){
    // RECURSIVE VERSION
    // base case: fib(0) = 0, fib(1) = 1
    if (n <= 1){
      return n;
    }
    return (recFib(n-1) + recFib(n-2));
  } 

  // recursive solution with memoization
  // memoization saves the work you have already calculated instead of calculating it again. 
  public static long recFibMemo(int n){
    // RECURSIVE VERSION
    // base case: given that fib(0) = 0 and fib(1) = 1
    if (n <= 1){
      return n;
    }
    if (fibCache[n] != 0){
      return fibCache[n];
    }
    long nthFibNum = recFibMemo(n-1, fibCache) + recFibMemo(n-2, fibCache);
    fibCache[n] = nthFibNum;
    return nthFibNum;
  }


  public static void main(String[] args) {
    sayHello(5);
    System.out.println(Recursion.itFib(45));
    System.out.println(recFibMemo(45, fibCache))
    System.out.println(Recursion.recFib(45));
    long[] fibCache = new long[100];

  }
}
