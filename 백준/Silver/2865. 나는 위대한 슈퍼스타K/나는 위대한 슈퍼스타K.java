
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] split1 = br.readLine().split(" ");
        int N = Integer.parseInt(split1[0]);
        int M = Integer.parseInt(split1[1]);
        int K = Integer.parseInt(split1[2]);
        
        // N명 만큼
        ArrayList<Double> db = new ArrayList<>();
        for(int i=0;i<N;i++) {
        	db.add(0.0);
        }
        
        // M개의 장르
        for(int i=0;i<M;i++) {
        	String[] split = br.readLine().split(" ");
        	for(int j=0;j<K*2;j+=2) {
        		int idx = Integer.parseInt(split[j])-1;
        		double score = Double.parseDouble(split[j+1]);
        		if(db.get(idx) < score) {
        			db.set(idx, score);
        		}
        	}
        }
        Collections.sort(db, Collections.reverseOrder());

        int cnt = 0;
        double answer = 0;
        for(int i = 0; i < db.size();i++) {
        	answer += db.get(i);
        	cnt++;
        	if (cnt == K) {
        		break;
        	}
        }
        System.out.printf("%.1f",answer);
    }
}
