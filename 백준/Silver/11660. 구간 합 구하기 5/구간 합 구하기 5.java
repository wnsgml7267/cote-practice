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
			System.out.println(sum(x2, y2) - sum(x1-1, y2) - sum(x2, y1-1) + sum(x1-1, y1-1));
		}
	}

	public static int sum(int i, int j) {
		int sol = 0;
		while(i > 0) {
			int k = j;
			while(k > 0) {
				sol += tree[i][k];
				k -= (k & -k);
			}
			i -= (i & -i);
		}
		return sol;
	}

	public static void update(int i, int j, int diff) {
		while(i<tree.length) {
			int k = j;
			while(k < tree[i].length) {
				tree[i][k] += diff;
				k += (k & -k);
			}
			i += (i & -i);
		}
	}
}