import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	static int N; // 행
	static int M; // 열
	static int T; // 가동 시간
	static int[][] graph;
	static int cleaner_top; // 공기청정기 위 좌표
	static int cleaner_bottom; // 공기청정기 아래 좌표
	static int[][] dirty; // 미세먼지 
	static int[] dx = {1,-1,0,0};
	static int[] dy = {0,0,1,-1};
	static int diff_count;
	static int tmp; // 이전에 가진 값
	static int temp; // 현재 가진 값
	static int result;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] split = br.readLine().split(" ");
		
		N = Integer.parseInt(split[0]);
		M = Integer.parseInt(split[1]);
		T = Integer.parseInt(split[2]);
		
		graph = new int[N][M];
		for(int i = 0; i < N; i++) {
			split = br.readLine().split(" ");
			for(int j = 0; j < M; j++) {
				graph[i][j] = Integer.parseInt(split[j]);
			}
		}
		
		// 공기 청정기 위에꺼랑 아래꺼 위치 찾기
		for(int i = 0; i < N; i++) {
			if(graph[i][0] == -1) {
				cleaner_top = i;
				break;
			}
		}
		for(int i = N-1; i >= 0; i--) {
			if(graph[i][0] == -1) {
				cleaner_bottom = i;
				break;
			}
		}
		// T초 만큼 반복하기.
		for(int w = 0; w < T; w++) {
			
			// 미세먼지 확산시키기 위한 배열 생성
			dirty = new int[N][M];
			dirty[cleaner_top][0] = -1;
			dirty[cleaner_bottom][0] = -1;
			// 미세먼지 찾고 확산하기.
			for(int j = 0; j < N; j++) {
				for(int k = 0; k < M; k++) {
					// 미세먼지를 찾았으면 확산시키자.
					if(graph[j][k] > 0) {
						diff(j,k);
					}
				}
			}
			
			// 확산 완료 후, 그래프에 최종 결과를 넣어주고
			for(int  j = 0; j < N; j++) {
				for(int k = 0; k < M; k++) {
					graph[j][k] = dirty[j][k];
				}
			}
			
			// 윗 공기 청정기 돌리기
			tmp = 0;
			// 오른쪽으로 밀기
			for(int j = 1; j < M; j++) {
				// 현재 가진 미세먼지 양을 temp에 잠시 넣어둔다.
				temp = graph[cleaner_top][j];
				
				// 이전에 가졌던 값을 넣어준다.
				graph[cleaner_top][j] = tmp;
				
				// 현재 가진 값을 이전에 가졌던 값으로 바꿔준다.
				tmp = temp;
			}
			// 위로 올라가야하니까 행을 0까지 줄여줘야함
			for(int j = cleaner_top-1; j >= 0; j--) {
				// 현재 가진 미세먼지 양을 temp에 잠시 넣어둔다.
				temp = graph[j][M-1];
				
				// 이전에 가졌던 값을 넣어준다.
				graph[j][M-1] = tmp;
				
				// 현재 가진 값을 이전에 가졌던 값으로 바꿔준다.
				tmp = temp;
			}
			
			//왼쪽
			for(int j = M-2; j >= 0; j--) {
				// 현재 가진 미세먼지 양을 temp에 잠시 넣어둔다.
				temp = graph[0][j];
				
				// 이전에 가졌던 값을 넣어준다.
				graph[0][j] = tmp;
				
				// 현재 가진 값을 이전에 가졌던 값으로 바꿔준다.
				tmp = temp;
			}
			
			//아래
			for(int j = 1; j < cleaner_top; j++) {
				// 현재 가진 미세먼지 양을 temp에 잠시 넣어둔다.
				temp = graph[j][0];
				
				// 이전에 가졌던 값을 넣어준다.
				graph[j][0] = tmp;
				
				// 현재 가진 값을 이전에 가졌던 값으로 바꿔준다.
				tmp = temp;
			}
			
			
			// 아래 공기 청정기 돌리기
			tmp = 0;
			
			// 오른쪽으로 밀기
			for(int j = 1; j < M; j++) {
				// 현재 가진 미세먼지 양을 temp에 잠시 넣어둔다.
				temp = graph[cleaner_bottom][j];
							
				// 이전에 가졌던 값을 넣어준다.
				graph[cleaner_bottom][j] = tmp;
							
				// 현재 가진 값을 이전에 가졌던 값으로 바꿔준다.
				tmp = temp;
			}
			
			// 아래
			for(int j = cleaner_bottom+1; j < N; j++) {
				// 현재 가진 미세먼지 양을 temp에 잠시 넣어둔다.
				temp = graph[j][M-1];
				
				// 이전에 가졌던 값을 넣어준다.
				graph[j][M-1] = tmp;
				
				// 현재 가진 값을 이전에 가졌던 값으로 바꿔준다.
				tmp = temp;
			}
			
			//왼쪽
			for(int j = M-2; j >= 0; j--) {
				// 현재 가진 미세먼지 양을 temp에 잠시 넣어둔다.
				temp = graph[N-1][j];
				
				// 이전에 가졌던 값을 넣어준다.
				graph[N-1][j] = tmp;
				
				// 현재 가진 값을 이전에 가졌던 값으로 바꿔준다.
				tmp = temp;
			}
			
			// 위
			for(int j = N-2; j > cleaner_bottom; j--) {
				temp = graph[j][0];
				graph[j][0] = tmp;
				tmp = temp;
			}
			
		}
		// 저장된 배열(graph) 상태 출력하기
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				if(graph[i][j] != -1) result += graph[i][j];
			}
		}
		System.out.println(result);
//		System.out.println(Arrays.deepToString(graph));
	}
	static void diff(int x, int y) {
		// 주변에 몇개가 확산되는지 부터 확인하기.
		diff_count = 0;
		for(int i = 0; i < 4; i++) {
			int nx = dx[i] + x;
			int ny = dy[i] + y;
			// 좌표 범위 내에 있고, 바이러스가 확산될 수 있는 장소인지(공기청정기 위치면 안됨.) 확인
			if(0 <= nx && nx < N && 0 <= ny && ny < M && graph[nx][ny] >= 0) {
				// 확산을 위해 만든 배열 dirty에다가 확산된 미세먼지 양을 계속 더해줌
				dirty[nx][ny] += graph[x][y] / 5;
				diff_count += 1; // 주변에 몇개 확산되는지 확인(퍼지기전 보스의 값을 정하기 위해서)
			}
		}
		// n, m에 남는 미세먼지 양
		dirty[x][y] += graph[x][y] - (graph[x][y] / 5) * diff_count;
	}
}