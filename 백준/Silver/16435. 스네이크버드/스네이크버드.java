import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.zip.InflaterInputStream;

public class Main {
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader((new InputStreamReader(System.in)));
		String[] split = br.readLine().split(" ");
		
		int N = Integer.parseInt(split[0]); // 과일 개수
		int L = Integer.parseInt(split[1]); // 초기 길이
		
		int[] arr = new int[N];
		split = br.readLine().split(" ");
		for(int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(split[i]);
		}
		
		Arrays.sort(arr);
		
		for(int i = 0; i < N; i++) {
			if (arr[i] <= L) {
				L += 1;
			} else {
				break;
			}
		}
		System.out.println(L);
	}
}