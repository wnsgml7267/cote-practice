import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
	static int N;
	static int M;
	static int[][] graph;
	static ArrayList<Integer> chicken_x = new ArrayList<>();
	static ArrayList<Integer> chicken_y = new ArrayList<>();
	static ArrayList<Integer> home_x = new ArrayList<>();
	static ArrayList<Integer> home_y = new ArrayList<>();
	static int[] chicken_size;
	static int[] numbers; // 뽑힌 m개의 치킨집 인덱스 저장할 배열
	static int min_value = 10000000;
	static int sm; // 각 치킨집 조합 M개 마다의 최소 거리 점수 합
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		String[] split = br.readLine().split(" ");
		N = Integer.parseInt(split[0]); // N, N 좌표
		M = Integer.parseInt(split[1]); // 치킨 집 M개 고르기
		graph = new int[N][N];
		
		// graph : 기본 좌표 입력 
		for(int i = 0; i < N; i++) {
			split = br.readLine().split(" ");
			for(int j = 0; j < N; j++) {
				graph[i][j] = Integer.parseInt(split[j]);
			}
		}
		
		chicken_x = new ArrayList<>();
		chicken_y = new ArrayList<>();
		home_x = new ArrayList<>();
		home_y = new ArrayList<>();
		// 치킨집(2) 좌표 뽑아내기.
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				if (graph[i][j] == 2) {
					chicken_x.add(i);
					chicken_y.add(j);
				} else if(graph[i][j] == 1) {
					home_x.add(i);
					home_y.add(j);
				}
			}
		}
		
		// chicken_size : 모든 치킨집들 배열로 기록 0 ~ M-1
		chicken_size = new int[chicken_x.size()];
		for(int i = 0; i < chicken_x.size();i++) {
			chicken_size[i] = i;
		}
		
		// 모든 치킨집들 중 M개의 치킨집 조합으로 뽑아내기
		numbers = new int[M];
		combination(0, 0);
		sb.append(min_value);
		System.out.println(sb);
	}
	private static void combination(int cnt, int start) {
		if(cnt == M) { // 치킨집 M개 뽑았으면 각 집마다 모든 치킨집을 비교해서 최솟값 저장
//			System.out.println(Arrays.toString(numbers));
			sm = 0;
			for(int j = 0; j < home_x.size(); j++) {
				int minv = 1000000;
				for(int k : numbers) {
					minv = Math.min(minv, Math.abs(chicken_x.get(k) - home_x.get(j)) + Math.abs(chicken_y.get(k) - home_y.get(j)));
				}
				sm += minv;
//				System.out.println(sm);
			}
			min_value = Math.min(min_value, sm);
			return;
		}
		
		for(int i = start; i < chicken_x.size(); i++) {
			numbers[cnt] = chicken_size[i]; // 수 하나 뽑음
			combination(cnt+1, i+1);
		}
	}
}