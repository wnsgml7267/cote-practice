import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int M;
	static int[][] tree;
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		
		int[][] arr = new int[N+1][N+1];
		// 펜윅 트리
		tree = new int[N+1][N+1];
		// 수 N개 입력받기
		for(int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 1; j <= N; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		// 펜윅 트리 구성하기
		for(int i = 1; i <= N; i++) {
			for(int j = 1; j <= N; j++) {
				update(i, j, arr[i][j]);
			}
		}

		
		for(int i = 0; i < M; i++) {
			st=new StringTokenizer(br.readLine());
			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			System.out.println(sum(tree, x2, y2) - sum(tree, x1-1, y2) - sum(tree, x2, y1-1) + sum(tree, x1-1, y1-1));
		}
	}

	public static int sum(int[][] tree, int idx_x, int idx_y) {
		int sol = 0;
		while(idx_x>0) {
			int temp_idx_y = idx_y;
			while(temp_idx_y>0) {
				sol += tree[idx_x][temp_idx_y];
				temp_idx_y -= (temp_idx_y&-temp_idx_y);
			}
			idx_x -= (idx_x&-idx_x);
		}
		return sol;
	}

	public static void update(int idx_x, int idx_y, int diff) {
		while(idx_x<tree.length) {
			int temp_idx_y = idx_y;
			while(temp_idx_y<tree[idx_x].length) {
				tree[idx_x][temp_idx_y] += diff;
				temp_idx_y += (temp_idx_y&-temp_idx_y);
			}
			idx_x += (idx_x&-idx_x);
		}
	}
	
}