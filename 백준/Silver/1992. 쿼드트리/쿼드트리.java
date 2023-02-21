import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;



public class Main {
	private static int N;
	private static String[][] graph;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		graph = new String[N][N];
		for(int i = 0; i < N; i++) {
			String[] split = br.readLine().split("");
			for(int j = 0; j < N; j++) {
				graph[i][j] = split[j];
			}
		}
		conquer(0,0,N);
	}
	
	private static void conquer(int x, int y, int size) {
		String num = graph[x][y];
		for(int i = x; i < x + size; i++) {
			for(int j = y; j < y + size; j++) {
				if(!graph[i][j].equals(num)) {
					System.out.print('(');
					conquer(x, y, size/2);
					conquer(x, y + size/2, size/2);
					conquer(x + size/2 , y, size/2);
					conquer(x + size/2, y + size/2, size/2);
					System.out.print(')');
					return;
				}
				
			}
		}
		if (num.equals("0")) {
			System.out.print('0');
			return;
		} else {
			System.out.print('1');
			return;
		}
		
	}
}