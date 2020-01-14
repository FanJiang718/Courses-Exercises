import tc.TC;

public class Argent {

	// répresentation interne de l'argent:
	// Champs d'objet
	private final int valeur;
	private final Monnaie monnaie;

	public Argent(int v) {
		this.valeur = v;
		this.monnaie = new Monnaie("Euro", 1.0);
	}

	public Argent(int v, Monnaie monnaie) {
		if (monnaie == null)
			throw new IllegalArgumentException("le parametre monnaie est null");
		this.valeur = v;
		this.monnaie = monnaie;
	}

	public Argent(String str, Monnaie[] tab){
		String[] mots = TC.motsDeChaine(str);
		String[] vals = TC.decoupage(mots[0],'.');
		int val_enti = Integer.parseInt(vals[0]);
		int val_decm = Integer.parseInt(vals[1]);
		this.valeur = val_enti * 100 + val_decm;
		this.monnaie = Monnaie.trouverMonnaie(mots[1],tab);	
	}
	
	public Monnaie getMonnaie() {
		return this.monnaie;
	}

	public int getValeur() {
		return this.valeur;
	}
	
	public int valeurEntiere() {
		return this.getValeur() / 100;
	}

	public int valeurDecimale() {
		return this.getValeur() % 100;
	}

	public boolean estEgalA(Argent a) {
		// a completer
		boolean egal = false;
		if(a != null){
			if((this.getValeur() == a.getValeur()) && (this.getMonnaie().estEgalA(a.getMonnaie())))
				egal = true;
			else
				egal = false;
		}
		else{
			egal = false;
		}
		return egal;
	}

	public String toString() {
		// a completer
		if(this.valeurDecimale()<10 && this.valeurDecimale() >= 0){
			return this.valeurEntiere() + ".0" + this.valeurDecimale() + " " + this.getMonnaie().nom;
		}
		else{
			return this.valeurEntiere() + "." + this.valeurDecimale() + " " + this.getMonnaie().nom;
		}
		
	}

	public Argent convertir(Monnaie autreMonnaie) {
		// a completer
		double newVal_double = (this.getMonnaie().getTaux())/(autreMonnaie.getTaux())*this.getValeur();
		int newVal_int = (int)newVal_double;
		Argent newArgent = new Argent(newVal_int,autreMonnaie);
		return newArgent;
	}

	
	public Argent plus(Argent x) {
		// a completer
		Argent xPrime = x.convertir(this.getMonnaie());
		Argent new_arg = new Argent(this.getValeur()+xPrime.getValeur(),this.getMonnaie());
		return new_arg;
	}

	public Argent moins(Argent x) {
		// a completer
		Argent xPrime = x.convertir(this.getMonnaie());
		if((this.getValeur()-xPrime.getValeur())>=0){
			Argent new_arg = new Argent(this.getValeur()-xPrime.getValeur(), this.getMonnaie());
			return new_arg;
		}
		else{
			return null;
		}
	}
}