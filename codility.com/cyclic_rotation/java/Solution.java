

class Solution {
	
	public int[] solution(int[] A, int K) {
		if( K == 0) {
			return A;
		}
		
		int B[] = new int[A.length];
		for(int i = 0; i < A.length; i++) {
			B[(i + K) % A.length] = A[i];
		}
		return B;
	}
	

	public static void main(String[] args) {
		
		Solution s = new Solution();
		
		int A[] = new int[5];
		A[0] = 1;
		A[1] = 2;
		A[2] = 3;
		A[3] = 4;
		A[4] = 5;
		
		
		for(int j = 0; j < 6; j++) {
			int B[] = s.solution(A, j);
			for(int i = 0; i < B.length; i++) {
				System.out.print(B[i] +" ");
			}
			System.out.println();
		}
		
	}
}



