/**
 * @author Luca Castelli Aleardi, Philippe Chassignet (INF311, 2014)
 * 
 *         Programme permettant de resoudre le probleme des 8 reines
 * 
 *         L'etat de l'echiquier est decrit par l'objet Echiquier 
 * 
 */
public class HuitReines {

  public static void genereConfigurationsSansConflit(Echiquier echiquier) {
    ajouteNouvelleReine(echiquier, 0); // commence par placer la premiere reine
                                       // (d'indice 0)
    System.out.println(echiquier.nombreDeSolutions()+" solutions");
  }

  /**
   * Cherche a placer la reine d'indice 'indiceReine' sur l'echiquier
   * On place la reine 'n' a' la ligne d'indice 'indiceReine', dans
   * toutes les colonnes de 0..N-1
   * 
   * @param echiquier
   *          l'Echiquier donnant la position des reines deja placees
   * @param indiceReine
   *          indice de la reine a placer (et a tester)
   */
  public static void ajouteNouvelleReine(Echiquier echiquier, int indiceReine) {
	// A COMPLETER (exo4)
	  if(indiceReine >= echiquier.taille){
		  echiquier.estUneSolution();
		  return;
	  }
	  for(int i =0; i< echiquier.taille; i++){
		  echiquier.placeReine(indiceReine, i);
		  if(!echiquier.estEnConflit(indiceReine)){
			  ajouteNouvelleReine(echiquier, indiceReine+1);
		  }
		  echiquier.enleveReine(indiceReine);
	  }
  }

  public static void main(String[] args) {
    genereConfigurationsSansConflit(new Echiquier(4, true));
    genereConfigurationsSansConflit(new Echiquier(5,false));
    genereConfigurationsSansConflit(new Echiquier(10,false));
    genereConfigurationsSansConflit(new Echiquier(13,false));
  }

}
