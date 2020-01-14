import tc.TC;

public class Test01a {
	public static void main(String[] args) {
		Candidat c1 = new Candidat("ALLUIRE GERALDINE 15");
		Candidat c2 = new Candidat("BERTHELEIN DONIA 7");
		Candidat c3 = new Candidat("BERTHELEIN HUGO 17");
		Candidat c4 = new Candidat("CENDRAY LUDOVIC 19");
		Maillon m1 = new Maillon(c1);
		Maillon m3 = Maillon.intercaler(m1, c3);
		Maillon m4 = Maillon.intercaler(m3, c4);
		Maillon m2 = Maillon.intercaler(m1, c2);
		Maillon m = Maillon.enleverSuivant(m1);
		TC.println("Il y a " + Maillon.longueur(m) + " candidats");
		Maillon.afficher(m);
	}

}
