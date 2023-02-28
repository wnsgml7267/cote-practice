import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
	
	static int T = 10; // 테스트 케이스 10개
	static int[][] graph;// (from, to) 쌍을 저장할 2차원 배열
	static Queue<Integer> q; // bfs 탐색할 큐
	static int[] visited; // 연락을 이미 했는지 방문 체크용
	static int max; // 최댓값 저장
	static ArrayList<Integer> arr; // 레벨별 최댓값 저장
	static int l; // 데이터 길이
	static int start; // 시작점
	static StringBuilder sb;
	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		sb = new StringBuilder();
		
		// 테스트 케이스는 무조건 10개
		for(int t = 1; t <= T; t++) {
			visited = new int[101]; // 최대 인원 1~100
			graph = new int[101][101];
			StringTokenizer st = new StringTokenizer(br.readLine());
			l = Integer.parseInt(st.nextToken());
			start = Integer.parseInt(st.nextToken());
			
			st = new StringTokenizer(br.readLine());
			for(int i = 0; i < l/2; i++) {
				int from = Integer.parseInt(st.nextToken());
				int to = Integer.parseInt(st.nextToken());
				
				graph[from][to] = 1; // 연락 가능 체크
			}
			sb.append("#" + t + " ");
			bfs(start); // 시작점부터 bfs탐색	
			
		}
		System.out.println(sb);
	}
	private static void bfs(int x) {
		arr = new ArrayList<>();
		q = new ArrayDeque<>();
		q.add(x); // 큐에 삽입
		visited[x] = 1; // 방문 체크
		while(!q.isEmpty()) {
			int q_size = q.size();
			max = 0; // 레벨별 최댓값 초기화
			for(int i = 0; i < q_size; i++) { // 같은 레벨의 시작점
				int cur = q.poll();
				for(int j = 1; j < 101; j++) {
					if(graph[cur][j] == 1 && visited[j] == 0) { // 연락 가능하고, 방문하지 않았으면
						q.add(j);
						visited[j] = 1;
						max = Math.max(max, j);
					}
				}
			}
			arr.add(max);
		}
		sb.append(arr.get(arr.size()-2) + "\n");
	}
}