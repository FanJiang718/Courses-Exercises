import java.util.Locale;

import tc.TC;

public class Noeud {
	
    public Noeud gauche;
    public Noeud droit;
    public Entree contenu;
    
    public Noeud(Entree e) {
        gauche = null;
        droit = null;
        contenu = e;
    }
    
    public Noeud(Noeud g, Noeud d, Entree e) {
        gauche = g;
        droit = d;
        contenu = e;
    }
    
	// Pour les trois méthodes "comparer" on exploite la surcharge de la 
	// méthode correspondant de la classe "Entree".
    public int comparer(Noeud x) {
        return contenu.comparer(x.contenu);
    }

    public int comparer(Entree e) {
        return contenu.comparer(e);
    }

    public int comparer(String m) {
        return contenu.comparer(m);
    }

    public String toString( ) {
        String str = "";
        if(gauche != null)
            str += "(" + gauche + ")";
        else
            str += "*";
        str += " <- " + contenu + " -> ";
        if(droit != null)
            str += "(" + droit + ")";
        else
            str += "*";
        return str;
    }
        
    // Les méthodes ci-dessus sont données, vous ne devez pas les modifier.
    
    // Exercice 1
    public int hauteur(){
    	if(this.gauche == null && this.droit == null) return 0;
    	else if(this.gauche == null && this.droit != null) return 1+ this.droit.hauteur();
    	else if(this.droit == null && this.gauche != null) return 1 + this.gauche.hauteur();
    	else{
    		return 1+ Math.max(this.gauche.hauteur(), this.droit.hauteur());
    	}
    }

    // Exercice 2
    public ListeEntiers chercher(String w) {
    	if(this.contenu == null) return new ListeEntiers();
    	int result = this.contenu.comparer(w);
    	if(result ==0) return this.contenu.occurrences;
    	else if(result < 0 && this.droit != null) return this.droit.chercher(w);
    	else if (result > 0 && this.gauche != null)return this.gauche.chercher(w);
    	else return new ListeEntiers();
    }
    
    // Exercice 3
    public boolean estValide(String min, String max) {
    	if(this.contenu == null) return true;
    	if (min == null && max == null){
    		if(this.gauche == null && this.droit == null) return true;
    		else if(this.gauche == null && this.droit != null) return this.droit.estValide(this.contenu.mot, max);
    		else if(this.droit == null && this.gauche != null) return this.gauche.estValide(min, this.contenu.mot);
    		else return this.gauche.estValide(min, this.contenu.mot) && this.droit.estValide(this.contenu.mot, max);
    	}
    	else if(min == null && max != null){
    		if(this.contenu.comparer(max) <0){
        		if(this.gauche == null && this.droit == null) return true;
        		else if(this.gauche == null && this.droit != null) return this.droit.estValide(this.contenu.mot, max);
        		else if(this.droit == null && this.gauche != null) return this.gauche.estValide(min, this.contenu.mot);
        		else return this.gauche.estValide(min, this.contenu.mot) && this.droit.estValide(this.contenu.mot, max);
        	}
    		else return false;
    	}
    	else if(min != null && max == null){
    		if(this.contenu.comparer(min) >0){
        		if(this.gauche == null && this.droit == null) return true;
        		else if(this.gauche == null && this.droit != null) return this.droit.estValide(this.contenu.mot, max);
        		else if(this.droit == null && this.gauche != null) return this.gauche.estValide(min, this.contenu.mot);
        		else return this.gauche.estValide(min, this.contenu.mot) && this.droit.estValide(this.contenu.mot, max);
        	}
    		else return false;
    	}
    	else{
    		if(this.contenu.comparer(min) >0 && this.contenu.comparer(max)<0){
        		if(this.gauche == null && this.droit == null) return true;
        		else if(this.gauche == null && this.droit != null) return this.droit.estValide(this.contenu.mot, max);
        		else if(this.droit == null && this.gauche != null) return this.gauche.estValide(min, this.contenu.mot);
        		else return this.gauche.estValide(min, this.contenu.mot) && this.droit.estValide(this.contenu.mot, max);
        	}
    		else return false;
    	}
    	
    }
    
    // Exercice 4
    public void ajouterOccurrence(String w, int n) {
    	int result = this.contenu.comparer(w);
    	if(result ==0 ){
    		this.contenu.occurrences.ajouterEnQueue(n);
    	}
    	else if(result >0){
    		if(this.gauche == null){
    			this.gauche = new Noeud(new Entree(w,n));
    		}
    		else{
    			this.gauche.ajouterOccurrence(w, n);
    		}
    	}
    	else{
    		if(this.droit == null){
    			this.droit = new Noeud(new Entree(w,n));
    		}
    		else{
    			this.droit.ajouterOccurrence(w, n);
    		}
    	}
    }
    
    // Exercice 5
    public void imprimer() {
    	if(this.gauche == null && this.droit== null) TC.println(this.contenu.toString());
    	else{
    		if(this.gauche!= null) this.gauche.imprimer();
    		TC.println(this.contenu.toString());
    		if(this.droit!= null) this.droit.imprimer();
    	}
    }
    
    // Exercice 6
    public ListeEntrees liste( ) {
    	ListeEntrees list = new ListeEntrees();
    	if(this.gauche == null && this.droit== null) {
    		list.ajouterEnQueue(this.contenu);
    		return list;
    	}
    	else{
    		if(this.gauche == null){
    			list.ajouterEnQueue(this.contenu);
    			list.concatener(this.droit.liste());
 
    		}
    		else if(this.droit== null){
    			list = this.gauche.liste();
    			list.ajouterEnQueue(this.contenu);
    		}
    		else{
    			list = this.gauche.liste();
    			list.ajouterEnQueue(this.contenu);
    			list.concatener(this.droit.liste());
    		}
    		return list;
    	}
    }

    // Exercice 7
	public static Noeud indexerTableauTrie(Entree[] entrees, int min, int max) {
		int middle = (min+max)/2;
		if(max -min ==1) return new Noeud(new Noeud(entrees[min]),null,entrees[max]);
		else if(max == min ) return new Noeud(entrees[min]);
		else{
			Noeud g = indexerTableauTrie(entrees, min, middle-1);
			Noeud d = indexerTableauTrie(entrees, middle+1, max);
			Noeud t = new Noeud(g,d,entrees[middle]);
			return t;
		}
	}
	
}
