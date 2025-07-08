/*
@author Manuel Pangelinan
@author Brent Ortizo
@author Kyla Cabrera
@version 1.5
@see Ampharos | Bulbasaur | Pokemon | PC | PCBox | PokemonDriver
*/

/*
Class that represents the Pokemon, Bulbasaur, inheriting from the Pokemon class
*/
public class Raticate extends Pokemon {

    /*
    Member Variable that represents the ID of the Pokemon
    */
    final protected int m_id = 20;

    /*
    Default Constructor that uses Pokemon's default constructor
    */
    public Raticate() {
        super();
    }

    /*
    Fully Specified Constructor that uses Pokemon's overloaded constructor
    @param n - name of the Pokemon
    @param t - type of the Pokemon
    @param l - level of the Pokemon
    @param h - health of the Pokemon
    @param a - attack of the Pokemon
    @param d - defense of the Pokemon
    */
    public Raticate(String n, String t, int l, int h, int a, int d) {
        super(n, t, l, h, a, d);
    }

    /*
    Method that creates a nicely printed statement, using Pokemon's toString method
    @return s - a string containing the Pokemon's name, type, level, health, attack, defense, and ID
    */
    public String toString() {
        String s = "";
        s += super.toString();
        s += "Pokedex ID: " + m_id;
        return s;
    }

    /*
    Getter method that returns the ID of the Pokemon
    @return m_id - the ID of the Pokemon
    */
    public int getID() {
        return m_id;
    }

    /*
    Defined abstract method that prints a Pokemon's cry
    */
    public void doCry() {
        System.out.println("PERYOO!!!");
    }
}