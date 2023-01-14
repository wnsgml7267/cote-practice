import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int cnt = 0;
        for(int i=1;i<=n;i++){
            for(int j=0;j<=i;j++){
                cnt += (i+j);
            }
        }
        System.out.print(cnt);
    }
}
