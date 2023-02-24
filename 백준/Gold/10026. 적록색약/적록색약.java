import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	
	static int N; // 구역 (행열)
	static char[][] graph;
	static int normal_count; // 정상인의 구역
	static int special_count; // 적록색약인의 구역
	static boolean[][] normal_visit;
	static boolean[][] special_visit;
	static int[] dx = {1,-1,0,0};
	static int[] dy = {0,0,1,-1};
	
	static Queue<Point> q = new LinkedList<Point>();
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			
		N = Integer.parseInt(br.readLine());
		graph = new char[N][N];
		
		normal_visit = new boolean[N][N];
		special_visit = new boolean[N][N];
		
		for(int i = 0; i < N; i++) {
			String st = br.readLine();
			for(int j = 0; j < N; j++) {
				graph[i][j] = st.charAt(j);
			}
		}
		
		normal_count = 0;
		// 정상인 탐색
		for(int i = 0; i < N; i++) {
			  for(int j = 0; j < N; j++) {
				  if(graph[i][j] == 'R' && normal_visit[i][j] == false) {
					  bfs(i,j,'R');
					  normal_count += 1;
				  } else if(graph[i][j] == 'G' && normal_visit[i][j] == false) {
					  bfs(i,j,'G');
					  normal_count += 1;
				  } else if(graph[i][j] == 'B' && normal_visit[i][j] == false) {
					  bfs(i,j,'B');
					  normal_count += 1;
				  }
			  }
		}
		
		
		
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				if(graph[i][j] == 'R') {
					graph[i][j] = 'G';
				}
			}
		}
		for(int i = 0; i < N; i++) {
			  for(int j = 0; j < N; j++) {
				  if(graph[i][j] == 'G' && special_visit[i][j] == false) {
					  bfs2(i,j,'G');
					  special_count += 1;
				  } else if(graph[i][j] == 'B' && special_visit[i][j] == false) {
					  bfs2(i,j,'B');
					  special_count += 1;
				  }
			  }
		}
//		System.out.println(Arrays.deepToString(graph));
		System.out.print(normal_count + " ");
		System.out.println(special_count);
		
	}
	private static void bfs(int a,int b, char alp){
		q.add(new Point(a,b));
		normal_visit[a][b] = true;
		while(!q.isEmpty()) {
			Point p = q.poll();
			for(int i = 0; i < 4; i++) {
				int nx = p.x + dx[i];
				int ny = p.y + dy[i];
				if (0 <= nx && nx < N && 0 <= ny && ny < N) {
					if(graph[nx][ny] == alp && normal_visit[nx][ny] == false) {
						normal_visit[nx][ny] = true;
						q.add(new Point(nx, ny));
					}
				}
			}
			
		}
	}
	private static void bfs2(int a,int b, char alp){
		q.add(new Point(a,b));
		special_visit[a][b] = true;
		while(!q.isEmpty()) {
			Point p = q.poll();
			for(int i = 0; i < 4; i++) {
				int nx = p.x + dx[i];
				int ny = p.y + dy[i];
				if (0 <= nx && nx < N && 0 <= ny && ny < N) {
					if(graph[nx][ny] == alp && special_visit[nx][ny] == false) {
						special_visit[nx][ny] = true;
						q.add(new Point(nx, ny));
					}
				}
			}
			
		}
	}
}