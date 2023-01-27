import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        String[] split = br.readLine().split(" ");
        
        for(int i = 0; i < N; i++){
            arr[i] = Integer.parseInt(split[i]);
        }
        for(int i = 1; i < N; i++){
            int parent = arr[0]; //분모
            int dle = arr[i];
            if (parent >= dle){
                for(int j = parent; j > 1; j--){
                    if (parent % j == 0 && dle % j == 0){
                        parent /= j;
                        dle /= j;
                    } 
                }
            } else {
                for(int j = dle; j > 1; j--){
                    if (parent % j == 0 && dle % j == 0){
                        parent /= j;
                        dle /= j;
                    }  
                }
            }
            System.out.println(parent + "/" + dle);
        }
    }
}