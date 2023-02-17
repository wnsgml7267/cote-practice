import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	static int[] numbers;
	static int[] arr;
	public static void main(String[] args) throws Exception{
		// 9개 중에 7개 뽑아서 100 맞추기. 맞추고 한 줄로 출력
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		arr = new int[9];
		for(int i = 0; i < 9; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
//		System.out.println(Arrays.toString(arr));
		
		numbers = new int[7];
		
		combination(0,0);
	}
	private static void combination(int cnt, int start) {
		if(cnt == 7) {
			int sm = 0;
//			System.out.println(Arrays.toString(numbers));
			for(int i : numbers) {
				sm += arr[i];
			}
			if (sm == 100) {
				for(int j : numbers) {
					System.out.println(arr[j]);
				}
			}
			return;
		}
		
		for(int i = start; i < 9; i++) {
			numbers[cnt] = i;
			combination(cnt + 1, i + 1);
		}
	}
}