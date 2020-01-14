import tc.TC;

public class TestPartition {
	public static void main(String[] args) {
		String nomFichierSortie = "TestPartition-sortie.txt";
		TC.println("--Test tri chaine -- redirection de sortie vers fichier " + nomFichierSortie);
		TC.ecritureDansNouveauFichier(nomFichierSortie);
				
		Dictionnaire d = new Dictionnaire("TestPartition.txt");
		PrefixComparator l = new LexicographicComparator();
		Tri t = new Tri(d, l);
		int lo = 3; 
		int hi = 9;
        int k = 7;
        int v = Dictionnaire.caractereA(d.get(lo), k);
        System.out.println("Pivot sur la lettre " + d.get(7).charAt(k) + " de code " + v + " en " + k + "-eme position");
		t.partition(v, lo, hi, k);
		TC.print(d);
		
	}
}
