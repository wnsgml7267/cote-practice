import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int N;
	static int L;
	static int R;
	static int[][] graph;
	static boolean[][] visited;
	static ArrayList<Integer> arr_x;
	static ArrayList<Integer> arr_y;
	private static Queue<Point> queue;
	private static int days;
	private static int sum;
	private static int[] dx = { -1, 1, 0, 0 };
	private static int[] dy = { 0, 0, -1, 1 };
	private static boolean bool;
	private static int ans;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] split = br.readLine().split(" ");
		N = Integer.parseInt(split[0]);
		L = Integer.parseInt(split[1]);
		R = Integer.parseInt(split[2]);
		
		graph = new int[N][N];
		
		for(int i = 0; i < N; i++) {
			split = br.readLine().split(" ");
			for(int j = 0 ; j < N; j++) {
				graph[i][j] = Integer.parseInt(split[j]);
			}
		}
		while(true) {
			bool = false;
			visited = new boolean[N][N];
			for(int k = 0; k < N; k++) {
				for(int l =0 ; l < N; l++) {
					if(visited[k][l] == false) {
						bfs(k, l);
					}
				}
			}
			if(!bool) {
				break;
			} else {
				days += 1;
			}
		}
		System.out.println(days);
		
	}
	
	
	private static void bfs(int row, int column) {
		queue = new LinkedList<Point>();
		queue.add(new Point(row, column));
		sum = graph[row][column];
		ans = 1;
		arr_x = new ArrayList<>();
		arr_y = new ArrayList<>();
		arr_x.add(row);
		arr_y.add(column);
		visited[row][column] = true;

		while(!queue.isEmpty()) {
		    Point p = queue.poll();
		    for(int i = 0; i < 4; i++) {
		    	int nx = dx[i] + p.x;
		    	int ny = dy[i] + p.y;
		    	if((0 <= nx && nx < N && 0 <= ny && ny < N) && visited[nx][ny] == false) {
		    		int div = Math.abs(graph[nx][ny] - graph[p.x][p.y]);
		    		if(L <= div && div <= R) {
		    			visited[nx][ny] = true;
		    			sum += graph[nx][ny];
		    			ans += 1;
		    			queue.add(new Point(nx, ny));
		    			arr_x.add(nx);
		    			arr_y.add(ny);
		    		}
		    	}
		    } 
		}
		if(ans > 1) {
			bool = true;
			int dv = sum / ans;
			for(int i = 0; i < arr_x.size(); i++) {
				graph[arr_x.get(i)][arr_y.get(i)] = dv; 
			}
		}
	}
}