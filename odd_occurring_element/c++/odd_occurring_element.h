

#ifndef ODD_OCCURRING_ELEMENT
#define ODD_OCCURRING_ELEMENT

#include <vector>

// @return element that occurs an odd number of times
// @parameter vector A which has all elements with an even multiplicity except
// 			 one element which has odd multiplicty
int odd_occurring_element(std::vector<int> &A) {
	int curr = 0, L = A.size();
	for(int i = 0; i < L; i++) {
		curr = curr ^ A[i];
	}
	return curr;
}

#endif