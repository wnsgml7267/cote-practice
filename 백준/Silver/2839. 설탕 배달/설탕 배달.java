import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int cnt = 1000000;
		for(int i = 0; i < N / 3; i++) {
			int a = (i+1) * 3;
			for(int j = 0; j < N / 5; j++) {
				int b =(j+1) * 5;
				if (a+b == N) {
					int num = (i+1) + (j+1);
					cnt = Math.min(cnt, num);
				}
			}
		}
		if(N%3 == 0) {
			cnt = Math.min(cnt, N/3);
		}
		if(N%5 == 0) {
			cnt = Math.min(cnt, N/5);
		}
		if (cnt == 1000000) {
			System.out.println(-1);
		} else {
			System.out.println(cnt);
		}
		
		
		
	}
}