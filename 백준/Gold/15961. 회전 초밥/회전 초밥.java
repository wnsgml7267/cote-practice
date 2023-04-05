import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	//접시의 수, 초밥의 가짓수, 연속해서 먹는 접시수, 쿠폰번호
		static int N, d, k, c;
		static int ans = 0;
		static int arr[], visited[];
		public static void main(String[] args) throws IOException {
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			d = Integer.parseInt(st.nextToken());
			k = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());
			arr = new int[N];
			visited = new int[d+1];
			for (int i = 0; i < N; i++) {
				arr[i]=Integer.parseInt(br.readLine());
			}
			int total=0;
			for (int i = 0; i < k; i++) {
				if(visited[arr[i]] == 0) total++;
				visited[arr[i]]++;
			}
			ans = total;
			
			for (int i = 1; i < N; i++) {
				if(ans<=total) {
					if(visited[c]==0) {
						ans = total+1;
					}else {
						ans = total;
					}
				}
				//
				visited[arr[i-1]]--;
				if(visited[arr[i-1]]==0)total--;
				
				if(visited[arr[(i+k-1)%N]]==0)total++;
				visited[arr[(i+k-1)%N]]++;
			}
			System.out.println(ans);
		}

}