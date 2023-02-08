import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int M;
	static int[][] arr;
	static int sm;
	static int x1;
	static int x2;
	static int y1;
	static int y2;
	static int[] answer;
	static int cnt;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken()); // 표의 크기
		M = Integer.parseInt(st.nextToken()); // 합을 구해야 하는 횟수
		arr = new int[N][N];
		answer = new int[M];
//		sm = 0; // 누적 합
		
		for(int i = 0; i < N; i++) {
			StringTokenizer st2 = new StringTokenizer(br.readLine());
			sm = 0;
			for(int j = 0; j < N; j++) {
				arr[i][j] = sm + Integer.parseInt(st2.nextToken());
				sm = arr[i][j];
			}
		}
		
//		System.out.println(Arrays.deepToString(arr));

		for(int i = 0; i < M; i++) {
			StringTokenizer st3 = new StringTokenizer(br.readLine());
			x1 = Integer.parseInt(st3.nextToken());
			y1 = Integer.parseInt(st3.nextToken());
			x2 = Integer.parseInt(st3.nextToken());
			y2 = Integer.parseInt(st3.nextToken());
			cnt = 0;
			// x1좌표 부터 ~ x2좌표까지
			for (int j = 0; j < x2 - x1 + 1; j++) {
				if (y1 == 1) cnt += arr[x1-1+j][y2-1];
				else cnt += arr[x1-1+j][y2-1] - arr[x1-1+j][y1-2];
//				System.out.println(cnt);
			}
			//x1 or x2 가 1이면
			answer[i] = cnt;
			
		}
		for(int fd : answer) {
			System.out.println(fd);
		}
//		x1 -= 1;
//		y1 = N;	
		
		// start가 1번 일 때와, start == end 일 때 예외처리 해줄 것.
		// x1, y1
	}
}