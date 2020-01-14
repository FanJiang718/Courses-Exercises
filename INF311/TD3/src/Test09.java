import tc.TC;
public class Test09 {
	public static void main(String[] args) {
		Monnaie[] tab={
				new Monnaie("Euro",1),
			    new Monnaie("Dollar",0.94)
		};
		
		long numero = 99887766;
		Argent a = new Argent(554433);
		String nom = "Agathe_Oursin";
		String s = "" + numero + " " + a + " " + nom;
		TC.println("-- test constructeur Compte(String) ");
		Compte c = new Compte(s,tab);
		TC.println("-- numero : attend " + numero);
		TC.println(c.numero);
		TC.println("-- nom : attend " + nom);
		TC.println(c.nom);
		TC.println("-- solde : attend " + a);
		TC.println(c.getSolde());
	}
}
