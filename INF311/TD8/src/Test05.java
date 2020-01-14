import tc.TC;

public class Test05 {
	public static void main(String[] args) {
		EnsembleCandidats e = new ListeCandidats();
		// EnsembleCandidats e = new LinkedListCandidats();
		e.ajouterFichierEnQueue("candidatsCorse.txt");
		e.selection();
		TC.println("Il reste " + e.nombreCandidats() + " candidats");
		TC.ecritureDansNouveauFichier("output05.txt");
		e.afficher();
	}

}
