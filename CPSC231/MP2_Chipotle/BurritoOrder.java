/**JavaDoc Comments:
 * This is the Burrito class which represents the type of burrito and its contents as well as its cost.
 * This class was created to assist with the BurritoOrder and ChipotleDriver classes.
 * @author Kyla Monique Cabrera
 * @see Burrito
 * @see ChipotleDriver
 */

public class BurritoOrder {
    /** Private Member Variables: */
    /** Burrito object array that represents the order of the burrito. */
    private Burrito[] m_order;
    /** Integer variable that represents the number of burritos. */
    private int m_numBurritos;
    /** Integer variable that represents the max number of burritos. */
    private int m_numBurritosMax;

    /** 
     * Default Constructor
     * Used to set default values to each member variable.
     */
    public BurritoOrder() {
        /** Each member variable below is being set to something by default. */
        m_order = new Burrito[m_numBurritosMax]; 
        m_order[0] = new Burrito();
        m_numBurritos = 1;
        m_numBurritosMax = 1;
    }

    /** 
     * Overloaded Constructor
     * Used to set each member variable to something. 
     * @param numBurritos represents the number of burritos there are in the order. 
     */
    public BurritoOrder(int numBurritos) {
        m_numBurritos = 0;
        m_numBurritosMax = numBurritos;
        m_order = new Burrito[m_numBurritosMax];
    }

    /**
     * Method that is used to increment the number of burritos there are. 
     * @param b represents the burrito object that will increase in size, esentially adding more burritos to the order. 
     * @return 1 if the burrito is able to be added.
     * @return -1 if the burrito is not able to be added.
     */
    public int addBurrito(Burrito b) {
        if (m_numBurritos < m_numBurritosMax) {
            m_order[m_numBurritos] = b;
            m_numBurritos++;
            return 1; // Success
        } else {
            return -1; // Unsuccessful, array is full
        }
    }

    /**
     * Method that is used to calculate the total cost of every burrito in the order.
     * @return total returns the total cost of every burrito in the order.
     */
    public double calcTotal() {
        double total = 0.0;
        for (int i = 0; i < m_numBurritos; i++) {
            total += m_order[i].calcCost();
        }
        return total;
    }


    /** 
     * Method used to create a printing format string for the total cost of the order as well as the phrase "Order Details".
     * @return s returns the printing format string for use in the main method.
     */
    public String toString() {
        String s = "";
        s += "\nTotal Cost: $" + calcTotal();
        s += "\nOrder Details: \n\n";
        for (int i = 0; i < m_numBurritos; i++){
            s += "Burrito " + (i + 1) + ":\n";
            s += m_order[i].toString() + "\n\n";
        }
        return s;
    }
}
