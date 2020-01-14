import java.util.*;

public class EditDistance implements EditDistanceInterface {
     
    int c_i, c_d, c_r;
    static int MAX = Integer.MAX_VALUE;
    static int UNDEF = -1;

    public EditDistance (int c_i, int c_d, int c_r) {
        this.c_i = c_i;
        this.c_d = c_d;
        this.c_r = c_r;
    }

    public int[][] getEditDistanceDP(String s1, String s2) {
    	int m = s1.length();
    	int n = s2.length();
    	int[][] result = new int[m+1][n+1];
    	for(int i=0; i< n+1; i++){
    		result[0][i] = i * this.c_i;
    	}
    	for(int i =0; i< m+1; i++){
    		result[i][0] = i * this.c_d;
    	}
    	for(int i=1; i < m+1; i++){
    		for(int j= 1; j< n+1; j++){
    			int min_tmp = Math.min(result[i-1][j] + this.c_d, result[i][j-1] + this.c_i);
    			if(s1.charAt(i-1) == s2.charAt(j-1)){
    				result[i][j] = Math.min(result[i-1][j-1], min_tmp);
    			}
    			else{
    				result[i][j] = Math.min(result[i-1][j-1] + this.c_r, min_tmp);
    			}
    		}
    	}
        return result;
    }

    public List<String> getMinimalEditSequence(String s1, String s2) {
        LinkedList<String> ls = new LinkedList<> ();
        int[][] d = this.getEditDistanceDP(s1, s2);
        int m=s1.length(),n =s2.length();    		
        while(d[m][n]!= 0){
        	if(n==0){
        		m--;
        		ls.addFirst("delete("+ (n) +")");
        		continue;
        	}
        	if(m==0){
				n--;
				ls.addFirst("insert("+ n +","+(s2.charAt(n)) +")");
				continue;
        	}
        	
    		if(s1.charAt(m-1) == s2.charAt(n-1)){
    			if(d[m][n]== d[m-1][n-1]){
    				m--;n--;
    			}
    			else if(d[m][n] == d[m][n-1]+ this.c_i){
    				n--;
    				ls.addFirst("insert("+ n +","+(s2.charAt(n)) +")");
            	}
            	else {
            		m--;
            		ls.addFirst("delete("+ (n) +")");
            	}
    		}
    		else{
    			if(d[m][n]== d[m-1][n-1]+this.c_r){
    				m--;n--;
    				ls.addFirst("replace("+ n +","+ s2.charAt(n) +")");
    				
    			}
    			else if(d[m][n] == d[m][n-1]+ this.c_i){
    				n--;
            		ls.addFirst("insert("+ n +","+(s2.charAt(n)) +")");
            	}
            	else {
            		m--;
            		ls.addFirst("delete("+ (n) +")");
            	}
    		}
        }
        return ls;
    }
    
};
