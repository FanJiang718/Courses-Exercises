public class Multred extends Thread {
  int k;
  int pos;
  int a[][];

  Multred(int k, int pos, int[][] tab) 
  {
	  this.k = k;
	  this.pos = pos;
	  this.a= tab;
  }
  
  
 
  public void run() {
    // multiplication parallèle par saut de pointeurs
    int i, j;
    for(i =1; i<=k;i++) {
    	j = this.pos+(1<<(i-1));
    	if(j<(1<<(k))) {
    		while(a[j][i-1]==0) {};
    		a[pos][i] = a[pos][i-1]* a[j][i-1];
    	}
    	else {
    		a[pos][i] = a[pos][i-1];
    	}
    }
  }
}
