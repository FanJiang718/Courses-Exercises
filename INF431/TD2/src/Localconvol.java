public class Localconvol extends Thread {
  int k;
  int pos;
  int t[][];
  int a[][];
  int b[];

  Localconvol(int k, int pos, int[][] t, int[][] a, int[] b) {
	  this.k = k;
	  this.a= a;
	  this.pos = pos;
	  this.t = t;
	  this.a = a;
	  this.b = b;
  }

  public void run() {
	  t[pos][0] = a[pos][k] * b[pos];  
  }
}