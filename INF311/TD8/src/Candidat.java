import tc.TC;

public class Candidat {
	private final String nom;
	private final String prenom;
	public final int note;

	public Candidat(String nom, String prenom, int note) {
		this.nom = nom;
		this.prenom = prenom;
		this.note = note;
	}

	/**
	 * Crée un candidat à partir d'une chaîne de la forme "nom prénom note".
	 * 
	 * @param ligne
	 *            la chaîne à analyser. On suppose qu'elle est de la forme
	 *            indiquée ci-dessus
	 */
	public Candidat(String ligne) {
		String[] mots = TC.motsDeChaine(ligne);
		this.nom = mots[0];
		this.prenom = mots[1];
		this.note = Integer.parseInt(mots[2]);
	}

	public String toString() {
		return (this.nom + " " + this.prenom + " " + this.note);
	}

	public int ordreAlphabetique(Candidat c) {
		int ordreNom = this.nom.compareTo(c.nom);
		if (ordreNom != 0)
			return ordreNom;
		return this.prenom.compareTo(c.prenom);
	}

	public boolean equals(Candidat c) {
		return this.ordreAlphabetique(c) == 0;
	}
}
