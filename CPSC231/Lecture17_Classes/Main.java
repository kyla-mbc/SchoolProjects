public class Main {
  public static void main(String[] args) {

    // create some cars
    Car c1 = new Car(1985, "Ferrari", "308QV", 11.5);
    Car c1ShallowCopy = c1;
    c1.setMPG(20);
    System.out.println(c1);
    System.out.println(c1ShallowCopy);
    // if we want to create deep copies, we must have a copy constructor. 
    Car c1DeepCopy = new Car(c1); // make a deep copy of c1 called c1DeepCopy
    c1.getAmountCarsCreated();
    c1DeepCopy.getAmountCarsCreated();

    System.out.println(c1.getAmountCarsCreated());
    System.out.println(c1DeepCopy.getAmountCarsCreated());
    System.out.println(c1.getMPG());
    System.out.println(c1DeepCopy.getMPG());
  }
}