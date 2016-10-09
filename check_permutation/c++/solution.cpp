
#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

// Assumes 256 ascii


bool check_permutation_with_sort(string a, string b) {
	int aL = a.size(), bL = b.size();
	if( aL != bL ) {
		return false;
	}
	transform(a.begin(), a.end(), a.begin(), ::tolower);
	transform(b.begin(), b.end(), b.begin(), ::tolower);
	int used[256] = {0};
	
	sort(a.begin(),a.end());
	sort(b.begin(),b.end());

	for(int i = 0; i < aL; i++) {
		if( a[i] != b[i] ) {
			return  false;
		}
	}
	return true;
}


bool check_permutation(string a, string b) {
	int aL = a.size(), bL = b.size();
	if( aL != bL ) {
		return false;
	}
	transform(a.begin(), a.end(), a.begin(), ::tolower);
	transform(b.begin(), b.end(), b.begin(), ::tolower);

	int used[256] = {0};
	
	for(int i = 0; i < aL; i++) {
		++used[a[i]];
		--used[b[i]];
	}
	for(int i = 0; i < 256; i++) {
		if( used[i] ) {
			return false;
		}
	}
	return true;
}


int main(int argc, char const *argv[]) {
	string a,b;
	cin >> a;
	cin >> b;
	cout << check_permutation_with_sort(a,b) << endl;
	return 0;
}
