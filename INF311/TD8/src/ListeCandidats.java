import tc.TC;

public class ListeCandidats implements EnsembleCandidats {

	private Maillon tete;
	private Maillon queue;

	public ListeCandidats() {
		this.tete = null;
		this.queue = null;
	}

	public boolean estVide() {
		if(this.tete == null && this.queue == null) return true;
		else return false;
	}

	public void ajouterEnTete(Candidat c) {
		if(this.estVide()){
			Maillon m = new Maillon(c);
			this.tete = m;
			this.queue = m;
		}
		else{
			Maillon m = new Maillon(c, this.tete);
			this.tete = m;
		}
	}

	public void ajouterEnQueue(Candidat c) {
		if(this.estVide()){
			this.queue = Maillon.intercaler(this.queue, c);
			this.tete = this.queue;
		}
		else{
			this.queue = Maillon.intercaler(this.queue, c);
		}
	}

	public int nombreCandidats() {
		return Maillon.longueur(this.tete);
	}

	public void afficher() {
		if(this.estVide()) TC.println("<liste vide>");
		else{
			Maillon.afficher(this.tete);
		}
	}

	public void ajouterFichierEnQueue(String nomFichier) {
		TC.lectureDansFichier(nomFichier);
		String region = TC.lireLigne();
		while(!TC.finEntree()){
			String tmp = TC.lireLigne();
			Candidat cand = new Candidat(tmp);
			this.ajouterEnQueue(cand);
		}
		TC.println("Candidats de la region "+ region+" ajoutes. Il y a maintenant "+this.nombreCandidats()+" candidats");
	}

	public void enleverSuivant(Maillon precedent) {
		if(precedent == null){
			if(this.estVide()) return;
			else if(this.tete == this.queue){
				this.tete = null;
				this.queue = null;
			}
			else{
				this.tete = this.tete.suivant();
			}
		}
		else{
			if(precedent.suivant() == this.queue){
				this.queue = Maillon.enleverSuivant(precedent);
			}
			else{
				Maillon m = Maillon.enleverSuivant(precedent);
			}
		}
	}

	public void desistement(Candidat c) {
		if(this.estVide()) return;
		Maillon p = null;
		Maillon m = this.tete;
		while(!m.contenu.equals(c)){
			p = m;
			m = m.suivant();
			if(m == null) return;
		}
		this.enleverSuivant(p);
	}

	public void desistementFichier(String nomFichier) {
		TC.lectureDansFichier(nomFichier);
		Maillon m = this.tete;
		Maillon p = null;
		Maillon enleve_prece = null;
		//boolean fin = false;
		while(!TC.finEntree() && m!= null){
			if(this.estVide()) return;
			String tmp = TC.lireLigne();
			tmp +=" 0";
			Candidat c = new Candidat(tmp);
			while( m != null && /*!m.contenu.equals(c)*/ m.contenu.ordreAlphabetique(c)<0 ){
				p = m;
				m = m.suivant();
				/*
				if(m == null){
					fin = true;
					p = enleve_prece;
					if (p != null) m = p.suivant();
					else m = this.tete;
					break;
				}
				*/
			}
			/*if(!fin){
				m = m.suivant();
				this.enleverSuivant(p);
				enleve_prece = p;
			}
			fin = false;
			*/
			if(m.contenu.ordreAlphabetique(c) == 0){
				this.enleverSuivant(p);
				if (p == null) m = this.tete;
				else m = p.suivant();
				enleve_prece = p;
			}
			/*else{
				p = enleve_prece;
				if (enleve_prece != null) m = enleve_prece.suivant();
				else m = this.tete;
			}
			*/
		}
	}
	//public int i = 0;
	public void selection() {
		int note_max = this.tete.contenu.note;
		Maillon m = this.tete.suivant();
		Maillon p = this.tete;
		
		while( m != null /*&& m.suivant() != null*/ && m.contenu!= null){
			if (this.estVide()) return;
			if(m.contenu.note < note_max){
				//TC.println(m.contenu.toString());
				this.enleverSuivant(p);
				m = p.suivant();
				//this.i++;
			}
			else if(m.contenu.note == note_max){
				//TC.println(m.contenu.toString());
				p = m;
				m = m.suivant();
				//this.i++;
			}
			else{
				note_max = m.contenu.note;
				//TC.println(m.contenu.toString());
				this.tete = m;
				//this.i++;
				this.selection();
			}
			
		}
		//TC.println(i);
	}

	public void ajouterFichierTrie(String nomFichier) {
		Maillon p = null;
		Maillon m = this.tete;
		TC.lectureDansFichier(nomFichier);
		String region = TC.lireLigne();
		while(!TC.finEntree()){
			Candidat c = new Candidat(TC.lireLigne());
			while(m!= null && m.contenu.ordreAlphabetique(c)< 0){
				p = m;
				m = m.suivant();
			}
			if(m == this.tete){
				this.ajouterEnTete(c);
				m = this.tete;
			}
			else if(p== this.queue){
				this.ajouterEnQueue(c);
				m = this.queue;
			}
			else{
				m = Maillon.intercaler(p, c);
				
			}
		}
		TC.println("Candidats de la region "+ region+" ajoutes. Il y a maintenant "+this.nombreCandidats()+" candidats");
	}

}
