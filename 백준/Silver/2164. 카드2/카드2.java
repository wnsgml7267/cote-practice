import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	
	static int N;
	static Queue<Integer> queue;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		N = sc.nextInt();
		queue = new ArrayDeque<>();
		for(int i = 1; i < N+1; i++) {
			queue.add(i);
		}
		
		while(queue.size()>1) {
			queue.poll(); // 앞 삭제
			queue.add(queue.poll()); //뒤로 보냄
		}
		System.out.println(queue.poll());

	}
}