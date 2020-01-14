import tc.TC;
public class Test07 {

	public static void main(String[] args) {
		Monnaie dollar=new Monnaie("Dollar",0.94);
		
		Argent a1 = new Argent(10073);
		Argent a2 = new Argent(2315);
		Argent a3 = new Argent(100000, dollar);
		Argent a4 = new Argent(2500, dollar);
		
		String nomFichierSortie = "Test07-sortie.txt";
		TC.println("--Test plus/moins -- redirection de sortie vers fichier " + nomFichierSortie);
		TC.ecritureDansNouveauFichier(nomFichierSortie);
		
		TC.println("-- test a1.plus(a2) : attend 123.88 Euro");
		Argent a5 = a1.plus(a2);
		TC.println(a5 + "");
		TC.println("-- test a1.plus(a3) : attend 1100.73 Euro");
		a5 = a1.plus(a3);
		TC.println(a5 + "");
		TC.println("-- test a3.plus(a4) : attend 1025.00 Dollar");
		a5 = a3.plus(a4);
		TC.println(a5 + "");
		TC.println("--test a4.plus(a2) : attend 49.62 Dollar");
		a5 = a4.plus(a2);
		TC.println(a5 + "");

		
        TC.println("-- test a2.moins(a1) : attend null");
        a5 = a2.moins(a1);
        TC.println(a5);
        TC.println("--test a3.moins(a1) : attend 899.27 Dollar");
		a5 = a3.moins(a1);
		TC.println(a5 + "");
	    TC.println("--test a3.moins(a1, 1.31) : attend 868.05 Dollar");
		a5 = a3.moins(a1);
		TC.println(a5 + "");
	    TC.println("--test a4.moins(a1, 1.31) : attend null");
		a5 = a4.moins(a1);
		TC.println(a5 + "");

	}

}
