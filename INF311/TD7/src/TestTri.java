import tc.TC;

public class TestTri {
	public static void main(String[] args) {
		String nomFichierSortie = "TestTri-sortie.txt";
		TC.println("--Test tri chaine -- redirection de sortie vers fichier " + nomFichierSortie);
		TC.ecritureDansNouveauFichier(nomFichierSortie);
		Dictionnaire d = new Dictionnaire("TestTri.txt");
		PrefixComparator l = new LexicographicComparator();
		Tri t = new Tri(d, l);

		t.tri();
		TC.print(d);
		
	}
}
