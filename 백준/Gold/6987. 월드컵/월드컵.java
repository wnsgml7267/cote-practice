import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
/*
	총 경기를 할 수 있는 경우의 수 : 6국가(0~5) 중 2개 조합(combination)의 경우
 */
public class Main {
	
	private static int[][] arr = new int[6][3];
	private static int[] arr2 = new int[18];
	private static int[] numbers = new int[2];
	private static int[] input = {0, 1, 2, 3, 4, 5};
	private static int[][] play = {{0,2}, {1,1}, {2,0}};
	private static int ans;
	private static ArrayList<Integer> numbers_x = new ArrayList<>();
	private static ArrayList<Integer> numbers_y = new ArrayList<>();
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		
		combination(0,0);
		
		
		for(int i = 0; i < 4; i++) {
			arr2 = new int[18];
			String[] split = br.readLine().split(" ");
			for(int j = 0; j < 18; j++) {
				arr2[j] = Integer.parseInt(split[j]);
			}
			int k2 = 0;
			for(int j = 0; j < 6; j++) {
				for(int k = 0; k < 3; k++) {
					arr[j][k] = arr2[k2++];
				}
				
			}
			ans = 0;
			back(0);
			System.out.print(ans + " ");
	
		}

	}
	
	private static void back(int round) {
		
		if(round == 15) { // 모든 경기를 다 치뤘을 때
			ans = 1;
			lo:
			for(int c = 0; c < 6; c++) {
				for(int d = 0; d < 3; d++) {
					if(arr[c][d] != 0) {
						ans = 0;
						break lo;
					}
				}
			}
			return;
		}
		
		// 경기 붙일 라운드
		int t1 = numbers_x.get(round);
		int t2 = numbers_y.get(round);
		
		for(int i = 0; i < 3; i++) {
			if (arr[t1][play[i][0]] > 0 && 0 < arr[t2][play[i][1]]) {
				arr[t1][play[i][0]] -= 1;
				arr[t2][play[i][1]] -= 1;
				back(round + 1);
				arr[t1][play[i][0]] += 1;
				arr[t2][play[i][1]] += 1;
			}
		}
		
	}
	
	private static void combination(int cnt, int start) {
		
		if (cnt == 2) {
			// numbers : 6국가가 대결하는 총 경우의 수 (15 라운드)
			numbers_x.add(numbers[0]);
			numbers_y.add(numbers[1]);
			return;
		}
		for(int i = start; i < 6; i++) {
			numbers[cnt] = input[i];
			combination(cnt + 1, i + 1);
		}
		
		
	}
}