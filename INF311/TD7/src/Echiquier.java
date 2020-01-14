/**
 * @author Luca Castelli Aleardi, Philippe Chassignet (INF311, 2014)
 * 
 * Classe permettant de représenter et mettre a' jour l'etat de l'echiquier
 * 
 * L'echiquier est decrit par le tableau int[] positions:
 * la reine d'indice i ( 0<= i < n) est placee a' la position suivante:
 *  ligne d'indice i;
 *  colonne d'indice positions[i]
 * 
 */
public class Echiquier {

	public final int taille; // taille de la grille
	private final int[] positions; // tableau representant l'echiquier
	private int nombreDeSolutions;
	public boolean affichage;
	
	/**
	 * Initialise un nouvel echiquier
	 * 
	 * @param taille la taille de l'echiquier
	 * @param affichage specifie si l'echiquier doit etre affiche'
	 */
	public Echiquier(int taille, boolean affichage) {
	  this.taille = taille;
	  this.positions = new int[taille];
	  this.nombreDeSolutions = 0;
	  this.affichage = affichage;
  }

  /**
	 * Teste si une reine est en conflit avec les reines 0..reine-1
	 * 
	 *  @param reine indice de la reine dont il faut tester le conflit
	 *  @return true si la reine est en conflit avec les autres reines, ayant indices de 0..reine-1
	 */
	public boolean estEnConflit( int reine) {
		for (int i = 0; i < reine; i++) {
			if (positions[i] == positions[reine])             return true;   // meme colonne
			if ((positions[i] - positions[reine]) == (reine - i)) return true;   // meme diagonale
			if ((positions[reine] - positions[i]) == (reine - i)) return true;   // meme diagonale
		}
		return false;
	}

	/**
	 * Place une reine à une position donnee, par definition: la case [reine, colonne] de l'echiquier
	 * 
	 *  @param reine indice de la reine a' placer
	 *  @param colonne indice de la colonne ou' la reine sera placee
	 */
	public void placeReine(int reine, int colonne) {
		positions[reine]=colonne;
	}

	/**
	 * Enleve une reine de l'echiquier
	 * 
	 *  @param reine indice de la reine a' supprimer
	 */
	public void enleveReine(int reine) {
		positions[reine]=-1;
	}

	/**
	 * Incremente le nombre de solutions trouvees et affiche une solution (si affichage==true)
	 */
	public void estUneSolution() {
	  this.nombreDeSolutions++;
	  if(!this.affichage) return;
		System.out.println();
		for(int j=0;j<taille;j++)
			System.out.print("----");
		System.out.println();
		for (int i = 0; i < taille; i++) {
			System.out.print("|");
			for (int j = 0; j < taille; j++) {
				if (positions[i] == j) 
					System.out.print(" R |");
				else
					System.out.print("   |");
			}
			System.out.println();
			for(int j=0;j<taille;j++)
				System.out.print("----");
			System.out.println();
		}
		System.out.println();
		System.out.println();
	}
	
	/**
	 * Renvoie le nombre de solutions trouvees
	 */
	public int nombreDeSolutions() { return this.nombreDeSolutions;}
	
	/**
	 * Renvoie le tableau des positions
	 */
	protected int[] getPositions() { return this.positions;}


}
