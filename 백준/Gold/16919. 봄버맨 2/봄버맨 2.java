import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int R; // 행
	static int C; // 열
	static int N; // 시간 초
	static int[][] graph;
	static ArrayDeque<int[]> bomb;
	static int[] dx = {1,-1,0,0};
	static int[] dy = {0,0,1,-1};
	static int time = 1;
	static char tmp = 'd'; // d : 폭발, s : 설치
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		N = Integer.parseInt(st.nextToken());
		
		graph = new int[R][C];
		bomb = new ArrayDeque<>();
		for (int i = 0; i < R; i++) {
			String s = br.readLine();
			for (int j = 0; j < C; j++) {
				graph[i][j]=s.charAt(j)=='.'?-1:0;
			}
		}
		if (N == 1) N = 1;
		else if (N % 2 == 0) N = 2;
		else if (N % 2 == 1) {
			if (N % 4 == 1) N = 5;
			else N = 3;
		}
		while(true) {
			if (time == N) {
				for(int k = 0; k < R; k++) {
					for(int l = 0; l < C; l++) {
						if (graph[k][l] == -1) System.out.print('.');
						else System.out.print('O'); 
					}
					System.out.println();
				}
				break;
			}
			// 폭발했으면 설치하기
			if (tmp == 'd') {
				set();
				time++;
				tmp = 's';
			} else {
				destroy();
				time++;
				tmp = 'd';
			}
		}
//		System.out.println(time);
	}
	private static void destroy() {
		while(!bomb.isEmpty()) {
			int[] b_arr = bomb.poll();
			int x = b_arr[0];
			int y = b_arr[1]; 
			graph[x][y] = -1;
			for(int i = 0 ; i < 4; i++) {
				int nx = dx[i] + x;
				int ny = dy[i] + y;
				if(0 <= nx && nx < R && 0 <= ny && ny < C && graph[nx][ny] == 0) {
					graph[nx][ny] = -1;
				}
			}
		}
		
	}
	private static void set() {
		for(int i = 0 ; i < R; i++) {
			for(int j = 0 ; j < C; j++) {
				if(graph[i][j] == 0) { // 폭탄 위치 받기
					bomb.add(new int[] {i, j});
				} else { // 폭탄 설치
					graph[i][j] = 0;
				}
			}
		}
		
	}
	
}