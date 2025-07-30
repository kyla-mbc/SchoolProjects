// A class to test the Card, Deck, and Dealer classes
public class TestCards {

    // The main method to run the test
    public static void main(String[] args) {

        // Create a new dealer
        Dealer dealer = new Dealer();

        // Print the dealer's deck before dealing any cards
        System.out.println("Dealer's deck:");
        System.out.println(dealer);

        // Deal 5 cards from the dealer and print them
        System.out.println("\nDealing 5 Cards:");
        System.out.println(dealer.deals(5));

        // Print the remaining cards in the dealer's deck after dealing 5 cards
        System.out.println("\nRemaining cards in dealer's deck:");
        System.out.println(dealer);
    }
}
