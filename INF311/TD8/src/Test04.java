import tc.TC;

public class Test04 {
	public static void main(String[] args) {
		EnsembleCandidats e = new ListeCandidats();
		// EnsembleCandidats e = new LinkedListCandidats();
		e.ajouterFichierEnQueue("candidatsCentreValDeLoire.txt");
		e.desistementFichier("desistements.txt");
		TC.println("Il reste " + e.nombreCandidats() + " candidats");
		TC.ecritureDansNouveauFichier("output04.txt");
		e.afficher();
	}

}
