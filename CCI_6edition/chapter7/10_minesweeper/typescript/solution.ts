
enum MSGameState {
    Playing = 0,
    Lost = 1,
    Won = 2
}

enum MSMoveType {
    Reveal, Flag
}

enum MSSpaceType {
    Blank = 0,
    Bomb = 1,
    Number = 2
}

class MSSpace {
    type: MSSpaceType;
    revealed: Boolean = false;
    flagged: Boolean = false;

    constructor(type: MSSpaceType) {
        this.type = type;
    }
}

class MSNumber extends MSSpace {
    number: Number
    constructor(number: Number) {
        this.number = number;
        this.type = MSSpaceType.Number;
    }
}


class MinesweeperGame {
    m: Number;
    n: Number;
    board: MSSpace[][];
    spacesToReveal: Number;
    gameState: MSGameState = MSGameState.Playing;

    constructor(m: Number, n: Number) {
        this.m = m;
        this.n = n;
        // Used to keep track wether the player has won
        this.spacesToReveal = n * m;
        // Init board
        this.board = [];
        for(var i = 0; i < this.m; i++) {
            var row = [];
            for(var j = 0; j < this.n; j++) {
                row.push(null);
            }    
            this.board.push(row);
        }
        // Generate bombs and populate board
        let totalBombs = (Math.random() * m * n) | 0;
        while(totalBombs-- > 0) {
            let [x, y] = this.generateBombSpace();
            this.board[x][y] = new MSSpace(MSSpaceType.Bomb);
        }
        // Update board spaces for numbers
        for(var x = 0; x < this.m; x++) {
            for(var y = 0; y < this.n; y++) {
                // If board piece is not null its a bomb so skip it.
                if( this.board[x][y] != null ) {
                    continue;
                }
                let bombCount = this.getBombCountForSpace(x,y);
                if( 0 < bombCount ) {
                    this.board[x][y] = new MSNumber(bombCount);
                } else {
                    this.board[x][y] = new MSSpace(MSSpaceType.Blank);
                }
            }    
        }
    }

    /////////////////////////////////////
    // Auxiliary methods

    // Returns the number of bombs given a valid x and y coordinate. Return value ranges between 0 and 8
    private getBombCountForSpace(x: Number, y: Number) {}
    // Generates unique bomb space coordinates using set
    private generateBombSpace() { return [0,0]; }

    // Determines if the game is finished. If it is it will return true for win and false for fail. If the game is still going it will return null.
    private IsGameFinished() {
        return this.spacesToReveal <= 0 ? MSGameState.Won : MSGameState.Playing;
    }
    // Returns the new move the player performed.
    private GetValidPlayerMove() { return { location: [0,0], type: MSMoveType.Reveal }; }

    RunGame() {
        while(true) {
            // Check game state at the beginning of game loop
            if( this.gameState == MSGameState.Won ) {
                console.log("Congrats! You won!");
            } else if ( this.gameState == MSGameState.Lost ) {
                console.log("Game Over. Better luck next time!");
            }

            let { location: [x,y], type } = this.GetValidPlayerMove();
            if( type == MSMoveType.Flag ) {
                this.board[x][y].flagged = !this.board[x][y].flagged;
            } else {
                if( !this.board[x][y].flagged && !this.board[x][y].revealed ) {
                    this.board[x][y].revealed = true;
                    this.spacesToReveal -= 1;
                    // If bomb space, player has lost. Mark loss.
                    if( this.board[x][y].type == MSSpaceType.Bomb ) {
                        this.gameState = MSGameState.Lost;
                    }
                }
            }
            // Determine if game won or still playing assuming player hasn't lost
            if( this.gameState != MSGameState.Lost ) {
                this.gameState = IsGameFinished();
            }
        }
    }

}