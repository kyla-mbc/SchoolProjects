public class Burrito {
    private String m_size;
    private String m_protein;
    private String m_rice;
    private String m_beans;
    private boolean m_guac;
    private boolean m_tomatillo;
    private boolean m_sourCream;
    private boolean m_cheese;
    private boolean m_lettuce;

    //Default Constructor
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

    //Overload Constructor
    public Burrito(String size, String protein, String rice, String beans,
                   boolean guac, boolean tomatillo, boolean sourCream,
                   boolean cheese, boolean lettuce) {
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

    // Copy Constructor
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

    // Public accessors and mutators.

    //Public Method calcCost()
    public double calcCost() {
        double cost = 0;
        if (m_size.equals("Kids")) {
            cost += 7.00;
        } else {
            cost += 9.00;
        }
        if (m_protein.equals("Chicken")) {
            cost += 0.50;
        } else if (m_protein.equals("Steak")) {
            cost += 1.25;
        } else if (m_protein.equals("Veggie") && !m_guac) {
            // Veggie includes guacamole
            cost += 0.50;
        }
        if (m_guac) {
            cost += 2.65;
        }
        if (m_sourCream) {
            cost += 0.25;
        }
        if (m_cheese) {
            cost += 0.50;
        }
        return cost;
    }

    //Returns Burrito Properties
    public String toString() {
        return "Burrito:\n" +
                "Size = '" + m_size + "'\n" +
                "Protein = '" + m_protein + "'\n" +
                "Rice = '" + m_rice + "'\n" +
                "Beans = '" + m_beans + "'\n" +
                "Guac = " + m_guac + "\n" +
                "Tomatillo = " + m_tomatillo + "\n" +
                "SourCream = " + m_sourCream + "\n" +
                "Cheese = " + m_cheese + "\n" +
                "Lettuce = " + m_lettuce + "\n" +
                "Cost = $" + calcCost() +
                "";
    }

    // Equals method
    public boolean equals(Burrito burritoToCopy) {
        return m_size.equals(burritoToCopy.m_size) &&
                m_protein.equals(burritoToCopy.m_protein) &&
                m_rice.equals(burritoToCopy.m_rice) &&
                m_beans.equals(burritoToCopy.m_beans) &&
                m_guac == burritoToCopy.m_guac &&
                m_tomatillo == burritoToCopy.m_tomatillo &&
                m_sourCream == burritoToCopy.m_sourCream &&
                m_cheese == burritoToCopy.m_cheese &&
                m_lettuce == burritoToCopy.m_lettuce;
    }

    public static void main(String[] args) {
        Burrito defaultBurrito = new Burrito();
        System.out.println("---------------------------------------------");
        System.out.println("Default Burrito: " + defaultBurrito.toString());
        System.out.println("---------------------------------------------");

        Burrito customBurrito = new Burrito("kids", "steak", "brown", "pinto", true, false, true, false, false);
        System.out.println("Custom Burrito: " + customBurrito.toString());
        System.out.println("---------------------------------------------");
        System.out.println("Are the burritos equal? " + defaultBurrito.equals(customBurrito));
    }
}
