import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	//결과를 한 번에 출력하기 위한 StringBuilder
	private static StringBuilder sb = new StringBuilder();
	private static int N_switch;
	private static String[] switch_state;
	private static int N_student;
	private static int gender;
	private static int number;
	public static void main(String[] args) throws Exception {

		/*
		 * 1. 입력파일 읽어들이기 
		 */

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		/*
		 * 2. 입력파일 객체화
		 */
		N_switch = Integer.parseInt(in.readLine());
		switch_state = in.readLine().split(" ");
		N_student = Integer.parseInt(in.readLine());
		/*
		 * 3. 알고리즘 풀기
		 */
		for (int i = 0; i < N_student; i++) {
			String[] _string = in.readLine().split(" ");
			gender = Integer.parseInt(_string[0]);
			number = Integer.parseInt(_string[1]);
			switch (gender) {
				case 1:
					man();
					break;
				case 2:
					woman();
					break;
			}
		}
		/*
		 * 4. 정답 출력 
		 */
		int cnt = 0;
	    for(String a : switch_state) {
	    	if (cnt != 0 && cnt % 20 == 0) {
	    		System.out.println();
	    	}
	        System.out.print(a + " ");
	        cnt += 1;
	    }
//		sb.append(Arrays.deepToString(switch_state));
//		System.out.println(sb);
	}
	
	private static void man() {
		int i = 1;
		while (number * i <= N_switch) {
			change(number * i - 1);
			i++;
		}
		
	}
	
	private static void woman() {
		int i = 0;
		change(number-1);
		while(true) {
			i++;
			if ((number-1-i) >= 0 && (number-1+i) < N_switch) {
				if (switch_state[number-1-i].equals(switch_state[number-1+i])) {
					change(number-1-i);
					change(number-1+i);
				} else {
                    break;
                }	
			}
			else {
				break;
			}
		}
		
	}
	private static void change(int i) {
		if (switch_state[i].equals("1")) {
			switch_state[i] = "0";
		}
		else {
			switch_state[i] = "1";
		}
	}	
}