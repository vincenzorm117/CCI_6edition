
#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

// Assumes 256 ascii
bool is_unique_with_map(string s) {
	int L = s.size();
	if( 256 < L ) {
		return false;
	}
	transform(s.begin(), s.end(), s.begin(), ::tolower);
	bool used[256] = {false};
	
	for(int i = 0; i < L; i++) {
		if( used[s[i]] ) {
			return false;
		}
		used[s[i]] = true;
	}
	return true;
}


int main(int argc, char const *argv[]) {
	string s;
	cin >> s;
	cout << is_unique_with_map(s) << endl;
	return 0;
}
