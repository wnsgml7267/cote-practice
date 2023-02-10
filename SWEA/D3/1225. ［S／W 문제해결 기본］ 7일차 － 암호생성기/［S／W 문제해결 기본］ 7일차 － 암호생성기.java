import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

public class Solution {
	static Queue<Integer> queue;
	static int N;
	
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();

		for(int i = 1 ; i <= 10; i++) {
			sb.append("#" + i + " ");
			queue = new ArrayDeque<>();
			N = sc.nextInt();
			
			
			for(int j = 0; j < 8; j++) {	
				queue.add(sc.nextInt());
			}
			int num = 1;
			while(queue.peek() > 0) {
				if (queue.peek() - num <= 0) {
					queue.poll();
					queue.add(0);
					break;
				} else {
					queue.add(queue.poll()-num);
				}
				num = num % 5 + 1;

			}
			
			for(int k = 0; k < 8; k++) {
				sb.append(queue.poll() + " ");
			}
			sb.append("\n");

		}
		System.out.println(sb);
	}
}