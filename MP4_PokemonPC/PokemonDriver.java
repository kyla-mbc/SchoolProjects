/*
Various imports for the program
*/
import java.util.Scanner;
import java.util.InputMismatchException;

/*
@author Manuel Pangelinan
@author Brent Ortizo
@author Kyla Cabrera
@version 1.5
@see Ampharos | Bulbasaur | Pokemon | Raticate | PCBox | PC
*/

/*
Class that runs the entirety of the program
*/
public class PokemonDriver {

    /*
    Main method signature that runs the program
    */
    public static void main(String[] args) {

        /*
        Scanner object that reads user input
        */
        Scanner scanner = new Scanner(System.in);

        /*
        Creates a new PC object
        */
        PC pc = new PC();

        /*
        Represents the menu that will be repeatedly printed out after each full action that the user does until wanting to exit the program
        */
        while (true) {

            /*
            Menu options
            */
            System.out.println("1. Add Pokemon to a box");
            System.out.println("2. Remove Pokemon from a box");
            System.out.println("3. Sort a box by Pokemon level");
            System.out.println("4. View a specific box");
            System.out.println("5. View all boxes");
            System.out.println("6. Choose a Pokemon to do its cry");
            System.out.println("7. Compare two Pokemon");
            System.out.println("8. Exit");

            /*
            Prompts the user to enter an option
            */
            int choice;
            try {
                choice = scanner.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("Invalid input, please enter a number.");
                scanner.next();
                continue;
            }

            /*
            If the user chooses the number 8, the program will end
            */
            if (choice == 8) {
                break;
            }

            /*
            Switch statement that runs the appropriate set of actions based on the user's choice
            */
            switch (choice) {

                /*
                If the user chooses the number 1, the program will add a Pokemon to a box
                */
                case 1:
                    System.out.println("Choose a box (1-5):");
                    int boxIndex;
                    try {
                        boxIndex = scanner.nextInt() - 1;
                    } catch (InputMismatchException e) {
                        System.out.println("Invalid input, please enter a number.");
                        scanner.next();
                        continue;
                    }

                    System.out.println("Choose the number of the Pokemon to add to the box:");
                    System.out.println("1. Bulbasaur");
                    System.out.println("2. Raticate");
                    System.out.println("3. Ampharos");

                    int pokemonChoice;
                    try {
                        pokemonChoice = scanner.nextInt();
                    } catch (InputMismatchException e) {
                        System.out.println("Invalid input, please enter a number.");
                        scanner.next();
                        continue;
                    }

                    System.out.println("Enter the level of the Pokemon:");
                    int level;
                    try {
                        level = scanner.nextInt();
                    } catch (InputMismatchException e) {
                        System.out.println("Invalid input, please enter a number.");
                        scanner.next();
                        continue;
                    }

                    Pokemon p = null;
                    switch (pokemonChoice) {
                        case 1:
                            p = new Bulbasaur("Bulbasaur", "Grass", level, 45, 49, 49);
                            break;
                        case 2:
                            p = new Raticate("Raticate", "Normal", level, 55, 81, 60);
                            break;
                        case 3:
                            p = new Ampharos("Ampharos", "Electric", level, 90, 75, 85);
                            break;
                        default:
                            System.out.println("Invalid choice, please try again.");
                            continue;
                    }

                    pc.addPokemonToBox(boxIndex, p);
                    pc.printBox(boxIndex);
                    break;

                /*
                If the user chooses the number 2, the program will remove a Pokemon from a box
                */
                case 2:
                    System.out.println("Choose a box (1-5):");
                    try {
                        boxIndex = scanner.nextInt() - 1;
                    } catch (InputMismatchException e) {
                        System.out.println("Invalid input, please enter a number.");
                        scanner.next();
                        continue;
                    }

                    System.out.println("Enter the name of the Pokemon to remove:");
                    String pokemonName = scanner.next();

                    pc.removePokemonFromBox(boxIndex, pokemonName);
                    pc.printBox(boxIndex);
                    break;

                /*
                If the user chooses the number 3, the program will sort a box by Pokemon level
                */
                case 3:
                    System.out.println("Choose a box to sort by Pokemon level (1-5):");
                    try {
                        boxIndex = scanner.nextInt() - 1;
                    } catch (InputMismatchException e) {
                        System.out.println("Invalid input, please enter a number.");
                        scanner.next();
                        continue;
                    }

                    pc.sortBoxByLevel(boxIndex);
                    pc.printBox(boxIndex);
                    break;

                /*
                If the user chooses the number 4, the program will view a specific box
                */
                case 4:
                    System.out.println("Choose a box to view (1-5):");
                    int viewBoxIndex;
                    try {
                        viewBoxIndex = scanner.nextInt() - 1;
                    } catch (InputMismatchException e) {
                        System.out.println("Invalid input, please enter a number.");
                        scanner.next();
                        continue;
                    }

                    pc.printBox(viewBoxIndex);
                    break;

                /*
                If the user chooses the number 5, the program will view all boxes
                */
                case 5:
                    pc.printAllBoxes();
                    break;

                /*
                If the user chooses the number 6, the program will choose a Pokemon to do its cry
                */
                case 6:
                    System.out.println("Choose a box to view (1-5):");
                    int boxIndexCry;
                    try {
                        boxIndexCry = scanner.nextInt() - 1;
                    } catch (InputMismatchException e) {
                        System.out.println("Invalid input, please enter a number.");
                        scanner.next();
                        continue;
                    }

                    System.out.println("Choose the index of the Pokemon in the box:");
                    pc.printBox(boxIndexCry);
                    int pokemonIndexCry;
                    try {
                        pokemonIndexCry = scanner.nextInt() - 1;
                    } catch (InputMismatchException e) {
                        System.out.println("Invalid input, please enter a number.");
                        scanner.next();
                        continue;
                    }

                    pc.performCry(boxIndexCry, pokemonIndexCry);
                    break;

                /*
                If the user chooses the number 7, the program will compare two Pokemon
                */
                case 7:
                    System.out.println("Choose the box of the first Pokemon (1-5):");
                    int firstBoxIndex;
                    try {
                        firstBoxIndex = scanner.nextInt() - 1;
                    } catch (InputMismatchException e) {
                        System.out.println("Invalid input, please enter a number.");
                        scanner.next();
                        continue;
                    }

                    System.out.println("Choose the index of the first Pokemon:");
                    pc.printBox(firstBoxIndex);
                    int firstPokemonIndex;
                    try {
                        firstPokemonIndex = scanner.nextInt() - 1;
                    } catch (InputMismatchException e) {
                        System.out.println("Invalid input, please enter a number.");
                        scanner.next();
                        continue;
                    }

                    System.out.println("Choose the box of the second Pokemon (1-5):");
                    int secondBoxIndex;
                    try {
                        secondBoxIndex = scanner.nextInt() - 1;
                    } catch (InputMismatchException e) {
                        System.out.println("Invalid input, please enter a number.");
                        scanner.next();
                        continue;
                    }

                    System.out.println("Choose the index of the second Pokemon:");
                    pc.printBox(secondBoxIndex);
                    int secondPokemonIndex;
                    try {
                        secondPokemonIndex = scanner.nextInt() - 1;
                    } catch (InputMismatchException e) {
                        System.out.println("Invalid input, please enter a number.");
                        scanner.next();
                        continue;
                    }

                    pc.comparePokemons(firstBoxIndex, firstPokemonIndex, secondBoxIndex, secondPokemonIndex);
                    break;

                /*
                If the user chooses the number 8, the program will end
                */
                default:
                    System.out.println("Invalid choice, please try again.");
                    break;
            }
        }
        
        /*
        When the user chooses to end the program, the scanner will close to prevent any issues
        */
        scanner.close();
    }
}