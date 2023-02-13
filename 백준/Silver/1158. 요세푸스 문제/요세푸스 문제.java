import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
public class Main {
	private static StringBuilder sb = new StringBuilder();

	public static void main(String args[]) throws Exception {

		/**
		 * 0. 입력파일 읽어들이기
		 */

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		/**
		 * 1. 입력 파일 객체화
		 */
		String[] split = in.readLine().split(" ");
		int N = Integer.parseInt(split[0]);
		int K = Integer.parseInt(split[1]);

		/**
		 * 2. 알고리즘 풀기
		 */
		// 1번부터 N번까지 사람 리스트에 넣기
		Queue<Integer> queue = new ArrayDeque<>();
		for (int i = 1; i <= N; i++) {
			queue.offer(i);
		}

		sb.append("<");
		
		// N명의 사람이 모두 제거될 때까지 반복
		while (queue.size() != 1) {
			int person = -1;
			for (int i = 1; i < K; i++) {
				person = queue.poll();
				queue.offer(person);
			}
			
			// K번째 사람 제거
			int remove = queue.poll();
			sb.append(remove).append(", ");
		}

		// 마지막 사람 출력
		sb.append(queue.poll()).append(">");

		/**
		 * 3. 정답 출력
		 */

		System.out.print(sb);

	}
}