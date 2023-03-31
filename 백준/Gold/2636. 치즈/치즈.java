import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static int[][] map;
	static boolean[][] visited;
	static int cheeseCnt;
	static int[] rangeX = { -1, 0, 1, 0 };
	static int[] rangeY = { 0, 1, 0, -1 };

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		map = new int[N][M];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		visited = new boolean[N][M];

		int ans;
		for (ans = 0; isCheese(); ans++) {
			for (boolean[] arr : visited) {
				Arrays.fill(arr, false);
			}
			visited[0][0] = true;
			cheeseCnt = 0;

			DFS(0, 0);
		}

		System.out.println(ans + "\n" + cheeseCnt + "\n");
	}

	// 치즈 존재 여부
	public static boolean isCheese() {
		// 공기로 변경
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (map[i][j] == 2) {
					map[i][j] = 0;
				}
			}
		}

		// 치즈 존재 여부 확인
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (map[i][j] == 1) {
					return true;
				}
			}
		}

		return false;
	}

	// 공기와 맞닿은 치즈 탐색
	public static void DFS(int x, int y) {
    
		for (int i = 0; i < 4; i++) {
      int dx = x + rangeX[i];
		  int dy = y + rangeY[i];
      if(0 <= dx && dx < N && 0 <= dy && dy < M){
  			if (!visited[dx][dy]) {
  				visited[dx][dy] = true;
  				if (map[dx][dy] == 1) {
  					map[dx][dy] = 2;
  					cheeseCnt++;
  				} else {
  					DFS(dx, dy);
  				}
  			}
      }
		}
	}
}