import tc.TC;
public class Compte {
	public final String nom;
	public final long numero;
	private Argent solde;
		
	public Compte(String nom, long numero, Argent a){
		this.nom = nom;
		this.numero = numero;
		this.solde = a;
	}
	public Compte(String str, Monnaie[] tab){
		String[] mots = TC.motsDeChaine(str);
		this.numero = Long.parseLong(mots[0]);
		String[] vals = TC.decoupage(mots[1],'.');
		int val_enti = Integer.parseInt(vals[0]);
		int val_decm = Integer.parseInt(vals[1]);
		int solde_val = val_enti * 100 + val_decm;
		Monnaie solde_monnaie = Monnaie.trouverMonnaie(mots[2],tab);
		this.solde = new Argent(solde_val,solde_monnaie);
		this.nom = mots[3];
			
	}
			
	public Argent getSolde(){
		return this.solde;
	}
	
	public Monnaie getMonnaie(){
		return this.solde.getMonnaie();
	}
	
	public void setSolde(Argent a){
		if(!a.getMonnaie().estEgalA(this.getMonnaie())){
			throw new IllegalArgumentException("le solde n'est pas dans la monnaie du compte");
		}
		this.solde = a;
	}

	public String toString(){
		return this.numero+" "+this.getSolde()+" "+this.nom;
	}
}
