import tc.TC;

public class Test05 {

  public static void test(int montant, Monnaie monnaie, Monnaie autreMonnaie) {
    Argent origine = new Argent(montant, monnaie);
    Argent converti = origine.convertir(autreMonnaie);
    TC.println(origine.toString() + " -> " + converti.toString());
  }

  public static void main(String[] args) {
    String nomFichierSortie = "Test05-sortie.txt";
    TC.println("-- test convertir : redirection de sortie vers fichier "
        + nomFichierSortie);
    TC.ecritureDansNouveauFichier(nomFichierSortie);
    
    Monnaie[] tab={new Monnaie("Euro",1),new Monnaie("Yuan",0.14),new Monnaie("Rouble",0.02),
    		new Monnaie("Dollar",0.94),new Monnaie("Livre",1.18)};
    
    
    Monnaie euro=Monnaie.trouverMonnaie("Euro", tab);
    Monnaie yuan=Monnaie.trouverMonnaie("Yuan", tab);
    Monnaie rouble=Monnaie.trouverMonnaie("Rouble", tab);
    Monnaie dollar=Monnaie.trouverMonnaie("Dollar",tab);
    Monnaie livre=Monnaie.trouverMonnaie("Livre",tab);
    Monnaie yen=Monnaie.trouverMonnaie("Yen",tab);
    
    TC.println("-- attend null : ");
    TC.println(yen);
   
    TC.println("-- Conversions : ");
    test(1245, euro, dollar);
    test(2322, yuan, euro);
    test(249, livre, yuan);
    test(1632, euro, livre);
    test(1387, livre, rouble);
    test(59, dollar, dollar);
  }
}
