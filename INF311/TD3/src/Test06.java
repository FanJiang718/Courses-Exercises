import tc.TC;
public class Test06 {
	public static void main(String[] args) {
		Monnaie[] tab={
		new Monnaie("Euro",1),
	    new Monnaie("Dollar",0.94),
	    };
		
		String s = "18716.05 Dollar";
		TC.println("-- test constructeur Argent(String) : attend 18716.05 Dollar");
		Argent a = new Argent(s,tab);
		TC.println(a);
	}
}
