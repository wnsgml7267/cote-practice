import java.util.Arrays;
import java.util.Scanner;

public class Main {
	
	// nPr
	private static int N;
	private static int R;
	private static int[] numbers;
	private static boolean[] isSelected;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		R = sc.nextInt();
		numbers = new int[R];
		isSelected = new boolean[N+1];
		
		permutation(0);
	}
	
	private static void permutation(int cnt) {
		if (cnt == R) {
			for(int num : numbers) {
				System.out.print(num + " ");
			}
			System.out.println();
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