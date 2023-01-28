import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
        
		// 테스트 케이스
		for(int i = 0; i < T; i++) {
     
			// 동전 가지수
			int N = Integer.parseInt(br.readLine());
			String[] split = br.readLine().split(" ");
            
			// 동전 리스트
			int[] arr = new int[N];
			for(int j = 0; j < N; j++) {
				arr[j] = Integer.parseInt(split[j]);
			}
			// 목표 금액
			int M = Integer.parseInt(br.readLine());
			
			// dp[0 ~ M+1]
			int[] dp = new int[M+1];
			dp[0] = 1;
			
			// 메모이제이션
			for(int coin : arr) {
				for(int target = 1; target <= M; target++) {
					if (target >= coin) {
						dp[target] += dp[target - coin];
					}
				}
			}
			System.out.println(dp[M]);
		}
	}
}
