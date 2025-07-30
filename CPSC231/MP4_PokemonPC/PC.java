/*
Various imports for the program
*/
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

/*
@author Manuel Pangelinan
@author Brent Ortizo
@author Kyla Cabrera
@version 1.5
@see Ampharos | Bulbasaur | Pokemon | Raticate | PCBox | PokemonDriver
*/

/*
Class that represents a Pokemon PC, storing Pokemon and their information, along with different methods to add, remove, and sort Pokemon
*/
public class PC {

    /*
    Member Variables that represent the different boxes in the PC and the maximum amount of boxes that can be in it
    */
    private ArrayList<PCBox> boxes;
    private static final int MAX_BOXES = 5;

    /*
    Default constructor that initializes the boxes ArrayList for the PC and clears the current text file
    */
    public PC() {
        boxes = new ArrayList<PCBox>(MAX_BOXES);
        for (int i = 0; i < MAX_BOXES; i++) {
            boxes.add(new PCBox());
        }
        writeToFile("Successfully logged in");
    }

    /*
    Method that prints the addition of a Pokemon to the PC and the current box to the text file
    @param boxIndex - the index of the box that the Pokemon was added to
    @param p - the Pokemon added
    */
    public void addPokemonToBox(int boxIndex, Pokemon p) {
        if (boxIndex < 0 || boxIndex >= MAX_BOXES) {
            System.out.println("Invalid box index.");
            return;
        }
        boxes.get(boxIndex).addPokemon(p);
        String content = "Added " + p.getName() + " to box " + (boxIndex + 1) + "\n";
        content += "Current contents of box " + (boxIndex + 1) + ":\n" + boxes.get(boxIndex).getBoxContents();
        writeToFile(content);
    }

    /*
    Method that prints the removal of a specific Pokemon from the PC and the current box to the text file
    @param boxIndex - the index of the box that the Pokemon was removed from
    @param pokemonName - the name of the Pokemon removed
    */
    public void removePokemonFromBox(int boxIndex, String pokemonName) {
        if (boxIndex < 0 || boxIndex >= MAX_BOXES) {
            System.out.println("Invalid box index.");
            return;
        }
        boolean removed = boxes.get(boxIndex).removePokemon(pokemonName);
        if (removed) {
            String content = "Removed " + pokemonName + " from box " + (boxIndex + 1) + "\n";
            content += "Current contents of box " + (boxIndex + 1) + ":\n" + boxes.get(boxIndex).getBoxContents();
            writeToFile(content);
        } else {
            System.out.println("Pokemon not found in the box.");
        }
    }

    /*
    Method that prints the sorted box in the PC by level to the text file
    @param boxIndex - the index of the box sorted
    */
    public void sortBoxByLevel(int boxIndex) {
        if (boxIndex < 0 || boxIndex >= MAX_BOXES) {
            System.out.println("Invalid box index.");
            return;
        }
        boxes.get(boxIndex).sortBox();
        String content = "Sorted box " + (boxIndex + 1) + " by Pokemon level.\n";
        content += "Current contents of box " + (boxIndex + 1) + ":\n" + boxes.get(boxIndex).getBoxContents();
        writeToFile(content);
    }

    /*
    Method that prints the contents in the box, vertically, by order of when added to the PC
    @param boxIndex - the index of the box to print
    */
    public void printBox(int boxIndex) {
        if (boxIndex < 0 || boxIndex >= MAX_BOXES) {
            System.out.println("Invalid box index.");
            return;
        }
        boxes.get(boxIndex).printBox();
    }

    /*
    Method that prints all the boxes in the PC, vertically
    */
    public void printAllBoxes() {
        for (int i = 0; i < MAX_BOXES; i++) {
            System.out.println("Box " + (i + 1) + ":");
            boxes.get(i).printBox();
            System.out.println();
        }
    }

    /*
    Method that gets a certain box from the PC, used for printing specific boxes in an earlier method
    @param index - index of the box
    @return boxes.get(index) - the box at the given index
    */
    public PCBox getBox(int index) {
        if (index < 0 || index >= MAX_BOXES) {
            System.out.println("Invalid box index.");
            return null;
        }
        return boxes.get(index);
    }

    /*
    Method that prints the comparison between two Pokemon objects by their level to the text file
    @param firstBoxIndex - the index of the first box
    @param firstPokemonIndex - the index of the first Pokemon in the first box
    @param secondBoxIndex - the index of the second box
    @param secondPokemonIndex - the index of the second Pokemon in the second box
    */
    public void comparePokemons(int firstBoxIndex, int firstPokemonIndex, int secondBoxIndex, int secondPokemonIndex) {
        Pokemon firstPokemon = getBox(firstBoxIndex).getPokemon(firstPokemonIndex);
        Pokemon secondPokemon = getBox(secondBoxIndex).getPokemon(secondPokemonIndex);

        if (firstPokemon == null || secondPokemon == null) {
            System.out.println("Invalid Pokemon selection.");
            return;
        }

        int comparisonResult = firstPokemon.compareTo(secondPokemon);

        String comparisonOutput;
        if (comparisonResult > 0) {
            comparisonOutput = firstPokemon.getName() + " is of a higher level than " + secondPokemon.getName();
        } else if (comparisonResult < 0) {
            comparisonOutput = firstPokemon.getName() + " is of a lower level than " + secondPokemon.getName();
        } else {
            comparisonOutput = firstPokemon.getName() + " and " + secondPokemon.getName() + " are of the same level.";
        }

        System.out.println(comparisonOutput);

        String comparisonDetails = "Comparing " + firstPokemon.getName() + " (Level " + firstPokemon.getLevel() + ") with " + secondPokemon.getName() + " (Level " + secondPokemon.getLevel() + "): " + comparisonOutput + "\n";
        writeToFile(comparisonDetails);
    }

    /*
    Method that prints the cry of a specific Pokemon to the text file
    */
    public void performCry(int boxIndex, int pokemonIndex) {
        Pokemon chosenPokemon = getBox(boxIndex).getPokemon(pokemonIndex);
        if (chosenPokemon != null) {
            chosenPokemon.doCry();
            String content = "Performed cry of " + chosenPokemon.getName() + "\n";
            writeToFile(content);
        } else {
            System.out.println("Invalid Pokemon index.");
        }
    }

    /*
    Method that writes the given content to a text file
    @param content - the content to write to the file
    */
    public void writeToFile(String content) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("user_choices.txt", true))) {
            writer.write(content);
            writer.newLine();
            writer.flush();
        } catch (IOException e) {
            System.out.println("An error occurred while writing to the file.");
        }
    }
}
