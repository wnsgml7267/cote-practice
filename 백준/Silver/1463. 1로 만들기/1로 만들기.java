import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new  BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int K = N > 3 ? N+1 : 4;
		int[] arr = new int[K];
		arr[2] = 1;
		arr[3] = 1;
		
		for(int i = 4 ; i <= N ; i++) {
			int min = arr[i-1];
			if(i%2 == 0) min = min > arr[i/2] ? arr[i/2] : min;
			if(i%3 == 0) min = min > arr[i/3] ? arr[i/3] : min;
			
			arr[i] = min+1;
		}
		System.out.println(arr[N]);
	}
}