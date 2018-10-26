
class Int {}

enum Suit { 
    Diamonds, Hearts, Spade, Clubs
}

class Card {
    suit: Suit
    value: Int
}


class Deck {
    cards = new Array<Card>()

    drawCards(count: Int) { /* ... */ }
    
}

class Player {
    name: string;
    cards = new Array<Card>();
    takeTurn(): Boolean { /* ... */ return true; }
}

abstract class Game {

    players = new Array<Player>();
    deck = new Deck();

    // Runs turn for player and returns true if they won
    abstract takeTurn(player: Player): Boolean; 
    // Runs through all the players turns
    abstract loopTurns(): Player;
    // Starts game
    abstract startGame(): void;

}

class Blackjack extends Game {

    takeTurn(player: Player): Boolean { /* ... */ return true; } 

    // Returns winner
    loopTurns(): Player { /* ... */ return null;}

    calculateValueOfHand(player: Player) {}
    compareHands(player1: Player, player2: Player) {}

    startGame() {
        // Init players
        console.log(this.loopTurns());
    }
}