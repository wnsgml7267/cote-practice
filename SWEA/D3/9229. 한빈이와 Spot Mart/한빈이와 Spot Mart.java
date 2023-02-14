import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Solution {
	static int[] arr;
	static int answer;
	static int left;
	static int right;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for(int i = 1; i <= T; i++) {
			String[] split = br.readLine().split(" ");
			int N = Integer.parseInt(split[0]);
			int M = Integer.parseInt(split[1]);
			answer = -1;
			arr = new int[N];
			split = br.readLine().split(" ");
			for(int j = 0; j < N; j++) {
				arr[j] = Integer.parseInt(split[j]);
			}
			
			for(int j = 0; j < N; j++) {
				left = arr[j];
				for(int k = j+1; k < N; k++) {
					if ((left + arr[k]) <= M) {
						answer = Math.max(answer, left + arr[k]);
					}
					
				}
			}
			sb.append("#" + i + " " + answer + "\n");
			
//			System.out.println(Arrays.toString(arr));
		}
		System.out.println(sb);
		
	}
}