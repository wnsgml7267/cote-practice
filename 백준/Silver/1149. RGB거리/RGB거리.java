import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[][] arr = new int[n][3];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < 3; j++) {
				arr[i][j] = sc.nextInt();
			}
		}
		int[][] dp = new int[n][3];
		dp[0][0] = arr[0][0];
		dp[0][1] = arr[0][1];
		dp[0][2] = arr[0][2];
		
		for(int i = 1; i < n; i++) {
			for(int j = 0; j < 3; j++) {
				if (j == 0) {
					dp[i][j] = Math.min(dp[i-1][j+1], dp[i-1][j+2]) + arr[i][j];
				} else if (j == 1) {
					dp[i][j] = Math.min(dp[i-1][j-1], dp[i-1][j+1]) + arr[i][j];
				} else if (j == 2) {
					dp[i][j] = Math.min(dp[i-1][j-1], dp[i-1][j-2]) + arr[i][j];
				}
				
			}
		}
		long min_value = 100000000;
		for (int i = 0; i < 3; i++) {
			min_value = Math.min(min_value, dp[n-1][i]);
		}
		System.out.println(min_value);
	}
}