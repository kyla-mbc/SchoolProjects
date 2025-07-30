public class Student{
  /*
  Blueprint to create a student object
  */
  
  /*
  MEMBER VARIABLES / ATTRIBUTES
- usually all attributes (aka member variables) will be private
- private attributes will only be made available outside of the class
    with accessors and will only be able to change through mutators 
- use m_ pre-fix to let us know this is a member var (just a naming convention)
  */
  /**A string that stores name of the student. */
  private String m_name;
  /**An int that stores the age of the student. */
  private int m_age;
  /**An int that stores the student id of the student. */
  private int m_sid;
  /**A string that stores the grade level of the student. */
  private String m_level;
  
  /*
  CONSTRUCTORS
  - Tell java what to do when a new instance of this class is created
  - same as a method but:
      - same name as the class
      - no return type
  */
  
  // DEFAULT CONSTRUCTOR
  // what should the values be set to if we are not given any information at instantiation? 
  public Student(){
    m_name = "";
    m_age = -1;
    m_sid = 0;
    m_level = "";
  }
  // 1st OVERLOADED CONSTRUCTOR: FULLY SPECIFIED CONSTRUCTOR
// in mmain this will be called by doing:
// Student s1 = new Student ("Elia", 26,12345,"Senior");

  // allows us to give values to every attribute 
  public Student(String n, int a, int id, String l){
    m_name = n;
    m_age = a;
    m_sid = id;
    m_level = l;
  }

  // 2nd OVERLOADED CONSTRUCTORS
  // we can give values to some other combination of attributes
  // we can have more overloaded constructors if we want

  public Student(String n, int a){
    m_name = n;
    m_age = a;
    m_sid = 0;
    m_level = "";
  }
  
  /*
  ACCESSORS AND MUTATORS
  - allow other classes to interact w/ private member variables from this class

  ACCESSORS:
    - same return type as the attribute they are returning
    - they will have a get prefix

  MUTATORS:
    - changing the value of an attribute
    - have a void return type (they don't return anything)
    - will take in a parameter of the same type as the member var they set
    - they will have a set prefix
  */

  // ACCESSORS / GETTERS
  public String getName(){ // accessor / getter for m_name 
    return m_name;
  }
  public int getAge(){
    return m_age;
  }
  public int getSID(){
    return m_sid;
  }
  public String getLevel(){
    return m_level;
  }

  // MUTATORS / SETTERS
  public void setName(String n){
    m_name = n;
  }
  public void setAge(int a){
    m_age = a;
  }
  // no mutator for sid because that's dangerous!
  public void setLevel(String l){
    m_level = l;
  }
  

  /*
  toString METHOD
  - to pretty print attributes of this class
  - always has the name toString
  */
  public String toString(){
    String s = "";
    s += "Name: " + m_name+ "\n";
    s += "Age: " + m_age+ "\n";
    s += "Student ID: " + m_sid+ "\n";
    s += "Level: " + m_level+ "\n";
    return s;
  }

  /*
  ANY OTHER METHODS YOU WANT
  */
  
 /*
    ADDED WITH CLASSES PT. 2: LECTURE 13
    */
    
    // COPY CONSTRUCTOR
    // always follows the same set-up 
    // put it at the top with the other constructors 
    // will take in an already existing object and will
    // copy all of its values into another object

    public Student(Student studentToCopy){ //studentToCopy is the pre-existing student we want to copy
        m_name = studentToCopy.m_name;
        m_age = studentToCopy.m_age;
        m_sid = studentToCopy.m_sid;
        m_level = studentToCopy.m_level;
    
  
    /*
    ACCESSORS AND MUTATORS
    - allow other classes to interact w/ private member variables from this class
  
    ACCESSORS:
      - same return type as the attribute they are returning
      - they will have a get prefix
  
    MUTATORS:
      - changing the value of an attribute
      - have a void return type (they don't return anything)
      - will take in a parameter of the same type as the member var they set
      - they will have a set prefix
    */

    public String getName(){
        return m_name;
    }

    public int getAge(){
        return m_age;
    }

    public int getSID(){
        return m_sid;
    }

    public String getLevel(){
        return m_level;
    }

    // public int getSSN(){
    //     return m_socialSecurityNumber;
    // } // i want to keep SSN private so I will not create a SSN getter/ accessor
  
    public void setName(String newName){
        m_name = newName;
    }  

    public void setAge(int newAge){
        m_age = newAge;
    }  

    public void setLevel(String newLevel){
        m_level = newLevel;
    }  
    // I only create setters/ mutators for things that I want to be able to change 
  
  
    /*
    toString METHOD
    - to pretty print attributes of this class
    - always has the name toString
    */
    
    public String toString(){
        String s = "";
        s += "Name: " + m_name + "\n";
        s += "Age: " + m_age + "\n";
        s += "Level: " + m_level + "\n";
        s += "Student ID: " + m_sid + "\n";
        return s;
    }
  
// EQUALS METHOD 
  public boolean equals(Object o){ // why not take in Student s? we want to make sure we can compare other types of objects without the program crashing 
    // check if they share a memory location first 
    if (this == o){
        return true;
    }

    // check whether o is an instance of Student 
    if ( ! (o instanceof Student)){ // if o is not a Student 
        return false;
    }

    // the rest of the code only runs if o is a Student 
    // type cast o into a Student 
    Student s = (Student) o; // refer to o as a Student again instead of a general Object 

    // now we can check if the member variables are equal 
    // for students it makes sense to just check ssn or student id 
    return ((this.m_sid == s.m_sid) && (this.m_name.equals(s.m_name))); 
}
    }
  
}