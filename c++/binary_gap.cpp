
#include <iostream>
#include <math.h>

using namespace std;


// @return longest binary gap or zero if there are none
// @parameter N 
int solution(int N) {

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




int main(int argc, char const *argv[]) {

	int x = 0;
	cin >> x;
	cout << solution(x) << endl;

	return 0;
}