import tc.TC;

public class Test06b {
	public static void main(String[] args) {
		EnsembleCandidats e = new ListeCandidats();
		// EnsembleCandidats e = new LinkedListCandidats();
		e.ajouterFichierTrie("candidatsAuvergneRhoneAlpes.txt");
		e.ajouterFichierTrie("candidatsBourgogneFrancheComte.txt");
		e.ajouterFichierTrie("candidatsBretagne.txt");
		e.ajouterFichierTrie("candidatsCentreValDeLoire.txt");
		e.ajouterFichierTrie("candidatsCorse.txt");
		e.ajouterFichierTrie("candidatsGrandEst.txt");
		e.ajouterFichierTrie("candidatsHautsDeFrance.txt");
		e.ajouterFichierTrie("candidatsIleDeFrance.txt");
		e.ajouterFichierTrie("candidatsNormandie.txt");
		e.ajouterFichierTrie("candidatsNouvelleAquitaine.txt");
		e.ajouterFichierTrie("candidatsOccitanie.txt");
		e.ajouterFichierTrie("candidatsPaysDeLaLoire.txt");
		e.ajouterFichierTrie("candidatsProvenceAlpesCoteDAzur.txt");
		e.desistementFichier("desistements.txt");
		e.selection();
		TC.println("Il reste " + e.nombreCandidats() + " candidat(s)");
		e.afficher();
	}

}
