import java.util.Scanner;

public class Solution {
	static final int MOD = 1234567891;
	static long ft[] = new long[1000001];
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int t = 1; t <= T; t++) {
			int N = sc.nextInt();
			int R = sc.nextInt();
			
			ft[0] = 1;
			for(int i = 1; i <= 1000000; i++) {
				ft[i] = ft[i-1] * i % MOD;
			}
			
			// n! * (((n-r)! * r!) % p)^(p-2)
			long p1 = ft[N];
			long p2 = (ft[N-R] * ft[R]) % MOD;
			long p3 = cal(p2, MOD-2);
			
			System.out.println("#" + t + " " + p1 * p3 % MOD);
			
		}
	}
	private static long cal(long n, long r) {
		if(r == 1) return n;
		long x = cal(n, r/2) % MOD;
		if (r % 2 == 0) return x * x % MOD;
		else return ((x * x) % MOD * n) % MOD;
	}
}