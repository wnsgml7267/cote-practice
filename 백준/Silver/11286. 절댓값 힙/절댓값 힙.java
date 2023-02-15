import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		PriorityQueue<Integer> plus_heap = new PriorityQueue<>(); // 최소 힙
		PriorityQueue<Integer> minus_heap = new PriorityQueue<>(Collections.reverseOrder()); // 최대 힙
		
		int N = Integer.parseInt(br.readLine());
		for (int i = 0; i < N; i++) {
			int x = Integer.parseInt(br.readLine());
			
			// 양수 힙
			if (x > 0) {
				plus_heap.add(x);
			// 음수 힙
			} else if (x < 0) {
				minus_heap.add(x);
				
			} else if (x == 0) {
				// 1. 두 힙이 존재할 경우
				if(!plus_heap.isEmpty() && !minus_heap.isEmpty()) {
					//값이 같다면 minus 힙에서 빼기
					if(plus_heap.peek() == Math.abs(minus_heap.peek())) {
						System.out.println(minus_heap.poll());
					}
					//값이 다르다면 작은 힙에서 빼기
					else if(plus_heap.peek() < Math.abs(minus_heap.peek())) { 
						System.out.println(plus_heap.poll());
					} else if(plus_heap.peek() > Math.abs(minus_heap.peek())) { 
						System.out.println(minus_heap.poll());
					}
				}
				// 2. 한 힙만 존재할 경우
				else if(!plus_heap.isEmpty() && minus_heap.isEmpty()) {
					System.out.println(plus_heap.poll());
				} else if(plus_heap.isEmpty() && !minus_heap.isEmpty()) {
					System.out.println(minus_heap.poll());
				}
				// 3. 아무것도 존재하지 않을 경우
				else if(plus_heap.isEmpty() && minus_heap.isEmpty()) {
					System.out.println(0);
				}
			}
		}
	}
}