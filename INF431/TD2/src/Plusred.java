public class Plusred extends Thread {
  int k;
  int pos;
  int t[][];

  
  Plusred(int k, int pos, int[][] tab) 
  {
	  this.k = k;
	  this.pos = pos;
	  this.t= tab;
  }

  public void run() { 
	    int i, j;
	    for(i =1; i<=k;i++) {
	    	j = this.pos-(1<<(i-1));
	    	if(j>=0) {
	    		while(t[j][i-1]==0) {};
	    		t[pos][i] = t[pos][i-1]+ t[j][i-1];
	    		
	    	}
	    	else {
	    		t[pos][i] = t[pos][i-1];
	    	}
	    }
  }
}