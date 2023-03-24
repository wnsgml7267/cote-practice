import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        
        for(int tc = 1; tc <= T ; tc++) {
            int K = Integer.parseInt(br.readLine());
            PriorityQueue<Long> queue = new PriorityQueue<>();
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int i = 0 ; i < K; i++) {
                queue.offer(Long.parseLong(st.nextToken()));
            }
            
            // solve
            long result = 0;
            long n1, n2;
            while(queue.size() > 1) {
                
                n1 = queue.poll();
                n2 = queue.poll();

                queue.offer(n1+n2);
                result += n1+n2;
            }
            
            sb.append(result).append('\n');
        }
        System.out.println(sb);
    }
}