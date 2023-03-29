import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static StringTokenizer st;
	static int n;
	static int[][] graph;
	static boolean[] visited;
	static int min;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		graph = new int[n+1][n+1];
		visited = new boolean[n+1];
		min = Integer.MAX_VALUE;
		
		for (int i = 1; i <= n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= n; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for (int i = 1; i <= n; i++) {
			dfs(i, i, 0, 0);
		}
		System.out.println(min);
	}
	// dfs
	static void dfs(int start, int i, int cnt, int sum) {
		// 모두 순회 후 제자리로 돌아왔을 경우
		if (cnt == n && start == i) {
			min = Math.min(min, sum);
		}
		
		for (int j = 1; j <= n; j++) {
			if (graph[i][j] == 0) continue; // 자기 자신 or 갈 수 없는 경우 pass
			
			if(!visited[i] && graph[i][j] > 0) {
				visited[i] = true;
				// 백트래킹
				sum += graph[i][j];
				dfs(start, j, cnt + 1, sum);
				sum -= graph[i][j];
				visited[i] = false;
			}
			
		}
	}
	
	
}