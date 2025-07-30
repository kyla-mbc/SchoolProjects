import java.util.LinkedList;

// Class "Player" that will be used with Dealer, Deck, Card, Game, and Driver Classes.
public class Player {

    // Private member variables that represent the number of players in the game, each of their hands, and the patterns for playing the game
    private int playerNum;
    private LinkedList<Card> hand;
    private String pattern;

    // Overloaded constructor that sets the three member variables to specific values. 
    public Player(int n, LinkedList<Card> h, String p) {
        playerNum = n;
        hand = h;
        pattern = p;
    }

    // Method playCard removes a Card from the top of the player’s hand (position 0) and returns it.
    public Card playCard() {
        if (hand.isEmpty()) {
            return null;
        }
        return hand.removeFirst();
    }

    // Method slaps evaluates the Player’s pattern member variable and calls the appropriate Game static method to check for that pattern. 
    //If the pattern is in play, the method should return true to slap. If not, the method should return false.
    public boolean slaps(LinkedList<Card> pile) {
        if (pattern.equals("doubles")) {
            return Game.doubles(pile);
        } else if (pattern.equals("top bottom")) {
            return Game.topBottom(pile);
        } else if (pattern.equals("sandwich")) {
            return Game.sandwich(pile);
        } else {
            return false;
        }
    }

    // Accessor Methods 
    //getPlayerNum gets the number of players.
    public int getPlayerNum() {
        return playerNum;
    }

    //getHand gets the hand of the players.
    public LinkedList<Card> getHand() {
        return hand;
    }

    //getPattern to get the pattern that each player looks out for. 
    public String getPattern() {
        return pattern;
    }

    // toString that returns the Player’s number, pattern, and current hand of cards
    @Override
    public String toString() {
        String s = "";
        for (Card card : hand) {
            s += card.toString() + ", ";
        }
        return "Player " + playerNum + ", Pattern: " + pattern + ", Hand: " + s;
    }
}
