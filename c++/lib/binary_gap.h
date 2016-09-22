
#ifndef BIN_GAP
#define BIN_GAP

#include <math.h>

// @return longest binary gap or zero if there are none
// @parameter N 
int bin_gap(int N) {

	int L = log2(N), 
		count = 0, 
		tempGap = 0;;

	// Find the first 1 if there is one
	while( L >= 0 ) {
		if( ((1 << L) & N) ) {
			--L;
			break;
		}
		--L;
	}
	// Start counting the binary gaps
	while( L >= 0 ) {
		if( ((1 << L) & N) ) {
			count = count < tempGap ? tempGap : count;
			tempGap = 0;
		} else {
			++tempGap;
		}
		--L;
	}
	return count;
}


#endif