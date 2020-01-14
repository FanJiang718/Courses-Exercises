import tc.TC;

public class Test04 {

  public static void test(int montant, Monnaie monnaie, Monnaie autreMonnaie) {
    Argent origine = new Argent(montant, monnaie);
    Argent converti = origine.convertir(autreMonnaie);
    Argent reconverti = converti.convertir(origine.getMonnaie());
    if(origine.estEgalA(reconverti))
    	TC.println(origine.toString() + " -> " + converti.toString() + " -> " + reconverti.toString() + " true" );
    else
    	TC.println(origine.toString() + " -> " + converti.toString() + " -> " + reconverti.toString() + " false" );
  }

  public static void main(String[] args) {
    String nomFichierSortie = "Test04-sortie-bis.txt";
    TC.println("-- test convertir : redirection de sortie vers fichier "
        + nomFichierSortie);
    TC.ecritureDansNouveauFichier(nomFichierSortie);
    
    Monnaie euro=new Monnaie("Euro",1);
    Monnaie yuan=new Monnaie("Yuan",0.14);
    Monnaie rouble=new Monnaie("Rouble",0.02);
    Monnaie dollar=new Monnaie("Dollar",0.94);
    Monnaie livre=new Monnaie("Livre",1.18);

    TC.println("-- Conversions : ");
    test(13399, euro, dollar);
    test(149, livre, rouble);
    test(2289, yuan, euro);
    test(1632, euro, livre);
    test(39, dollar, dollar);
    test(149, livre, yuan);
  }
}
