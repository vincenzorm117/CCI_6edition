


class HashTable<A,B> {

    private array: B[][];

    constructor() {
        this.array = [
            [],[],[],[],[],[],[]
        ]
    }

    private hash(key: A): Number {
        /* Need hash function here. My code on the next line is just placeholder. */
        return ((Math.random()*this.array.length)|0) % this.array.length
    }

    size() {
        var size = 0;
        for(var subArray of this.array) {
            size += subArray.length;
        }
        return size ;
    }

    isEmpty() {
        var size = 0;
        for(var subArray of this.array) {
            size += subArray.length;
        }
        return size == 0;
    }

    remove(key: A) {
        var index = this.hash(key);
        var subArray = this.array[index];
        // get index of item
        var subArrayIndex = -1;
        for(var i = 0; i < subArray.length; i++) {
            if( subArray[i].key == key ) {
                subArrayIndex = i;
                break;
            }
        }
        if( subArrayIndex < 0 ) {
            return null;
        }
        var returnValue = subArray[subArrayIndex];
        // Move last element to place of removed element
        subArray[subArrayIndex] = subArray.pop();
        return returnValue;
    }

    get(key: A) {
        var index = this.hash(key);
        var subArray = this.array[index];
        for(var storedValue in subArray) {
            if( storedValue.key == key ) {
                return storedValue.value;
            }
        }
        return null;
    }

    set(key: A, value: B) {
        var index = this.hash(key);
        var subArray = this.array[index];
        for(var storedValue in subArray) {
            if( storedValue.key == key ) {
                storedValue.value = value;
                return;
            }
        }
        subArray.push({ key, value });
    }
}

var hash = new HashTable<string, Number>();

hash.set('Apples', 5);
hash.set('Bananas', 11);
hash.set('Cherries', 3);

console.log(hash.get('Bananas'));