import java.io.*;
import java.util.*;
 
public class Main {
    
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        Deque<int[]> stack = new ArrayDeque<>();
        for(int i = 1; i <= n; i++) {
            int top = Integer.parseInt(st.nextToken());
            while(!stack.isEmpty()) {
                if(stack.peekLast()[1] >= top) {
                    System.out.print(stack.peekLast()[0] + " ");
                    break;
                }
                stack.pollLast();
            }
            if(stack.isEmpty()) {
                System.out.print("0 ");
            }
            stack.add(new int[] {i, top});
        }
    }
}  
