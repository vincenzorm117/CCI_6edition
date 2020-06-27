
class Song {
    value: number;
    name: string;
    constructor(value,name) {
        this.value = value;
        this.name = name;
    }
}

class PlaySongHandler {
    song: Song;
    progress: number;
    time: number;

    constructor() {}

    finishedPlayingSong() {}
    hasSong() {}
    isPlaying() {}
    play() {}
    pause() {}
    stop() {}
    changeSong(song: Song) {
        this.song = song;
        this.progress = 0;
        this.time = 0;
    }
}

class JukeBox {

    availableSongs: Song[];
    queuedSongs: Song[];
    currentSong: Song;
    credit: number;
    storedChange: number;
    songHandler: PlaySongHandler;

    constructor() {
        this.songHandler = new PlaySongHandler();
        this.currentSong = null;
        this.credit = 0;
        setInterval(this.loop.bind(this), 1000)
    }

    loop() {
        // Check if complete
        if( this.songHandler.finishedPlayingSong() ) {
            this.songHandler.changeSong(this.getNextSong());
            this.songHandler.play();
        }
    }

    addCredit(credit: number) {
        this.credit += credit;
    }

    cancelSelection() {
        this.credit = 0;
    }

    selectSong(song: Song) {
        if( this.credit < song.value ) return false;
        this.credit -= song.value;
        this.storedChange += song.value;
        this.queuedSongs.push(song)
    }

    isPlaying() {}
    getCurrentSong() {}

    getNextSong() {
        if( this.queuedSongs.length <= 0 ) return;
        this.currentSong = this.queuedSongs.shift();
        return this.currentSong;
    }
}