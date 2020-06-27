

// #include <iostream>

// using namespace std;






// class S1 {
// 	int *a;
// 	int N;
// 	int top[3];
// public:
// 	S1(int N = 3) {
// 		for(int i = 0; i < 3; i++)
// 			top[i] = i;

// 		if( 3 < N ) {
// 			this->N = N;
// 			a = new int[N];
// 		}
// 	}

// 	void push(int item, int s = 0) {
// 		if( top[s] < N ) {
// 			a[top[s]] = item;
// 			top[s] += 3;
// 		} else {
// 			// Throw error
// 		}
// 	}

// 	int pop(int s = 0) {
// 		if( 3 <= top[s] ) {
// 			top[s] -= 3;
// 			return a[top[s]];
// 		}
// 		return -1;
// 	}

// 	int peek(int s = 0) {
// 		if( 3 <= top[s] ) {
// 			return a[top[s] - 3];
// 		}
// 		return -1;
// 	}

// 	int isEmpty(int s = 0) {
// 		return top[s] < 3;
// 	}
// };


// class S2 {
// 	int *a;
// 	int N;
// 	int top[3];
// 	int base[3];
// public:
// 	S2(int N = 3) {
// 		for(int i = 0; i < 3; i++)
// 			base[i] = top[i] = i * N / 3;

// 		if( 3 < N ) {
// 			this->N = N;
// 			a = new int[N];
// 		}
// 	}

// 	void push(int item, int s = 0) {
// 		bool isvalid = false;
// 		if( s == 0 || s == 1 ) {
// 			isvalid = top[s] < base[s+1];
// 		} else if( s == 3 ) {
// 			isvalid = top[s] < N;
// 		}

// 		if( isvalid ) {
// 			a[top[s]++] = item;
// 		} else {
// 			// Throw error
// 		}
// 	}

// 	int pop(int s = 0) {
// 		if( 3 <= top[s] ) {
// 			top[s] -= 3;
// 			return a[top[s]];
// 		}
// 		return -1;
// 	}

// 	int peek(int s = 0) {
// 		if( 3 <= top[s] ) {
// 			return a[top[s] - 3];
// 		}
// 		return -1;
// 	}

// 	int isEmpty(int s = 0) {
// 		return top[s] < 3;
// 	}
// };



// int main(int argc, char const *argv[]) {
	
// 	S1 *x = new S1(99);
// 	// x->push(65, 2);
// 	cout << x->pop(2) << endl;

// 	return 0;
// }