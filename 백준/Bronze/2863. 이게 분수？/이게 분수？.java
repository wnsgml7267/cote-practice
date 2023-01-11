
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double[] arr = new double[4];
        for(int i=0; i<4; i++)
            arr[i]=sc.nextDouble();
        double max=0;
        int ans=0;
        for(int i=0; i<4; i++){
            double A=arr[0];
            double B=arr[1];
            double C=arr[2];
            double D=arr[3];
            if(max<A/C+B/D){
                max=A/C+B/D;
                ans=i;
            }
            arr[0]=C;
            arr[1]=A;
            arr[2]=D;
            arr[3]=B;

        }
        System.out.println(ans);
    }
}
