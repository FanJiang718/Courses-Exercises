import tc.TC;

public class TestInsertion {
	public static void main(String[] args) {
		String nomFichierSortie = "TestInsertion-sortie.txt";
		TC.println("--Test tri insertion -- redirection de sortie vers fichier " + nomFichierSortie);
		TC.ecritureDansNouveauFichier(nomFichierSortie);
		
		Dictionnaire d = new Dictionnaire("TestInsertion.txt");
		LexicographicComparator comp = new LexicographicComparator();
		Tri t = new Tri(d, comp);

		t.triInsertion(4, d.size() - 2, 4);
		TC.print(d);
	}
}
