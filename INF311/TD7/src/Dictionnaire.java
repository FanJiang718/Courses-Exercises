import java.util.ArrayList;

import tc.TC;

public class Dictionnaire {
	private String[] dict;

	public Dictionnaire(String dict) {
		TC.lectureDansFichier(dict);
		ArrayList<String> a = new ArrayList<>();

                while (! TC.finEntree()) {
                    a.add(TC.lireLigne());
                }

		String[] s = new String[0];
		this.dict = a.toArray(s);
	}

	public int size() {
		return dict.length;
	}

	public String toString() {
		String s = "";
		for (int i = 0; i < dict.length; i++) {
			s += dict[i] + "\n";
		}
		return s;
	}
    
	int compare(String s, int i){
		return s.compareTo(dict[i]);
	}

	public void echange(int i, int j) {
		String tmp = dict[i];
		dict[i] = dict[j];
		dict[j] = tmp;
	}
	
	public String get(int i){
		return dict[i];
	}
	
	static int caractereA(String s, int d) {
		if (d < s.length()) {
			return s.charAt(d);
		} else {
			return -1;
		}
	}	
}
