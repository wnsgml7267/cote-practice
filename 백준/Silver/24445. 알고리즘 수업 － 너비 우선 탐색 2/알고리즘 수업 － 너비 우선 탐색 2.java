import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Deque;
import java.util.StringTokenizer;
public class Main {
	public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        Deque<Integer> q = new ArrayDeque<>();
        int[] visited = new int[n+1];
        q.add(k);
        visited[k] = 1;
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for(int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        int cnt = 1;
        // bfs
        while(!q.isEmpty()) {
            int x = q.poll();
            Collections.sort(graph.get(x), Collections.reverseOrder()); // 내림차순
            for (int num : graph.get(x)) {
                if (visited[num] == 0) { 
                    cnt+=1;
                    visited[num] = cnt;
                    q.add(num);
                }
            }
        }
        for(int i = 1; i <= n; i++) {
            System.out.println(visited[i]);
        }
    }
}