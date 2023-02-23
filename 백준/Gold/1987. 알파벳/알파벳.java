
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int R, C;
	static int[][] graph;
	static boolean[] visited = new boolean[26];
	static int[] dx = { -1, 1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };
	static int ans = 0;
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		graph = new int[R][C];
		for (int i = 0; i < R; i++) {
			String str = br.readLine();
			for (int j = 0; j < C; j++) {
				graph[i][j] = str.charAt(j) - 'A';
			}
		}

		dfs(0, 0, 0);

		System.out.println(ans);
	}
	
	private static void dfs(int x, int y, int cnt) {
		if(visited[graph[x][y]]) {
			ans = Math.max(ans, cnt);
			return;
		} else {
			visited[graph[x][y]] = true;
			for(int i = 0 ; i < 4; i ++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				
				if(0 <= nx && nx < R && 0 <= ny && ny < C ) {
					dfs(nx, ny, cnt + 1);
				}
			}
			visited[graph[x][y]] = false;
			
		}
	}
}
