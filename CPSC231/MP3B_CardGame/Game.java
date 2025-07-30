import java.util.LinkedList;
import java.util.Random;


// Class "Game" that will be used with Dealer, Deck, Player, Card, and Driver Classes.
public class Game {
   //Declare member variables that will be used in the game
    private LinkedList<Player> players;
    private LinkedList<Card> pile;
    private Dealer dealer;
    private static final String[] patterns = {"doubles", "top bottom", "sandwich"};
    private Player currentPlayer;
    private Player face;
    private Card lastCard;
    private Card faceCard;
    private LinkedList<Player> playerSlap;
    private boolean playerRemoved;  

    Random rand = new Random();

    // Default constructor that initializes a game with two players. 
    public Game() {
        dealer = new Dealer();
        players = new LinkedList<Player>();
        pile = new LinkedList<Card>();
        players.add(new Player(1, dealer.deals(26), patterns[(rand.nextInt(3))]) );
        players.add(new Player(2, dealer.deals(26), patterns[(rand.nextInt(3))]) );
        currentPlayer = players.getFirst();
    }

    // Overloaded constructor that accepts an integer that represents the number of players. 
    // This includes creating a new dealer, creating a default LinkedList of players and piles. 
    public Game(int numPlayers) {
        dealer = new Dealer();
        players = new LinkedList<Player>();
        pile = new LinkedList<Card>();
        for(int i = 1; i <= numPlayers; ++i) {
            players.add(new Player(i, dealer.deals(52 / numPlayers), patterns[(rand.nextInt(3))]));
        }
        currentPlayer = players.getFirst();
    }

    // Accessors used to return a specific variable
    // getplayers returns the number of players
    public LinkedList<Player> getPlayers() {
        return players;
    }

    //getPile returns the pile of the players
    public LinkedList<Card> getPile() {
        return pile;
    }

    //returns the current player to play next
    public Player getCurrentPlayer() {
        return currentPlayer;
    }

    // Method that carries out the rules of the game until only one player is remaining.
    //At the end, it returns the integer of the winning player.
    public int play() {
        System.out.println("===================================================================================================");
        System.out.println("Each player has 13 cards in their hand.");
        System.out.println("===================================================================================================");
        // Prints out each player in the game and the patterns they will watch out for and slap in for. 
        for (int i = 0; i < players.size(); ++i) {
            System.out.println("Player " + players.get(i).getPlayerNum() + "'s pattern: " + players.get(i).getPattern());
        }
        while (players.size() > 1) {
            // The current player drops a card
            lastCard = currentPlayer.playCard();
            pile.add(lastCard);
            System.out.print("Player " + currentPlayer.getPlayerNum() + " dropped a " + lastCard + " | ");
            for (Player player : players) {
                System.out.print("Player " + player.getPlayerNum() + "'s hand: " + player.getHand().size() + " | ");
            }
            System.out.println();
            // Checks if any Player can slap
            playerSlap = slapCheck();
            if (playerSlap.size() > 0) {
                playSlap(playerSlap);
            }
            // Checks if the card that was played is a face card
            else if (lastCard.getRank() > 10) {
                playFaceCard();
                removePlayer();
            }
            // If not all the players can slap and the card was not a face card, the next player goes.
            else {
                currentPlayer = nextPlayer();
                removePlayer();
            }
            // Prints the Players and each of their hands
            System.out.println("===================================================================================================");
            System.out.print("Hands: ");
            for (int i = 0; i < players.size(); ++i) {
                System.out.print("Player " + players.get(i).getPlayerNum() + "'s hand: "  + players.get(i).getHand().size() + " | ");
            }
            System.out.println("\n===================================================================================================");
        }
        System.out.println("Pile: " + pile.size() + " cards");
        return players.getFirst().getPlayerNum();
    }

    // Method will run if any of the players drop a face card.
    public void playFaceCard() {
        while (pile.size() > 0) {
            if (players.size() > 1) {
                face = nextPlayer();
                int chances = lastCard.getRank() - 10;
                System.out.println("Player " + face.getPlayerNum() + " has " + chances + " chances.");
   
                for (int i = 0; i < chances; ++i) {
                    faceCard = face.playCard();
                    pile.add(faceCard);
                    System.out.println("Player " + face.getPlayerNum() + " dropped a " + faceCard);
                    playerSlap = slapCheck();
                    if (playerSlap.size() > 0) {
                        playSlap(playerSlap);
                        break;
                    } else if (faceCard.getRank() > 10) {
                        lastCard = faceCard;
                        removePlayer();
                        if (players.size() > 1) {
                            currentPlayer = nextPlayer();
                        }
                        break;
                    } else if (i == (lastCard.getRank() - 11)) {
                        currentPlayer.getHand().addAll(pile);
                        System.out.println("Player " + currentPlayer.getPlayerNum() + " got the pile.");
                        pile.clear();
                        removePlayer();
                        break;
                    } else {
                        playerRemoved = removePlayer();
                        if (playerRemoved) {
                            face = nextPlayer();
                        }
                    }
                }
                removePlayer();
            } else {
                break;
            }
        }
    }
   
    // Method named removePlayer tells the code what the conditions are to remove a player.
    public boolean removePlayer() {
        for (int i = 0; i < players.size(); ++i) {
            if (players.get(i).getHand().size() == 0) {
                System.out.println("Player " + players.get(i).getPlayerNum()+ " has run out of cards.");
                players.remove(i);
                return true;
            }
        }
        return false;
    }

    // Method to slap the pile of qualifications are met.
    public void playSlap(LinkedList<Player> playerSlap) {
        if (playerSlap.size() > 0) {
                if (playerSlap.size() == 1) {
                    playerSlap.getFirst().getHand().addAll(pile);
                    pile.clear();
                    System.out.println("Player " + playerSlap.getFirst().getPlayerNum() + " slapped after finding a " + playerSlap.getFirst().getPattern() + " and got the pile");
                    currentPlayer = playerSlap.getFirst();
                }
                else {
                    Player slapped = playerSlap.get(rand.nextInt(playerSlap.size()));
                    slapped.getHand().addAll(pile);
                    pile.clear();
                    System.out.println("Player " + slapped.getPlayerNum() + " slapped after finding a " + slapped.getPattern() + " and got the pile");
                    currentPlayer = slapped;
                }
                removePlayer();
            }
    }

    // Method named playSlap that would determine if the players should slap based on the pattern rules.
    public LinkedList<Player> slapCheck() {
        LinkedList<Player> playerSlap = new LinkedList<Player>();
        for (int i = 0; i < players.size(); ++i) {
            if (players.get(i).slaps(pile)) {
                playerSlap.add(players.get(i));
            }
        }
        return playerSlap;
    }

    // Method to check who is the next player after te current player. 
    private Player nextPlayer() {
        if (getPlayers().size() > 1) {
            if (players.indexOf(currentPlayer) < (players.size() - 1)) {
                return players.get(players.indexOf(currentPlayer) + 1);
            }
            else return getPlayers().getFirst();
        }
        else {
            return getPlayers().getFirst();
        }
    }

    //Method that takes in a LinkedList, pile, and checks if the top card 
    //and the bottom card of the pile have the same rank. 
    //The code returns true if they do, and false if they are not equal.
    static boolean topBottom(LinkedList<Card> pile) {
        if (pile.size() >= 2) {
            if (pile.getFirst().equals(pile.get(pile.size() - 1))) {
                return true;
            }
            else  {
                return false;
            }
        }
        else {
            return false;
        }
    }

    //Method that takes in a LinkedList, pile, and checks if the top two cards
    //of the pile have the same rank. The code returns true if they do, and false if they are not equal.
    static boolean doubles(LinkedList<Card> pile) {
        if (pile.size() >= 2) {
            if (pile.get(pile.size() - 2).equals(pile.get(pile.size() - 1))) {
                return true;
            }
            else {
                return false;
            }
        }
        else {
            return false;
        }
    }

    //Method that takes in a LinkedList, pile, and checks if the top card 
    //and the card under the one before it on the pile have the same rank. 
    //The code returns true if they do, and false if they are not equal.
    static boolean sandwich(LinkedList<Card> pile) {
        if (pile.size() >= 3) {
            if (pile.get(pile.size() - 3).equals(pile.get(pile.size() - 1))) {
                return true;
            }
            else {
                return false;
            }
        }
        else {
            return false;
        }
    }
}
