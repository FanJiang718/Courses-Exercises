import tc.TC;

public class Bissextile {
	public static boolean estBissextile(int annee){
		if(annee%100 == 0){
			if(annee%400 ==0) return true;
			else return false;
		}
		else if(annee%4 ==0) return true;
		else return false;
	}
	
	public static void affichage(int annee){
		boolean BI = estBissextile(annee);
		if(BI)
			TC.println(annee+" est bissextile.");
		else
			TC.println(annee+" n'est pas bissextile.");
		return;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
	    affichage(1900);
	    affichage(1901);
	    affichage(1904);
	    affichage(2000);
	    return;
	}

}
