import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = 5;
        int answer = 0;
        int answer2 = 0;
        for(int i = 0; i < 5; i++){
            String[] split = br.readLine().split(" ");
            int sum = 0;
            for(int j = 0; j < 4; j++){
                sum += Integer.parseInt(split[j]);
            }
            if (answer < sum){
                answer = sum;
                answer2 = i+1;
            }
        }
        System.out.print(answer2 + " " + answer);
    }
}
