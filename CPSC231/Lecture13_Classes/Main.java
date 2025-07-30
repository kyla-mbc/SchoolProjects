public class Main {
  // DRIVER CLASS
  public static void main(String[] args) {
    // main class w main method
    // CREATE INSTANCES OF CLASS STUDENT
    // aka create Student objects
    // className instanceName = new className( anyArgs);
    
   // STUDENT1 Java will use the default CONSTRUCTOR bc we didnt provide any args based on parameters (values) given
    Student s1 = new Student();
    
    // STUDENT2 Java will know to use the 1st OVERLOADED CONSTRUCTOR based on parameters (values) given
    Student s2 = new Student("Kyla", 18, 2445213, "Freshman");

    // STUDENT3 Java will know to use the 2nd OVERLOADED CONSTRUCTOR based on parameters (values) given
    Student s3 = new Student ("Jessica", 95);

    // use the .ageInMonths() method 

    //CREATING COPIES
    Student s2ShallowCopy = s2; // will this use the copy constructor? No, this is a shallow copy
    System.out.println(s2); 
    System.out.println(s2ShallowCopy); // two names, s2 and s2 shallow copy 

    //use the copy constructor
    Student s2DeepCopy = new Student(s2); // DEEP COPY; allocating new memory in the heap to be allocated. 
    System.out.println(s2DeepCopy);

    //.equals()
    System.out.println(s2ShallowCopy); //True, they are the same object
    System.out.println(s2DeepCopy); // False, we wat this to return the same things.
    System.out.println(s2.equals("HELLO")); // we want to make sure this does not break our code.

    s2ShallowCopy.setName("Grace");
    System.out.println(s2);
    System.out.println(s2ShallowCopy);
    System.out.println(s2DeepCopy);



    // use accessors and modifiers (getters and setters)
    System.out.println(s2.getName());
    s2.setName("Dr.EEL");
    System.out.println(s2.getName());

    // use .toString() method implicitly 
    
    System.out.println(s2);
   // same as  
  System.out.println(s2.toString());
    
    
  // create a class to model a car
    // make
    // model 
    // color 
    // hp


  }
}