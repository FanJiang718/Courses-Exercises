import tc.TC;

public class Test06a {
	public static void main(String[] args) {
		EnsembleCandidats e = new ListeCandidats();
		// EnsembleCandidats e = new LinkedListCandidats();
		e.ajouterFichierTrie("candidatsGrandEst.txt");
		e.ajouterFichierTrie("candidatsHautsDeFrance.txt");
		TC.ecritureDansNouveauFichier("output06a.txt");
		e.afficher();
	}

}
