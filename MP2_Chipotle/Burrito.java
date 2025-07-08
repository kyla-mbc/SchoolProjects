/**JavaDoc Comments:
 * This is the Burrito class which represents the type of burrito and its contents as well as its cost.
 * This class was created to assist with the BurritoOrder and ChipotleDriver classes.
 * @author Kyla Monique Cabrera
 * @see BurritoOrder
 * @see ChipotleDriver
 */

public class Burrito {
    /** Private Member Variables */
    /** A string representing the size of the burrito, whether it be "Regular" or "Kids" */
    private String m_size;
    /** A string representing the type of protein in the burrito. */
    private String m_protein;
    /** A string representing what type of rice is in the burrito. */
    private String m_rice;
    /** A string representing the type of beans in the burrito. */
    private String m_beans;
    /** A boolean representing whether or not the burrito has guacamole. */
    private boolean m_guac;
    /** A boolean representing whether or not the burrito has tomatillo. */
    private boolean m_tomatillo;
    /** A boolean representing whether or not the burrito has sour cream. */
    private boolean m_sourCream;
    /** A boolean representing whether or not the burrito has cheese. */
    private boolean m_cheese;
    /** A boolean representing whether or not the burrito has lettuce. */
    private boolean m_lettuce;

    /**
     * Default Constructorz
     * The Burrito constructor sets default values to each member variable. 
     */
    public Burrito() {
        m_size = "Regular";
        m_protein = "Chicken";
        m_rice = "White";
        m_beans = "Black";
        m_guac = false;
        m_tomatillo = false;
        m_sourCream = true;
        m_cheese = false;
        m_lettuce = true;
    }

    /** 
     * Overloaded Constructor  
     * Sets each member variable to the given input, whether it be through user input or hard coding. In this case, we use hard coding. 
     * @param size represents the size of the burrito.
     * @param protein represents the protein that will be in the burrito.
     * @param rice represents what type of rice will be in the burrito. 
     * @param beans represents what type of beans will be in the burrito.
     * @param guac represents whether or not the burrito will have guacamole.
     * @param tomatillo represents whether or not the burrito will have tomatillo.
     * @param sourCream represents whether or not the burrito will have sour cream.
     * @param cheese represents whether or not the burrito will have cheese.
     * @param lettuce represents whether or not the burrito will have lettuce.
     */
    public Burrito(String size, String protein, String rice, String beans,
                   boolean guac, boolean tomatillo, boolean sourCream,
                   boolean cheese, boolean lettuce) {
        /** Each parameter is assigned to its respective member variable. */
        m_size = size;
        m_protein = protein;
        m_rice = rice;
        m_beans = beans;
        m_guac = guac;
        m_tomatillo = tomatillo;
        m_sourCream = sourCream;
        m_cheese = cheese;
        m_lettuce = lettuce;
    }

    /**
     * Copy Constructor
     * Makes a deep copy of the already existent burrito. 
     * @param burritoToCopy is a parameter that represents an already existent burrito.
     */
    public Burrito(Burrito burritoToCopy) {
        m_size = burritoToCopy.m_size;
        m_protein = burritoToCopy.m_protein;
        m_rice = burritoToCopy.m_rice;
        m_beans = burritoToCopy.m_beans;
        m_guac = burritoToCopy.m_guac;
        m_tomatillo = burritoToCopy.m_tomatillo;
        m_sourCream = burritoToCopy.m_sourCream;
        m_cheese = burritoToCopy.m_cheese;
        m_lettuce = burritoToCopy.m_lettuce;
    }

    /** Accessors that are used to return each member variable as follows:  */

    /** @return m_size returns the value of the burrito's size attribute. */
    public String getSize() {
        return m_size;
    }

    /** @return m_size returns the value of the burrito's protein attribute. */
    public String getProtein() {
        return m_protein;
    }

    /** @return m_size returns the value of the burrito's rice attribute. */
    public String getRice() {
        return m_rice;
    }

    /** @return m_size returns the value of the burrito's beans attribute. */
    public String getBeans() {
        return m_beans;
    }

    /** @return m_size returns the value of the burrito's guacamole attribute. */
    public boolean hasGuac() {
        return m_guac;
    }

    /** @return m_size returns the value of the burrito's tomatillo attribute. */
    public boolean hasTomatillo() {
        return m_tomatillo;
    }

    /** @return m_size returns the value of the burrito's sour cream attribute. */
    public boolean hasSourCream() {
        return m_sourCream;
    }

    /** @return m_size returns the value of the burrito's cheese attribute. */
    public boolean hasCheese() {
        return m_cheese;
    }

    /** @return m_size returns the value of the burrito's lettuce attribute. */
    public boolean hasLettuce() {
        return m_lettuce;
    }

    /** Mutators are used to change the member variables.
     * Each parameter of the mutators lets the value of every member variable to be changed or altered. 
     */

    /** @param size is a string for the new size of the burrito. */
    public void setSize(String size) {
        m_size = size;
    }

    /** @param protein is a string for the new protein of the burrito. */
    public void setProtein(String protein) {
        m_protein = protein;
    }

    /** @param rice is a string for the new rice of the burrito. */
    public void setRice(String rice) {
        m_rice = rice;
    }

    /** @param beans is a string for the new beans in the burrito. */
    public void setBeans(String beans) {
        m_beans = beans;
    }

    /** @param guac is a boolean for whether or not there is guacamole in the burrito. */
    public void setGuac(boolean guac) {
        m_guac = guac;
    }

    /** @param tomatillo is a boolean for whether or not there is tomatillo in the burrito. */
    public void setTomatillo(boolean tomatillo) {
        m_tomatillo = tomatillo;
    }

    /** @param sourCream is a boolean for whether or not there is sour cream in the burrito. */
    public void setSourCream(boolean sourCream) {
        m_sourCream = sourCream;
    }

    /** @param cheese is a boolean for whether or not there is cheese in the burrito. */
    public void setCheese(boolean cheese) {
        m_cheese = cheese;
    }

    /** @param lettuce is a boolean for whether or not there is lettuce in the burrito. */
    public void setLettuce(boolean lettuce) {
        m_lettuce = lettuce;
    }

    /** 
     * Public Method calcCost is used to calculate the cost of the burrito given the different member variables and returns the total cost. 
     * @return cost returns the total cost of the burrito with all the chosen member variables taken into account. 
     */
    public double calcCost() {
        double cost = 0.0;
        if (m_size.equals("Kids")) {
            cost += 7.00;
        } else {
            cost += 9.00;
        }
        if (m_protein.equals("Chicken")) {
            cost += 0.50;
        } else if (m_protein.equals("Steak")) {
            cost += 1.25;
        } else if (m_protein.equals("Veggie")){
            cost += 0.50;
        }
        if (m_guac && !m_protein.equals("Veggie")) {
            cost += 2.65;
        }
        if (m_tomatillo) {
            cost += 0.0;
        }
        if (m_sourCream) {
            cost += 0.25;
        }
        if (m_cheese) {
            cost += 0.50;
        }
        if (m_lettuce) {
            cost += 0.0;
        }
        return cost;
    }

    /** 
     * toString Method that is used to create a printing format string with all the details of the burrito.
     * @return s returns the printing format string for use in the main method. 
     */
    public String toString(){
        String s = "";
        s += "Size: " + m_size;
        s += "\nProtein: " + m_protein;
        s += "\nRice: " + m_rice;
        s += "\nBeans: " + m_beans;
        s += "\nGuacamole: " + m_guac;
        s += "\nTomatillo Salsa: " + m_tomatillo;
        s += "\nSour Cream: " + m_sourCream;
        s += "\nCheese: " + m_sourCream;
        s += "\nLettuce: " + m_lettuce;
        s += "\nCost: S" + calcCost();

        return s;
    }

    /**
     * Equals Method is used to compare one burrito to another and checks if they are equal. 
     * Checks if each member variable is equivalent to that of the other burrito. 
     * @param obj represents the Burrito object to compare to.
     * @return true returns returns true if the object equals to "this".
     * @return this.m_size.equals(obj.m_size) &&
                this.m_protein.equals(obj.m_protein) &&
                this.m_rice.equals(obj.m_rice) &&
                this.m_beans.equals(obj.m_beans) &&
                this.m_guac == obj.m_guac &&
                this.m_tomatillo == obj.m_tomatillo &&
                this.m_sourCream == obj.m_sourCream &&
                this.m_cheese == obj.m_cheese &&
                this.m_lettuce == obj.m_lettuce; returns this entier line if object != "this".
     */
    public boolean equals(Burrito obj) {
        if (obj == this){
            return true;
        }
        Burrito a = (Burrito) obj;
        return this.m_size.equals(obj.m_size) &&
                this.m_protein.equals(obj.m_protein) &&
                this.m_rice.equals(obj.m_rice) &&
                this.m_beans.equals(obj.m_beans) &&
                this.m_guac == obj.m_guac &&
                this.m_tomatillo == obj.m_tomatillo &&
                this.m_sourCream == obj.m_sourCream &&
                this.m_cheese == obj.m_cheese &&
                this.m_lettuce == obj.m_lettuce;
    }
}
                
