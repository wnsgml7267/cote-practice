import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    private static int N;
    private static int[] arr;
    private static int student_count;
    private static int gender;
    private static int num;
    private static int g;
	public static void main(String[] args) throws Exception{
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    N = Integer.parseInt(br.readLine());
	    arr = new int[N];
	    String[] split = br.readLine().split(" ");
	    for(int i = 0; i < N; i++) {
	        arr[i] = Integer.parseInt(split[i]);
	    }
	    
	    student_count = Integer.parseInt(br.readLine());
	    
	    for(int i = 0; i < student_count; i++) {
	    	String[] split2 = br.readLine().split(" ");
	        gender = Integer.parseInt(split2[0]);        
	        num = Integer.parseInt(split2[1]);
	        if (gender == 1) {
	        	g = num;
	            while(g <= N) {
	                arr[g-1] = Math.abs(arr[g-1] - 1);
	                g += num ;
	                
	                
	            }
	        } else if (gender == 2) {
	            arr[num-1] = Math.abs(arr[num-1] - 1);
	            search(num-1, 1, arr);
	        }
	    }
	    int cnt = 0;
	    for(int a : arr) {
	    	if (cnt != 0 && cnt % 20 == 0) {
	    		System.out.println();
	    	}
	        System.out.print(a + " ");
	        cnt += 1;
	    }
	}
	private static void search(int k, int l, int[] arr) {
	    if (k-l >= 0 && k+l <= N-1) {
	        if(arr[k-l] == arr[k+l]) {
	            arr[k-l] = Math.abs(arr[k-l] - 1);
	            arr[k+l] = Math.abs(arr[k+l] - 1);
	            search(k, l+1, arr);
	        } else {
	        	return;
	        }
	    }

	}
}