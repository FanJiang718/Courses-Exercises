import tc.TC;

public class Maillon {
	public final Candidat contenu;
	private Maillon suivant;

	public Maillon(Candidat c) {
		this.contenu = c;
		this.suivant = null;
	}

	public Maillon(Candidat c, Maillon reste) {
		this.contenu = c;
		this.suivant = reste;
	}

	public Maillon suivant() {
		return this.suivant;
	}

	public static Maillon intercaler(Maillon courant, Candidat c) {
		if(courant == null){
			Maillon m = new Maillon(c);
			return m;

		}
		else if(courant.suivant() == null){
			Maillon m = new Maillon(c);
			courant.suivant = m;
			return m;

		}
		else{
			Maillon m = new Maillon(c,courant.suivant());
			courant.suivant = m;
			return m;

		}
	}

	public static Maillon enleverSuivant(Maillon courant) {
		if(courant == null) return null;
		else if(courant.suivant() == null) return courant;
		else if(courant.suivant().suivant()== null){
			courant.suivant = null;
			return courant;
		}
		else{
			courant.suivant = courant.suivant().suivant();
			return courant;
		}
	}

	public static int longueur(Maillon m) {
		int longeur= 0;
		if (m == null) return longeur;
		longeur++;
		while(m.suivant() != null){
			longeur++;
			m = m.suivant();
		}
		return longeur;
	}

	public static void afficher(Maillon m) {
		if (m == null) return;
		TC.println(m.contenu);
		afficher(m.suivant());
	}
}
