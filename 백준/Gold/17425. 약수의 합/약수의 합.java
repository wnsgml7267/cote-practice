
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		// 약수의 배수들의 합
		long[] dp = new long[1000001];
		Arrays.fill(dp, 1);
		
		// 누적합
		long[] sum_arr = new long[1000001];
		
		// 약수의 배수들의 합
		for(int i = 2; i<=1000000; i++) {
			int j = 1;
			while (i*j <= 1000000) {
				dp[i*j] += i;
				j += 1;
			}
		}
		
		// 누적합
		for (int i = 1; i <= 1000000; i++) {
			sum_arr[i] = sum_arr[i-1] + dp[i];
		}
		
		int T = Integer.parseInt(br.readLine());
		// 테스트 케이스
		for(int i = 0; i < T; i++) {
			int N = Integer.parseInt(br.readLine());
			sb.append(sum_arr[N]).append("\n");
		}
		System.out.println(sb);
	}
}
