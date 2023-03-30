import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int[][] graph = new int[9][9];
	static ArrayList<int[]> zero_arr;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for(int i = 0; i < 9; i++) {
			String split = br.readLine();
			for( int j = 0 ; j < 9; j++) {
				graph[i][j] = split.charAt(j) - '0';
			}
		}
		zero_arr = new ArrayList<>();
		for(int i = 0 ; i < 9; i++) {
			for(int j = 0 ; j < 9; j++) {
				if(graph[i][j] == 0) { // 자리가 비어있는 좌표 모두 저장
					zero_arr.add(new int[] {i,j});
					
				}
			}
		}
		back(0);
		
	}
	
	static void back(int n) {
		// 빈칸을 다 채웠으면 출력
		if (zero_arr.size() == n) {
			for(int i = 0; i < 9; i++) {
				for(int j = 0; j < 9; j++) {
					System.out.print(graph[i][j]);
				}
				System.out.println();
			}
			System.exit(0);
		}
		
		int x = zero_arr.get(n)[0];
		int y = zero_arr.get(n)[1];
		// 4. 1~3 true일 경우, 값 선택. 그 후, 백트래킹
		for(int k = 1; k <= 9; k++) {
			if (width(x, k) && height(y, k) && square(x, y, k)) {
				graph[x][y] = k;
				back(n+1);
				graph[x][y] = 0;
			}
		}
	}	
	// 1. 가로 판단
	static boolean width(int r, int n) {
		for(int i = 0 ; i<9; i++) {
			if (graph[r][i] == n) return false; 
		}
		return true;
	}
	//2. 세로 판단
	static boolean height(int c, int n) {
		for(int i = 0; i < 9; i++) {
			if (graph[i][c] == n) return false;
		}
		return true;
	}		
	// 3. 3x3 판단
	static boolean square(int r, int c, int n) {
		int rx = r/3*3;
		int ry = c/3*3;
		for(int i = rx; i < rx+3; i++) {
			for(int j = ry; j < ry+3; j++) {
				if(graph[i][j] == n) return false;
			}
		}
		return true;
	}		
}