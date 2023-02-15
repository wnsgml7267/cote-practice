import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[][] graph = new int[101][101];
		int answer = 0;
		for(int i = 0; i < N; i++) {
			String[] split = br.readLine().split(" ");
			int x = Integer.parseInt(split[0]);
			int y = Integer.parseInt(split[1]);
			
			for(int j = x; j < x + 10; j++) {
				for(int k = y; k < y + 10; k++) {
					graph[j][k] = 1;
				}
			}
		}
		
		for(int i = 0; i < 101; i++) {
			for(int j =0; j < 101; j++) {
				if (graph[i][j] == 1) {
					answer += 1;
				}
			}
		}
		System.out.println(answer);
	}

}