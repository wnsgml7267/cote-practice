import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	
	static int N;
	static int R;
	static int[] answer;
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] split = br.readLine().split(" ");
		N = Integer.parseInt(split[0]);
		R = Integer.parseInt(split[1]);
		answer = new int[R]; 
		comb(0,1);
		
		
	}
	
	private static void comb(int cnt, int start) { // 횟수, 주사위 시작번호
		
		if(cnt == R) {
			for(int i : answer) {
				System.out.print(i + " ");
			}
			System.out.println();
			return;
		}
		for(int i = start; i <= N; i++) {
			answer[cnt] = i;
			comb(cnt+1, i+1);
		}	
	}
}