import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int T;
	static int[][] arr;
	static boolean[] isSelected;
	static int mn;
	static int x;
	static int y;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		T = Integer.parseInt(br.readLine());
		arr = new int[T][2];
		isSelected = new boolean[T];
		mn = 10000000;
		for(int i = 0; i < T; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int j = 0; j < 2; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
//		System.out.println(Arrays.toString(arr[0]));
		gs(0);
		System.out.println(mn);
			
	}
	private static void gs(int cnt) {
		
		if(cnt == T) {
			x = 1;
			y = 0;
			for(int j = 0; j < T; j++) {		
				if(isSelected[j]) {
					
//					for(int k = 0; k < Arrays.toString(arr[j]).length(); k++) {
					x *= arr[j][0];
					y += arr[j][1];
//						System.out.println(arr[j][0]);
//						System.out.println(arr[j][1]);
//						System.out.print(Arrays.toString(arr[j]));
//					}
//					System.out.println("차이 : " + (y-x));
					mn = Math.min(mn, Math.abs(x-y));
				}
			}
//			System.out.println();
			return;
		}
		
		isSelected[cnt] = true;
		gs(cnt + 1);
		
		isSelected[cnt] = false;
		gs(cnt + 1);
	}
	
}