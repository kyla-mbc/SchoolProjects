public class MethodsIntro {
    // void method vs. a method that returns a value 
    // methods to calculate the GPA based on 3 grade points

    public static void printGPA (double grade1, double grade2, double grade3){
        double gpa = (grade1 + grade2 + grade3) / 3;
        System.out.println("The GPA is: " + gpa);
    }

    public static double returnGPA (double grade1, double grade2, double grade3){
        double gpa = (grade1 + grade2 + grade3) / 3;
        return gpa;
    }

    // EXERCISE WILL BE POSTED AFTER CLASS 


    public static void main(String[] args) {
        // calling a void method vs non-void method
        // calling a void method:
        printGPA(3.4, 2.8, 4.0);
        // does not get saved, just printing 
        // cannot do something like: 
        // System.out.println("The GPA is: " + printGPA(2,4,2));

        // calling a non-void method (returns something):
        // if we just call it like our void method, what will happen?
        returnGPA(3.4, 2.8, 4.0);

        // print the results of a non-void method:
        System.out.println("The GPA is: " + returnGPA(3.4, 2.8, 4.0));

        // if the method is void, we cannot use the values it calculated later!
    }
}