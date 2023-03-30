import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt(); // 물품의 수
		int K = sc.nextInt(); // 버틸 수 있는 무게
		
		int[] weights = new int[N+1]; // 무게
		int[] values = new int[K+1]; // 가치
		int[][] dp = new int[N+1][K+1];
		
		for (int i = 1; i <= N; i++) {
			weights[i] = sc.nextInt();
			values[i] = sc.nextInt();
		}
		
		for (int i = 1; i <= N; i++) { // 물품
			for( int j = 1; j <= K; j++) { // 무게
				// 버틸 수 있는 무게를 초과 한다면
				if (weights[i] > j) {
					dp[i][j] = dp[i-1][j];
				} else {
					dp[i][j] = Math.max(dp[i-1][j], values[i] + dp[i-1][j-weights[i]]);
				}
			}
		}
		
		System.out.println(dp[N][K]);
		
	}
}