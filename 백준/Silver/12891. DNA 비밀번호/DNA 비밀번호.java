import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	

	static int S; // 임의로 만든 DNA 문자열 길이
	static int P; // 비밀번호로 사용할 부분 문자열의 길이
	static char[] atgt = {'A', 'C', 'G', 'T'};
	static String make_dna; // dna 문자열 만들기
	static int[] dna = new int[4]; // {0,0,0,0} dna 개수
	static int cnt;
	static boolean bool;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		S = Integer.parseInt(st.nextToken()); // 총 길이
		P = Integer.parseInt(st.nextToken()); // 8, 부분 문자열 길이
		
		StringTokenizer st2 = new StringTokenizer(br.readLine());
		make_dna = st2.nextToken(); // CCTGGATTG, 총 길이
		StringTokenizer st3 = new StringTokenizer(br.readLine());
		for(int i = 0; i < 4; i++) {
			dna[i] = Integer.parseInt(st3.nextToken()); // [2, 0, 1, 1]
		}
//		System.out.println(S);
//		System.out.println(P);
//		System.out.println(make_dna);
//		System.out.println(Arrays.toString(dna));
		bool = true;
		// P개 비교
		for(int i = 0; i < P; i++) {
			for(int j = 0; j < 4; j++) { // A, C, G, T 중에 같은 게 있는지
				if(make_dna.charAt(i) == (atgt[j])) {
					dna[j] -= 1;
				}
			}
		}
//		System.out.println(Arrays.toString(dna));
		check();
		
		// P ~ S 까지 비교 
		for(int i = P; i < S; i++) {
			for(int j =0; j < 4; j++) {
				
				if(make_dna.charAt(i-P) == atgt[j]) {
//					System.out.println(make_dna.charAt(i-P));
					dna[j] += 1;
					
				}
				if(make_dna.charAt(i) == atgt[j]) {
					dna[j] -= 1;
					
				}
			}
			
			check();
		}
		System.out.println(cnt);
	}
	private static void check() {
		bool = true;
		for(int a : dna) {
			if(a > 0) {
				bool = false; 
			}
		}
		if(bool) {
			cnt += 1;
			
			bool = true;
			return;
		}
		return;
	}
}