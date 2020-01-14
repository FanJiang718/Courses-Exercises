
public class Tableau {
    public int[] t;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 Tableau[] tab = new Tableau[3];
		    for(int i = 0; i < 3; i++){
		      tab[i] = new Tableau();
		      for(int j = 0; j < 2; j++)
		        tab[i].t[j] = i * j;
		    }
		    for(int i = 0; i < 3; i++)
		      System.out.print(" "+tab[i].t[0]);
	}

}
