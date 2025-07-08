/**JavaDoc Comments:
 * This is the ChipotleDriver class which sets up member variables, constructors, and methods to be used with the other public classes.  
 * This class was created to assist with the BurritoOrder and Burrito classes.
 * @author Kyla Monique Cabrera
 * @see BurritoOrder
 * @see Burrito
 */

public class ChipotleDriver{
    /**
     * The main method where the program starts execution with parts of the Burrito and BurritoOrder classes. 
     * @param args The command-line arguments.
     */
    public static void main (String[] args){
        /** Creates a new Burrito object variable with the properties of a default burrito. */
        Burrito defaultBurrito = new Burrito(); 
        
        /** Creates a new Burrito object variable that stores a new kind of burrito with different properties.  
         * VeggieBurrito: regular, veggie, white rice, pinto beans, guacamole, lettuce, tomatillo 
         */ 
        Burrito veggieBurrito = new Burrito("Regular", "Veggie", "White", "Pinto", true, true, false, false, true);
       
        /** Creates a new Burrito object variable that stores a copy of an already existent burrito, in this case a veggie burrito.  */
        Burrito veggieBurrito2 = new Burrito(veggieBurrito);

        /** Creates a new Burrito object variable that stores a copy of an already existent burrito, in this case a default burrito.  */
        Burrito  defaultBurrito2 = new Burrito(defaultBurrito);

        /** Creates a new BurritoOrder object variable that can store up to 3 burrito inputs. */
        BurritoOrder order = new BurritoOrder(3);

        /** Adds default burrito to order. */
        System.out.println(order.addBurrito(defaultBurrito));

        /** Adds veggie burrito to order. */
        System.out.println(order.addBurrito(veggieBurrito));

        /** Adds veggie burrito copy to order.  */
        System.out.println(order.addBurrito(veggieBurrito2));

        /** Adds default burrito copy to order, but burrito has reached its maximum capacity, so it will not be added. */
        System.out.println(order.addBurrito(defaultBurrito2));

        /** Checks if veggieBurrito and veggieBurrito2 are the same. They are! */
        System.out.print("Are veggieBurrito and veggieBurrito2 the same? ");
        System.out.println(veggieBurrito.equals(veggieBurrito2));
        /** Checks if veggieBurrito and veggieBurrito2 are the same. They are not! */
        System.out.print("Are veggieBurrito and defaultBurrito the same? ");
        System.out.println(veggieBurrito.equals(defaultBurrito));

        // Should call order’s toString methods
        System.out.println(order);
        
    }
}




