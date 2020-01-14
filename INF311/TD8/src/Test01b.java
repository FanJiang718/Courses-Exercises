import tc.TC;

public class Test01b {
	public static void main(String[] args) {
		EnsembleCandidats e = new ListeCandidats();
		// EnsembleCandidats e = new LinkedListCandidats();
		Candidat c1 = new Candidat("BERTHELEIN DONIA 7");
		Candidat c2 = new Candidat("BERTHELEIN HUGO 17");
		Candidat c3 = new Candidat("CENDRAY LUDOVIC 19");
		Candidat c4 = new Candidat("ALLUIRE GERALDINE 15");
		if (!e.estVide())
			TC.println("ERREUR: une liste nouvellement creee doit etre vide!");
		e.ajouterEnTete(c1);
		if (e.estVide())
			TC.println("ERREUR: quand on ajoute un element, la liste reste vide!");
		e.ajouterEnQueue(c2);
		e.ajouterEnQueue(c3);
		e.ajouterEnTete(c4);
		TC.println("Il y a " + e.nombreCandidats() + " candidats");
		e.afficher();
	}

}
