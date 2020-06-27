

class PuzzlePiece {
    id: number;
    imageURL: string;
    constructor(id: number) {
        this.id = id;
    }
}

class JigsawPuzzle {

    pieceIsAdjacent: Set<string>;
    N: number;
    M: number;
    pieces: PuzzlePiece[];
    connectedPieces: Set<PuzzlePiece>;

    constructor(N: number, M: number) {
        this.init(N,M);
    }

    init(N: number, M: number) {
        // Create pieces
        this.pieces = [];
        for(let i = 0; i < N*M; i++) {
            this.pieces.push(new PuzzlePiece(i));
        }
        this.connectedPieces = new Set<PuzzlePiece>();
    }

    getCoordinates(piece: PuzzlePiece) {
        return {
            x: (piece.id / this.N)|0,
            y: (piece.id % this.N)
        }
    }

    fitsWith(pieceA: PuzzlePiece, pieceB: PuzzlePiece) {
        let A = this.getCoordinates(pieceA);
        let B = this.getCoordinates(pieceB);
        let isAdjacentX = Math.abs(A.x - B.x) == 1;
        let isAdjacentY = Math.abs(A.y - B.y) == 1;
        return (isAdjacentX && !isAdjacentY) || (!isAdjacentX && isAdjacentY);
    }

    connectPieces(pieceA: PuzzlePiece, pieceB: PuzzlePiece) {
        // Check if valid pieces
        if( this.N*this.M <= pieceA.id || this.N*this.M <= pieceB.id ) return;
        // Check if pieces are connected
        if( !this.fitsWith(pieceA, pieceB) ) return;
        // Mark pieces as connected
        this.connectedPieces.add(pieceA);
        this.connectedPieces.add(pieceB);
    }
}