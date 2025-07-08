/*
Various imports for the program
*/
import java.util.ArrayList;
import java.util.Collections;

/*
@author Manuel Pangelinan
@author Brent Ortizo
@author Kyla Cabrera
@version 1.5
@see Ampharos | Bulbasaur | Pokemon | Raticate | PC | PokemonDriver
*/

/*
Class that represents a Pokemon PC Box, where Pokemon are stored, removed, and sorted
*/
public class PCBox {

    /*
    Member Variables that represent the list of Pokemon in the box, and the maximum amount of Pokemon that can be stored in a single box
    */
    private ArrayList<Pokemon> box;
    private static final int MAX_POKEMON_PER_BOX = 10;

    /*
    Default Constructor that initializes the ArrayList of Pokemon in the box
    */
    public PCBox() {
        box = new ArrayList<Pokemon>();
    }

    /*
    Method that adds a Pokemon to the box
    @param p - the Pokemon to be added to the box
    */
    public void addPokemon(Pokemon p) {
        if (box.size() < MAX_POKEMON_PER_BOX) {
            box.add(p);
        } else {
            System.out.println("Box is full!");
        }
    }

    /*
    Method that removes a Pokemon from the box
    @param name - the name of the Pokemon to be removed
    @return true if the Pokemon was removed, false if the Pokemon was not found
    */
    public boolean removePokemon(String name) {
        for (Pokemon p : box) {
            if (p.getName().equalsIgnoreCase(name)) {
                box.remove(p);
                return true;
            }
        }
        return false;
    }

    /*
    Method that sorts the Pokemon in the box by level
    */
    public void sortBox() {
        Collections.sort(box);
    }

    /*
    Method that prints the current box
    */
    public void printBox() {
        for (int i = 0; i < MAX_POKEMON_PER_BOX; i++) {
            if (i < box.size()) {
                Pokemon pokemon = box.get(i);
                System.out.println("Pokemon #" + (i + 1) + ": " + pokemon.getName());
                System.out.println("\tType: " + pokemon.getType());
                System.out.println("\tLevel: " + pokemon.getLevel());
                System.out.println("\tHealth: " + pokemon.getHealth());
                System.out.println("\tAttack: " + pokemon.getAttack());
                System.out.println("\tDefense: " + pokemon.getDefense());
            } else {
                System.out.println("Empty Slot");
            }
        }
    }

    /*
    Method that returns the contents of a box as a string
    @return s - a string containing the contents of the box
    */
    public String getBoxContents() {
        String s = "";
        for (int i = 0; i < MAX_POKEMON_PER_BOX; i++) {
            if (i < box.size()) {
                s += box.get(i).toString() + "\n";
            } else {
                s += "Empty Slot\n";
            }
        }
        return s;
    }

    /*
    Method that gets the Pokemon at a specific index in the box
    @param index - the index of the Pokemon to be returned
    @return null if the index is out of bounds
    @return box.get(index) - the Pokemon at the specified index
    */
    public Pokemon getPokemon(int index) {
        if (index < 0 || index >= box.size()) {
            System.out.println("Invalid Pokemon index.");
            return null;
        }
        return box.get(index);
    }
}