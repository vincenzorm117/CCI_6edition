// NOTE: some methods have return statements. I put those there so the linter doesn't highlight where the method is used.

enum Color {
    Black = 0, 
    White = 1
}

class Piece {
    type: Color;
    constructor(type: Color) {
        this.type = type;
    }
}

class Player {
    type: Color;
    game: OthelloGame;
    name: string;
    
    constructor(type: Color, game: OthelloGame, name: string) {
        this.type = type;
        this.game = game;
    }

    GetUserInput() { /* ... */ return { x:0, y: 0} }

    TakeTurn() {
        do {
            var coordinates = this.GetUserInput();
        } while(this.game.IsInvalidMove(coordinates));
        // Make move:
        // 1. Put piece down
        // 2. Update board with pieces
    }
}


class OthelloGame {
    players: Player[] = [
        new Player(Color.White, this, 'Steve'), 
        new Player(Color.Black, this, 'Bill')
    ];

    size: Number = 8;

    board: Piece[][];

    constructor(size: Number = 8) {
        // Init othello board
        this.board = [];
        for(var i = 0; i < size; i++) {
            this.board.push([]);
            for(var j = 0; j < size; j++) {
                this.board[i].push(null);
            }   
        }
    }

    IsInvalidMove(coordinates: { x: Number, y: Number }) {
        // Check if coordinates within bounds of board
        if( coordinates.x < 0 || coordinates.y < 0 || this.size <= coordinates.x || this.size <= coordinates.y ) {
            return false;
        }
        // Check if coordinates point to existing piece
        if( this.board[coordinates.x][coordinates.y] instanceof Piece ) {
            return false
        }
        // Check if valid move according to game.
        return false; // Ignore this line
    }

    RunGame() {
        for(var i = 0; true; i++) {
            if( !this.GameHasValidMoves() ) {
                break;
            }
            // Make current player make move
            this.players[i%2].TakeTurn();
        }
        // Find winner and log him
        let winner = this.calculateWinner() as Player;
        if( winner == null ) {
            console.log('Draw!');
        } else {
            console.log(winner.name);
        }
    }

    // Return's player
    calculateWinner() {
        var counts = { white: 0, black: 0 };
        for(var i = 0; i < 8; i++) {
            for(var j = 0; j < 8; j++) {
                let piece = this.board[i][j];
                if( piece instanceof Piece ) {
                    if( piece.type == Color.White) {
                        counts.white++;
                    } else if( piece.type == Color.Black ) {
                        counts.black++;
                    }
                }
            }   
        }
        if( counts.white == counts.black ) {
            return null;
        } else {
            return this.players[counts.white > counts.black ? 0 : 1];
        }
    }

    // Check to see if either pla
    GameHasValidMoves() {
        /* ... */
        return false;
    }
}

