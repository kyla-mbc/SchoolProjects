import java.util.LinkedList;

// Represents a dealer in a card game
public class Dealer {

    // Instance variable to store the deck of cards
    private Deck m_deck;

    // Constructor that initializes the dealer with a new deck of cards
    public Dealer() {
        m_deck = new Deck();
    }

    // Deals a certain amount of cards from the deck
    public LinkedList<Card> deals(int n) {
        LinkedList<Card> dealtCards = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            Card card = m_deck.deal();
            if (card != null) {
                dealtCards.add(card);
            } else {
                break;
            }
        }
        return dealtCards;
    }

    // Getter method that returns the number of cards remaining in the deck
    public int size() {
        return m_deck.getCardSize();
    }

    // Returns a string representation of the dealer's deck of cards
    public String toString() {
        return m_deck.toString();
    }
}
