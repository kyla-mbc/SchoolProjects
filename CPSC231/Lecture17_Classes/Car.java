/*
 * what are javadocs?
 *   an easy way to create documentation for your java code 
 * what is documentation?
 *   explanations of code, how to use methods in a class, etc. 
 * 
 * special tags:
 *  @see links other classes to this javadoc 
 *  @author 
 *  @version 
 *  @param 
 *  @return 
 */


 /**
  * This is a JavaDoc comment
  * This is the Car class that is used to represent a car for CPSC231
  * The Car class is related to the person class. 
  * Explain what the Car class is:
  * a class to create object representations of a 4-wheel vehicle 
  * This is the class for 
  * 
  * @see Person
  * @see Car
  * 
  * @author Kyla 
  * @version 1.5
  *
  */
public class Car {
  // member variables
  /** An integer representing the year that the car was manufactured */
  private int m_year;
  /** A string storing the make of the car, a.k.a. brand of the car */
  private String m_make;
  /** A string storing the the model name of the Car */
  private String m_model;
  /** A double storing the miles per gallon for the Car */
  private double m_mpg;
  /** A int storing the vin number, 
   * guaranteed to be unique unless you create a deep or shallow copy of a Car 
   * It is calculated using the generateVin() @see generateVin() */
  private int m_vin; // we will generate vin, it will not be provided
  /** the owner of the vehicle, a Person object */
  private Person m_owner; // declare member variable 
  
  // static attributes
  /*
   * STATIC: belongs to the class itself not a specific instance 
   */
  private static int m_countCars = 0; // keeps track of how many car objects we've created
	
  /*
   * CONSTRUCTORS !!!
   * like methods but:
   * - same name as class
   * - no return type
  /** A method to generate a unique VIN*/
  private int generateVIN(){
    return 100000 + numCarsCreated;
  }

  /**
   * Calculates a unique identifier for each Car created
   * guaranteed to be unique unless there are copies of a Car 
   * used in every constructor that is not a copy constructor 
   * @return a unique integer based on the number of cars created thus far in the application
   */
  private int calculateVIN(){
    return 100000 + (m_countCars*21); // 1st car we create will have m_vin = 100021, 2nd vin = 100042
  } 

    /** DEFAULT CONSTRUCTOR, sets attributes to dummy values  */
  public Car() {
    m_year = -1;
    m_make = "Unknown";
    m_model = "Unknown";
    m_mpg = 0.0;
    ++ m_countCars; // increment every time we create a new car 
    m_vin = calculateVIN();

    m_owner = new Person();
		
  }
 /**
  * OVERLOAD CONSTRUCTOR
  * @param make 
  * @param model
  */
  public Car(String make, String model) {
    m_year = -1;
    m_make = make;
    m_model = model;
    m_mpg = 0.0;
    ++ m_countCars;
    m_vin = calculateVIN();

    m_owner = new Person();
  }

  // FULLY SPECIFIED CONSTRUCTOR
  /** An Overload constructor
   * @param y an integer to store the year of the car 
   * @param make is a string to store the make of the car 
   * @param model is a string to store the model of the car 
   * @param mpg is a double to store mpg of your car
   * @param owner uses person to store the owner of the car. 
   */
  public Car(int y, String make, String model, double mpg, Person owner) {
    m_year = y;
    m_make = make;
    m_model = model;
    m_mpg = mpg;
    ++ m_countCars;
    m_vin = calculateVIN();
    m_owner = owner;
}

  // COPY CONSTRUCTOR
  /** */
 
  public Car(Car c) {
    m_year = c.m_year;  
    m_make = c.m_make;
    m_model = c.m_model;
    m_mpg = c.m_mpg;
    ++ m_countCars;
    // m_vin = calculateVIN(); // or
    m_vin = c.m_vin;
    // m_owner = c.m_owner;  // shallow copy! 
    m_owner = new Person(c.m_owner); // deep copy 
  }

  /*
   * MUTATORS AND ACCESSORS
   */
  /** To get access to the Car's Make  */
  public String getMake() {
    return m_make;
  }
  /**
   * 
   * @param make
   */
  public void setMake(String make) {
    m_make = make;
  }
  /**
   * 
   * @return
   */
  public double getMPG() {
    return m_mpg;
  }

  public void setMPG(double mpg) {
    m_mpg = mpg;
  }

  
  // toString method to print member variables
  

  public String toString() {
    String s = "";
    s += "Year: " + m_year;
    s += "\nMake: " + m_make;
    s += "\nModel: " + m_model;
    s += "\nMPG: " + m_mpg;
    s += "\nVIN: " + m_vin;

    // s += "\nOwner: " + m_owner.toString();
    // or 
    s += "\nOwner Name: " + m_owner.getName();

    return s;
  }

  // EQUALS METHOD
  /** 
   * A method to compare two object for equality
   * Will return true if they are both Car objects and they share the same make, model, and year attributes. 
   * @param o Any object you want to compare to a Car. 
   * @return true if the objects are both car pbjects and share the same make, model, and year attributes
   * @return false otherwise. 
   */

  public boolean equals(Object obj){ 
    if(obj == this){ // are obj and "this" the same exact object?
      return true;
    }
    // check if obj is NOT a Car
    if (!(obj instanceof Car)){ // if obj is not a car then the two objects cannot be equal
      return false;
    } 
    // obj is a car, type cast obj back into a Car 
    Car c = (Car) obj; 
    // check member variables
    return this.m_vin == c.m_vin;
  }



  // STATIC METHOD: belongs to the class itself, not a specific instance (object)
  // called upon the class and not an instance, e.g. Car.getAmntCarsProduced()
  public static int getAmntCarsProduced(){
    return m_countCars;
  }

}