import tc.TC;

public class Test02 {
	public static void main(String[] args) {
		EnsembleCandidats e = new ListeCandidats();
		// EnsembleCandidats e = new LinkedListCandidats();
		e.ajouterFichierEnQueue("candidatsBourgogneFrancheComte.txt");
		TC.ecritureDansNouveauFichier("output02.txt");
		TC.println("Bourgogne-Franche-Comte");
		e.afficher();
	}

}
