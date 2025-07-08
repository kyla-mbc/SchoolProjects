//Class to represent a playing card
public class Card {
    //Assign values to card suits
    public static final int HEARTS = 0;
    public static final int SPADES = 1;
    public static final int CLUBS = 2;
    public static final int DIAMONDS = 3;

    //Assign values to card ranks for face cards
    public static final int JACK = 11;
    public static final int QUEEN = 12;
    public static final int KING = 13;
    public static final int ACE = 14;

    //Instance variables for rank and suit of the card
    private int rank; //assigns values 2-10 to given cards along with the already set values above
    private int suit;

    //Default Constructor which creates an Ace of Spades
    public Card() {
        rank = ACE; 
        suit = SPADES;
    }

    //Constructor that creates a card with a given rank and suit
    public Card(int rc, int sc) {
        rank = rc;
        suit = sc;
    }

    //Copy constructor that creates a card by copying an already existent card
    public Card(Card cardToCopy) {
        rank = cardToCopy.rank;
        suit = cardToCopy.suit;
    }

    //Setter method for the rank of the card
    public void setRank(int rc) {
        rank = rc;
    }

    //Setter method for the suit of the card
    public void setSuit(int sc) {
        suit = sc;
    }

    //Getter method for the rank of the card
    public int getRank() {
        return rank;
    }

    //Getter method for the suit of the card
    public int getSuit() {
        return suit;
    }

    //Returns a string representation of the card
    public String toString() {
        String rankStr;
        String suitStr;

        //Converts rank to string representation
        if (rank == JACK) {
            rankStr = "Jack";
        } else if (rank == QUEEN) {
            rankStr = "Queen";
        } else if (rank == KING) {
            rankStr = "King";
        } else if (rank == ACE) {
            rankStr = "Ace";
        } else {
            rankStr = String.valueOf(rank);
        }

        //Converts suit to string representation
        if (suit == HEARTS) {
            suitStr = "Hearts";
        } else if (suit == SPADES) {
            suitStr = "Spades";
        } else if (suit == CLUBS) {
            suitStr = "Clubs";
        } else if (suit == DIAMONDS) {
            suitStr = "Diamonds";
        } else {
            suitStr = "Invalid Suit";
        }

        //Returns the formatted string representation of the card
        return rankStr + " of " + suitStr;
    }

    //Checks if two card are equal based on their rank
    public boolean equals (Card o){
        if (o == this){
            return true;
        }
        if (!(o instanceof Card)){
            return false;
        }
        Card a = (Card) o;
        return this.rank == a.rank;
    }
}

