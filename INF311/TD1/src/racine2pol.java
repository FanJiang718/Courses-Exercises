import tc.TC;
public class racine2pol {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		double a=0.,b=0.,c=0.;
		TC.print("Entrer a b c : ");
		a= TC.lireDouble();
		b= TC.lireDouble();
		c= TC.lireDouble();
		double dis= 0.;
		double rac1 = 0.,rac2= 0.;
		dis = b*b-4*a*c;
		TC.println("Discriminant = "+dis);
		if(dis<0)
			TC.println("Pas de racine");
		else if(dis ==0)	
			TC.println("Racine double : "+(-b/2./a));
		else
		{
			rac1 = (-b +Math.sqrt(dis))/2./a;
			rac2 = (-b -Math.sqrt(dis))/2./a;
			TC.println("Deux racines : "+ rac2 +" et "+rac1);
		}
		return;
	}

}
