import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;



public class Main {
	static int L; // 뽑을 개수
	static int C; // 전체 알파벳 수
	static char[] L_list;
	static char[] C_list;
	static int mo; // 모음 개수
	static int ja; // 자음 개수
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		L = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		L_list = new char[L];
		C_list = new char[C];
		
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < C; i++) {
			C_list[i] = st.nextToken().charAt(0);
			
		}
		Arrays.sort(C_list);
		combination(0,0);
	}
	
	static void combination(int cnt, int start) {
		// 기저 부분
		if(cnt == L) { // 
			if(isValid(L_list)) {
				System.out.println(L_list);
			}
			return;
		}
			
		// 유도 부분
		for(int i = start; i < C; i++) {
			L_list[cnt] = C_list[i];
			combination(cnt + 1, i + 1);
		}
	}
	static boolean isValid(char[] arr) {
		mo = 0;
		ja = 0;
		for(char alp : arr) {
			if(alp == 'a' || alp == 'e' || alp == 'i' || alp == 'o' || alp == 'u') {
				mo += 1;
			} else {
				ja += 1;
			}
		}
		if (mo >= 1 && ja >= 2) {
			return true;
		} else {
			return false;
		}
	}
	
	
}