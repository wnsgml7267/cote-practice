import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	
	static int[] arr; // 1~N 집합
	
	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		
		int T = Integer.parseInt(br.readLine());
		for(int t = 1; t <= T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			
			arr = new int[n+1];
			for(int i = 1; i <= n; i++) {
				arr[i] = i; // 자기 루트 노드 가리키기
			}
			
			System.out.print("#" + t + " ");
			for(int i = 0; i < m; i++) {
				st = new StringTokenizer(br.readLine(), " ");
				int idx = Integer.parseInt(st.nextToken());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				
				// 합집합
				if (idx == 0) {
					union(a, b);
				// 같은 집합인지 여부 ? 1 : 0
				} else {
					if (find(a) == find(b)) {
						System.out.print(1);
					} else {
						System.out.print(0);
					}
				}
			}
			System.out.println();
		}
	}
	
	static int find(int x) {
		if (x == arr[x]) {
			return x;		}
		
		return arr[x] = find(arr[x]);
	}
	
	static boolean union(int x, int y) {
		int aRoot = find(x);
		int bRoot = find(y);
		if (aRoot == bRoot) {
			return false;
		}
		// b를 a에 담는다
		arr[bRoot] = aRoot;
		return true;
	}
}