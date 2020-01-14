import tc.TC;
public class Test08 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Monnaie rouble=new Monnaie("Rouble",0.02);

		Argent a1 = new Argent(13468);
		Argent a2 = new Argent(17401, rouble);
		
		Compte c1=new Compte("Fan",123456789, a1);
		Compte c2=new Compte("JIANG",987654321, a2);
		
		TC.println("-- test toString : attend 123456789 134.68 Euro Fan");
		TC.println(c1.toString());

		TC.println("-- test toString : attend 987654321 174.01 Rouble JIANG");
		TC.println(c2);
	}

}
