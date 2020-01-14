import tc.TC;
public class BoucleBissextile {

	static class Bissextile {
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

	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int annee = 0;
		TC.print("Entrer une valeur : ");
		annee = TC.lireInt();
		while(annee >= 0){
			Bissextile.affichage(annee);
			TC.print("Entrer une valeur : ");
			annee = TC.lireInt();
		}
		TC.println("Au revoir.");
		

	}


}

