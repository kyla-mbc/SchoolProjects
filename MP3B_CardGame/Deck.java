import java.util.LinkedList;
import java.util.Random;

// Represents a deck of playing cards
public class Deck {

    //Private member variable that establishes the maximum cards in a deck
    public static final int NUM_CARDS =  52;
    // LinkedList to store cards in the deck
    private LinkedList<Card> m_cards;
    // Random object for shuffling and dealing cards
    Random rand = new Random();

    // Default constructor that initializes a deck with 52 cards and stores it into the m_cards variable
    public Deck() {
        m_cards = new LinkedList<>();
        for (int s = 0; s < 4; s++) {
            for (int r = 2; r <= 14; r++) {
                m_cards.add(new Card(r, s));
            }
        }
    }

    // Copy constructor that creates a copy of another deck that would change the m_cards variable
    public Deck(Deck deckToCopy) {
        m_cards = new LinkedList<>();
        for (int i = 0; i < deckToCopy.m_cards.size(); i++) {
            Card c = deckToCopy.m_cards.get(i);
            m_cards.add(new Card(c));
        }
    }

    // toString method returns a string representation of the deck
    public String toString() {
        return m_cards.toString();
    }

    // Getter method that returns the number of cards in the deck
    public int getCardSize() {
        return m_cards.size();
    }

    // Removes and returns a random card from the deck
    public Card deal() {
        if (m_cards.isEmpty()) {
            return null;
        }
        int ranIndex = rand.nextInt(m_cards.size());
        return m_cards.remove(ranIndex);
    }

}
