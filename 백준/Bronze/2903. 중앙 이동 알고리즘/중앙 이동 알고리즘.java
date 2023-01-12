import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[16];
        arr[0] = 4;
        int two = 2;
        int one = 1;
        int cnt = 0;
        for(int i=1;i<16;i++){
            two += one;
            cnt = two * two;
            arr[i] = cnt;
            one = one * 2;
        }
        System.out.print(arr[n]);
    }
}
