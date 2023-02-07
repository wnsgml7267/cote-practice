import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	
	// nPr
	private static int N;
	private static int R;
	private static int[] numbers;
	private static boolean[] isSelected;
	private static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] split = br.readLine().split(" ");
		N = Integer.parseInt(split[0]);
		R = Integer.parseInt(split[1]);
		numbers = new int[R];
		isSelected = new boolean[N+1];
		
		permutation(0);
		
		System.out.println(sb);
	}
	
	private static void permutation(int cnt) {
		if (cnt == R) {
			for(int num : numbers) {
				sb .append(num + " ");
//				System.out.print(num + " ");
			}
			sb.append("\n");
//			System.out.println();
			return;
		}
		
		for (int i = 1; i <= N; i++  ) {
			if (isSelected[i]) {
				continue;
			}
			numbers[cnt] = i;
			isSelected[i] = true;
			permutation(cnt + 1);
			isSelected[i] = false;
		}	
	}
}