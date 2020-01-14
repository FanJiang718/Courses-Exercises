import tc.TC;

public class TestRang {
	public static void main(String[] args) {
		Dictionnaire d = new Dictionnaire("TestTri.txt");
		LexicographicComparator comp = new LexicographicComparator();
		Tri t = new Tri(d, comp);
		t.tri();
		
		TC.println("-- test rang : attend 'epitome' en position 5");
		TC.println(t.rang("polymath"));	

		TC.println("-- test rang : ne trouve pas 'polytechnique', attend -1");
		TC.println(t.rang("polytechnique"));	
		
	}
}
