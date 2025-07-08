public class MethodsExercise{
    // Method to calculate the area of a circle
    public static double calculateArea(double radius){
        double area = Math.PI * (radius * radius);
        return area;
    }

    // Method to calculate the area of a triangle
    public static double calculateArea(double base, double height){
        double area = 1/2.0 * (base * height);
        return area;
    }

		// To do after finishing question 3: Method to calculate the area of a rectangle 
    // public static double calculateArea(double length, double width){
    //     double area = length * width;
    //     return area; 
    // }

    // main method, mostly finished, just uncomment the last line when specified (for question 5)
    public static void main (String[] args){
        System.out.println("The area of the circle is: " + calculateArea(10));
        System.out.println("The area of the triangle is: " + calculateArea(5, 3)); // height, width

        // uncomment the following line for the answer to question 5 
        // System.out.println("The area of the rectangle is: " + calculateArea(4, 2)); // length,  width 
    }
}