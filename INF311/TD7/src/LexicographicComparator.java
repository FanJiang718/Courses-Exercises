public class LexicographicComparator implements PrefixComparator {
	
	public boolean precede(String v, String w, int d) {
		// A completer (Exo 6a)
		int x = Dictionnaire.caractereA(w,d);
		int y = Dictionnaire.caractereA(v,d);
		
		if(x== -1) return false;
		else if(y == -1) return true;
		else if(y == x) return precede(v,w,d+1);
		else if(y < x) return true;
		else return false;
	}
}
