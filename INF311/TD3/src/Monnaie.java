
public class Monnaie {

	public final String nom;
	private double taux = 0.;
	
	public Monnaie(String par_nom, double par_taux){
		this.nom = par_nom;
		this.taux = par_taux;
		
	}
	public double getTaux(){
		return this.taux;
	}
	
	public void setTaux(double autreTaux){
		this.taux = autreTaux;
	}
	
	public boolean estEgalA(Monnaie m){
		boolean egal = false;
		if (m != null){
			if ((this.taux == m.taux) && this.nom.equals(m.nom))
				egal = true;
			else
				egal = false;
		}
		else{
			egal = false;
		}
		return egal;
	}
	
	public static Monnaie trouverMonnaie(String s, Monnaie[] tab){
		for(int i =0; i< tab.length; i++){
			if(tab[i].nom.equals(s))
				return tab[i];
		}
		return null;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
