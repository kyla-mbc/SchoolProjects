// Class that is named "Driver" that will be used along with the following classes: Dealer, Deck, Player, Game, and Card
public class Driver {
    public static void main(String[] args) { // Main method signature to run code


        // Creating a game with 4 players
        Game game = new Game(4);
        // Creating a variable called winner that would hold the winner of the game played
        int winner = game.play();
        // System.out.println("Player " + winner + " wins!");  
        System.out.println("!!!!!!!!!!!!!!Player " + winner + " wins!!!!!!!!!!!!!!");
    }
}
