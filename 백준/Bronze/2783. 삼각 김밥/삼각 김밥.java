import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] split = br.readLine().split(" ");
        int N = Integer.parseInt(split[0]);
        int M = Integer.parseInt(split[1]);
        int T = Integer.parseInt(br.readLine());
        double minPrice = (double)N/M * 1000;
        //테스트케이스 T번 반복
        for(int i=0;i<T;i++){
            String[] split2 = br.readLine().split(" ");
            int X = Integer.parseInt(split2[0]);
            int Y = Integer.parseInt(split2[1]);
            double price = (double)X/Y * 1000;
            minPrice = Math.min(minPrice, price);
        }
        System.out.println(minPrice);
    }
}
