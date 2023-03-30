import java.awt.Point;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class Main {
	static int N;
	static int M;
	static int graph[][];
	static int max_value = 0; // 안전영역 최댓값
	static int wall_cnt = 0; // 벽 개수
	static int[] dx = {1,-1,0,0};
	static int[] dy = {0,0,1,-1};
	static Deque<Point> q;
	static int[][] visited;
	static int[][] copy_graph;
	static int safe_cnt;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] split = br.readLine().split(" ");
		N = Integer.parseInt(split[0]);
		M = Integer.parseInt(split[1]);
		graph = new int[N][M];
		for(int i = 0; i < N; i++) {
			split = br.readLine().split(" ");
			for(int j = 0; j < M; j++) {
				graph[i][j] = Integer.parseInt(split[j]);
			}
		}
		dfs(0);
		System.out.println(max_value);
	}
	
	static void dfs(int cnt) {
		
		// 벽이 3개일 경우
		if(cnt == 3) {
			// 바이러스 확산
			virus();
			// 안전영역 구하기
			// 최댓값 초기화
		} else {
			for(int i = 0; i < N; i++) {
				for(int j = 0; j < M; j++) {
					if(graph[i][j] == 0) {
						graph[i][j] = 1; // 벽 생성
						cnt += 1; // 벽 개수 증가
						dfs(cnt);
						cnt -= 1;
						graph[i][j] = 0;
					}
				}
			}
		}
	}
	
	static void virus() {
		copy_graph = new int[N][M];
		safe_cnt = 0;
		for (int i = 0; i < N; i++) {
			for(int j = 0; j < M; j ++) {
				copy_graph[i][j] = graph[i][j];
			}
		}

		visited = new int[N][M];
		q = new ArrayDeque<>();
		
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				if (copy_graph[i][j] == 2 && visited[i][j] == 0) { // 방문하지 않은 바이러스 확인
					visited[i][j] = 1;
					q.add(new Point(i, j));
					while(!q.isEmpty()) {
						Point p = q.poll();
						for(int k = 0; k < 4; k++) {
							int nx = dx[k] + p.x;
							int ny = dy[k] + p.y;
							if(0 <= nx && nx < N && 0 <= ny && ny < M) {
								if(copy_graph[nx][ny] == 0 && visited[nx][ny] == 0) {
									copy_graph[nx][ny] = 2;
									visited[nx][ny] = 1;
									q.add(new Point(nx, ny));
								}
							}
						}
					}
				}
			}
		}
		
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				if (copy_graph[i][j] == 0) {
					safe_cnt += 1;
				}
			}
		}
		max_value = Math.max(max_value, safe_cnt);
	}
	// 벽 3개를 백트래킹하며 바이러스를 BFS로 퍼트리며 안전 영역의 최대 크기를 지속적으로 최댓값으로 초기화
	
	// 1. 벽 3개 백트래킹
	// 2. 바이러스 퍼트림
	// 3. 최댓값 초기화

}