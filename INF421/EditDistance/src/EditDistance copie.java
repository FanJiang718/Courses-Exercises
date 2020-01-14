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
    /*    
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
    */
    public int[][] getEditDistanceDP(String s1, String s2) {
    	int m = s1.length();
    	int n = s2.length();
    	int X = 1;
    	int diff_nm = Math.abs(m-n);
    	int[][] result = new int[m+1][n+1];
    	for(int i=0; i< n+1; i++){
    		result[0][i] = i * this.c_i;
    	}
    	for(int i =0; i< m+1; i++){
    		result[i][0] = i * this.c_d;
    	}
    	while(true){
    		for(int i=1; i < m+1; i++){
    			for(int j= 1; j< n+1; j++){
    				if(Math.abs(i-j) <= diff_nm + X){
    					long min_tmp = Math.min((long)result[i-1][j] + this.c_d, (long)result[i][j-1] + this.c_i);
    					if(s1.charAt(i-1) == s2.charAt(j-1)){
    						result[i][j] = (int) Math.min((long)result[i-1][j-1], min_tmp);
    					}
    					else{
    						result[i][j] =(int) Math.min((long)result[i-1][j-1] + this.c_r, min_tmp);
    					}
    				}
    				else{
    					result[i][j] = MAX;
    				}
    			}
    		}	
    		if( (result[m][n]/(this.c_i+ this.c_d)) <= X) break;
    		X = X*2;
    	}
        return result;
    }

    public List<String> getMinimalEditSequence(String s1, String s2) {
        /* To be completed in Part 2. Remove sample code block below. 
        LinkedList<String> ls = new LinkedList<> ();
        if (c_r == 6) {
            ls.add("delete(1)");
            ls.add("delete(1)");
            ls.add("insert(2,c)");
            ls.add("insert(3,b)");
        }
        else {
            ls.add("replace(1,d)");
            ls.add("replace(3,b)");
        }
        return ls;
        Code block to be removed ends. */
        LinkedList<String> ls = new LinkedList<> ();
        int[][] d = this.getEditDistanceDP(s1, s2);
        int i=0,j =0;
        int m=0,n =0;
        int target = d[s1.length()][s2.length()];
        int count_d = 0;
        int count_i = 0;
    		
        while(d[m][n]!= target){
        	if(i>=s1.length()) i = s1.length()-1;
        	if(j>=s2.length()) j = s2.length()-1;
        	
    		if(s1.charAt(i) == s2.charAt(j)){
    			if(d[m][n]== d[m+1][n+1]){
    				m++;n++;
    			}
    			else if(d[m][n] == d[m][n+1]- this.c_i){
            		ls.add("insert("+ n +","+(s2.charAt(n)) +")");
            		n++;i++;
            	}
            	else {
            		ls.add("delete("+ (n) +")");
            		m++;
            	}
    		}
    		else{
    			if(d[m][n]== d[m+1][n+1]-this.c_r){
    				ls.add("replace("+ n +","+ s2.charAt(n) +")");
    				m++;n++;
    			}
    			else if(d[m][n] == d[m][n+1]- this.c_i){
            		ls.add("insert("+ n +","+(s2.charAt(n)) +")");
            		n++;
            	}
            	else {
            		ls.add("delete("+ (n) +")");
            		m++;
            	}
    		}
    		i = m;
    		j = n;
        	System.out.println("m:"+ m + ", n: "+n);
        }
        return ls;
    }
    
    public static void main(String[] args) {
        String s1 = "aebcd";
        String s2 = "eadcb";
        EditDistance edt = new EditDistance(3,2,6);
        int[][] d = edt.getEditDistanceDP(s1, s2);
        for(int i =0; i<= s1.length(); i++){
        	for(int j =0; j<= s2.length();j++){
        		System.out.print(d[i][j]+" ");
        	}
        	System.out.println("");
        }
    }

};
