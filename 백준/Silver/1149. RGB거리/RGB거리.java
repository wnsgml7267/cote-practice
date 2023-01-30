import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[][] dp = new int[n][3];
		for(int i = 0; i < n; i++) {
			String[] split = br.readLine().split(" ");
			for(int j = 0; j < 3; j++) {
				dp[i][j] = Integer.parseInt(split[j]);
			}
		}
		
		for(int i = 1; i < n; i++) {
			for(int j = 0; j < 3; j++) {
				if (j == 0) dp[i][j] = Math.min(dp[i][j] + dp[i-1][j+1], dp[i][j] + dp[i-1][j+2]);
				else if (j == 1) dp[i][j] = Math.min(dp[i][j] + dp[i-1][j-1], dp[i][j] + dp[i-1][j+1]);
				else if (j == 2) dp[i][j] = Math.min(dp[i][j] + dp[i-1][j-1], dp[i][j] + dp[i-1][j-2]);
			}
		}
		int answer = 10000000;
		for(int i = 0; i < 3; i++) {
			answer = Math.min(answer, dp[n-1][i]);
		}
		System.out.println(answer);
	}
}  

