import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;
public class Solution {
	static int N, M, graph[][];
    static int bCnt, sCnt;
 
    public static void main(String[] args) throws IOException {
 
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
 
        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
 
            N = Integer.parseInt(br.readLine()); // 학생 수 : 정점 수
            M = Integer.parseInt(br.readLine()); // 관계 수 : 간선 수
            graph = new int[N + 1][N + 1];
            
            int i, j;
            for (int m = 1; m <= M; m++) {
                st = new StringTokenizer(br.readLine());
                
                i = Integer.parseInt(st.nextToken());
                j = Integer.parseInt(st.nextToken());
                // 단방향 그래프
                graph[i][j] = 1;
            }
 
            int temp = 0;
            for (int k = 1; k <= N; k++) {
                bCnt = sCnt = 0;
                bBFS(k);
                sBFS(k);
                if(bCnt + sCnt == N - 1) temp++;
            }
            System.out.println("#" + t + " " + temp);
        }
 
    }
 
    // 키 큰 학생 탐색
    private static void bBFS(int start) {
 
        Queue<Integer> q = new LinkedList<>();
        boolean[] visited = new boolean[N + 1];
        q.add(start);
        visited[start] = true;
        
        while(!q.isEmpty()) {
            int k = q.poll();
            for (int i = 1; i <= N; i++) {
                if (graph[k][i] == 1 && !visited[i]) {
                    q.add(i);
                    visited[i] = true;
                    bCnt++;
                }
            }
        }
 
    }
 
    // 키 작은 학생 탐색
    private static void sBFS(int start) { 
 
        Queue<Integer> q = new LinkedList<>();
        boolean[] visited = new boolean[N + 1];
        q.add(start);
        visited[start] = true;
        
        while(!q.isEmpty()) {
            int k = q.poll();
            for (int i = 1; i <= N; i++) {
                if (graph[i][k] == 1 && !visited[i]) {
                    q.add(i);
                    visited[i] = true;
                    sCnt++;
                }
            }
        }
    }
}