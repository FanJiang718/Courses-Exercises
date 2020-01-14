import java.util.*;

public class Recurrence {
  public static void main(String[] args) {
    int k = Integer.parseInt(args[0]);
    

    // test somme de n entiers tirés aléatoirement
    Random r = new Random();
    // on tire un nouvel élément entre 0 et n-1 par r.nextInt(n)
    int n = 1<<k;
    int[][] tab = new int[n][k+1];
    int[][] a = new int[n][k+1] ;
    int[] b = new int[n];
    for(int i=0;i<n;i++) {
    	a[i][0] = 2;
    	b[i] = r.nextInt(n)+1;
    }

    // test y(i+1)=2y(i)+a(i) où a est un tableau aléatoire
    for(int i =0; i< n; i++) {
    	new Multred(k,i,a).start();
    }
    for(int i=0; i< n; i++) {
    	while(a[i][k] ==0) {};
    }
    for(int i =0; i< n; i++) {
    	new Localconvol(k,i,tab,a,b).start();
    }
    for(int i=0; i< n; i++) {
    	while(tab[i][0] ==0) {};
    }
    for(int i =0; i< n; i++) {
    	new Plusred(k,i,tab).start();
    }
    for(int i=0; i< n; i++) {
    	while(tab[i][k] ==0) {};
    }
    System.out.println("a: ");
    for(int i =0; i< k+1; i++){
    	System.out.println();
    	for(int j =0; j< n; j++){
    		System.out.print(a[j][i] + " ");
    	}
    }
    System.out.println();	
    System.out.println("b: ");
    for(int j =0; j< n; j++){
    	System.out.print(b[j] + " ");
    }
    System.out.println();
    System.out.println("t: ");
    for(int i =0; i< k+1; i++){
    	System.out.println();
    	for(int j =0; j< n; j++){
    		System.out.print(tab[j][i] + " ");
    	}
    }
    System.out.println();
  }
}