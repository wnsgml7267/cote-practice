import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;



public class Solution {
	
	static int N;
	static int W;
	static int H;
	static int[][] graph;
	static int[][] copy; // graph 복사본
	static int min_count; //다 부순 후 남은 벽돌 개수 최솟값 초기화
	static int[] input; //중복조합으로 뽑을 0~W-1 
	static int[] numbers; // 중복조합으로 0~W-1 중에 N개 뽑기
	static Deque<Integer> arr;
	static int count;
	
	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		
		int T = Integer.parseInt(br.readLine());
		for(int t = 1; t <= T; t++) {
			min_count = 10000000;
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken()); // 떨어트리는 벽돌 개수
			W = Integer.parseInt(st.nextToken()); // 가로
			H = Integer.parseInt(st.nextToken()); // 세로
			
			input = new int[W];
			numbers = new int[N];
			graph = new int[H][W];
			for(int i = 0; i < W; i++) {
				input[i] = i;
			}
			for(int i = 0; i < H; i++) {
				st = new StringTokenizer(br.readLine(), " ");
				for(int j = 0; j < W; j++) {
					graph[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			comb(0,0); // 중복조합
			System.out.println("#" + t + " " + min_count);
		}
	}
	
	static void comb(int cnt, int start) {
		if(cnt == N) {
			// 배열 복사
			copy = new int[H][W];
			for(int i = 0; i < H; i++) {
				copy[i] = graph[i].clone();
			}
//			System.out.println(Arrays.toString(numbers));
			for (int num : numbers) {
				play(num);
				int mm;
				//벽돌 한 번 다 부쉈으니 벽돌 내리기
				for(int n = 0; n < W; n++) {
					int mode = 0;
					arr = new ArrayDeque<>();
					mm = 0;
					for(int m = H-1; m >= 0; m--) {
						// 0보다 큰 공중에 있는 벽돌들을 담는다.
						if(mode == 1 && copy[m][n] > 0) {
							arr.add(copy[m][n]);
							
						} else if(mode == 0) {
							if(copy[m][n] == 0) { // 중간에 빈 부분
								mm = m; // x 좌표 저장
								mode = 1; // 모드 변경
							}
						}
					}
					// 만약 arr가 비어있는게 아니면 빈 공간이 있다는 것
					if(!arr.isEmpty()) {
						int ct = 0;
						int size = arr.size();
						for(int o = mm; o >= 0; o--) {
							if (size == ct) {
								copy[o][n] = 0;
							} else {
								copy[o][n] = arr.poll();
								ct += 1;
							}
						}
					}
				}
				
			}
			// 최소벽돌개수 초기화
			count = 0;
			for(int i = 0; i < H; i++) {
				for(int j = 0; j < W; j++) {
					if (copy[i][j] > 0) { // 남은 벽돌 개수
						count += 1;
					}
				}
			}
			min_count = Math.min(min_count, count);
			
			return;
		}
		for(int i = 0; i < W; i++) {
			numbers[cnt] = input[i];
			comb(cnt + 1, i);
		}
	}
	// 
	static void play(int x) {
		for(int i = 0; i < H; i++) {
			if (copy[i][x] == 1) {
				copy[i][x] = 0;
				return;
			} else if(copy[i][x] > 1) {
				bomb(i,x);
				return;
			}
		}
	}
	static void bomb(int x, int y) {
		int scale = copy[x][y]-1; // 상하좌우 부술 갯수
		copy[x][y] = 0;
		for(int i = 1; i <= scale; i++) {
			int[] dx = {i,-i,0,0};
			int[] dy = {0,0,i,-i};
			for(int j = 0; j < 4; j++) {
				int nx = dx[j] + x;
				int ny = dy[j] + y;
				if(0 <= nx && nx < H && 0 <= ny && ny < W) {
					if(copy[nx][ny] == 1) {
						copy[nx][ny] = 0;
					} else if(copy[nx][ny] > 1) {
						bomb(nx,ny);
					}
				}
			}
		}
	}
}