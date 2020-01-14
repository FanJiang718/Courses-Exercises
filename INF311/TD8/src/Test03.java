import tc.TC;

public class Test03 {
	public static void main(String[] args) {
		EnsembleCandidats e = new ListeCandidats();
		// EnsembleCandidats e = new LinkedListCandidats();
		e.ajouterFichierEnQueue("candidatsBretagne.txt");
		e.desistement(new Candidat("PANCOLET ALEXANDRE 0"));
		e.desistement(new Candidat("DANCTOVILLE GERALDE 0"));
		e.desistement(new Candidat("VAUDRUDE SYLVAIN 0"));
		TC.println("Il reste " + e.nombreCandidats() + " candidats");
		TC.ecritureDansNouveauFichier("output03.txt");
		e.afficher();
	}

}
