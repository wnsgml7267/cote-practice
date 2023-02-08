import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int M;
	static int[] arr;
	static int sm;
	static int start;
	static int end;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken()); // 수의 개수
		M = Integer.parseInt(st.nextToken()); // 합을 구해야 하는 횟수
		arr = new int[N];
		sm = 0;
		StringTokenizer st2 = new StringTokenizer(br.readLine());
		for(int i = 0; i < N; i++) {
			arr[i] = sm + Integer.parseInt(st2.nextToken());
			sm = arr[i];
		}

		for(int i = 0; i < M; i++) {
			StringTokenizer st3 = new StringTokenizer(br.readLine());
			start = Integer.parseInt(st3.nextToken());
			end = Integer.parseInt(st3.nextToken());
			if (start == 1) {
				System.out.println(arr[end-1]);
			} else {
				System.out.println(arr[end-1] - arr[start-2]);

			}
		}
		
	}
}