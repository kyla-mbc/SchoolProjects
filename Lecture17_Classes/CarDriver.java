public class CarDriver {
    public static void main(String[] args) {
        Person p1 = new Person("Elia");
        Person p2 = new Person("Erik");
        //   public Car(int y, String make, String model, double mpg, Person owner) {
    
        Car c1 = new Car(2022, "Tesla" , "Y", 0.0, p1 );
        Car c2 = new Car(2003, "Honda", "Civic", 37.2, p2);
        Car c3 = new Car(c2); // deep copy, uses new keyword 
        
        System.out.println("CAR 1: ");
        System.out.println(c1);
        System.out.println("CAR 2: ");
        System.out.println(c2);
        System.out.println("CAR 3: ");
        System.out.println(c3);
        
        p2.setName("Lola"); // from Erik to Lola

        System.out.println("CAR 1: ");
        System.out.println(c1);
        System.out.println("CAR 2: ");
        System.out.println(c2);
        System.out.println("CAR 3: ");
        System.out.println(c3);
    }
}