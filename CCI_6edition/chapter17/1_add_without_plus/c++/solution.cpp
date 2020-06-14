
#include <iostream>
#include <bitset>
#include <assert.h>


using namespace std;


int shiftBitByLength(int bit, int position) {
    while( position > 0 ) {
        bit = bit << 1;
        position = position >> 1;
    }
    return bit;
}


int add(int a, int b) {
    int aBit,
        bBit,
        currBit,
        result = 0,
        carryBit = 0,
        position = 0;

    // Use long since for ints ((long)INT_MAX) << 1 becomes negative
    //  and when it is right shifted it just produces 1s on the left hand side.
    long countDown = ((long)INT_MAX) << 1;

    // We can't use a for loop from 1 to 32 since we can't use arithmetic operators
    while( countDown > 0 ) {
        // Grab current bits
        aBit = a & 1;
        bBit = b & 1;
        // Calculate current bit value and the carryBit
        currBit = (aBit ^ bBit ^ carryBit) & 1;
        carryBit = (aBit & bBit) | (aBit & carryBit) | (bBit & carryBit);
        // Aggregate value on result
        result = shiftBitByLength(currBit, position) | result;
        // Shift numbers down to get next bits
        a = a >> 1;
        b = b >> 1;
        // Shift countdown down to get closer to the loop end
        countDown = countDown >> 1;
        // Update position to new location to set next bit on.
        position = position > 0 ? (position << 1) : 1;
    }

    // Add carryBit if it is 1 and if a and b were not
    //  negative numbers.
    //  Last carry bit isn't added for negative numbers.
    if( carryBit > 0 && a >= 0 && b >= 0) {
        carryBit = shiftBitByLength(carryBit, position);
        result = carryBit | result;
    }

    return result;
}


int main() {
    int solution = -1;
    for(int a = -10; a < 10; a++) {
        for(int b = -10; b < 10; b++) {
            solution = add(a,b);
            assert(solution == (a+b));
            // Print results
            cout << a << " " << b << " " << (a+b) << " " << solution << endl;
            cout << bitset<32>(a) << endl;
            cout << bitset<32>(b) << endl;
            cout << bitset<32>(solution) << endl;
        }
    }
    return 0;
}