public class Tri {

	private static final int COUPURE = 5;
	private Dictionnaire dict;
	private PrefixComparator comparator;
	
	Tri (Dictionnaire dict, PrefixComparator comparator){
		this.dict = dict;
		this.comparator = comparator;
	}
		
	public void triInsertion(int lo, int hi, int d) {
		// A completer (Exo 6a)
		if(lo < hi){
		for(int i= lo+1; i< hi;i++){
			int j = i;
			while(j>lo && this.comparator.precede(this.dict.get(j), this.dict.get(j-1), d)){
				this.dict.echange(j, j-1);
				j--;
				
			}
		}
		}
	}
	public Bornes partition(int v, int lo, int hi, int d) {
		// A completer (Exo 6b)
		int inf=lo, mid = lo, sup = hi-1;
		while(mid <= sup){
			if( Dictionnaire.caractereA(this.dict.get(mid), d)==v){
				mid++;
			}
			else if(Dictionnaire.caractereA(this.dict.get(mid), d) < v){
				this.dict.echange(inf,mid);
				inf++;
				mid++;
			}
			else{
				this.dict.echange(mid, sup);
				sup--;
			}
		}
		Bornes b = new Bornes(inf,sup);
		return b;
	}

	public void tri(int lo, int hi, int d) {
		// A completer (Exo 6b)
		if(lo<hi){
		if((hi-lo) < Tri.COUPURE) this.triInsertion(lo,hi,d);
		else{
			int v = -1;
			while(v==-1 && lo < hi){
				Dictionnaire.caractereA(this.dict.get(lo), d);
				lo++;
			}
			Bornes b = this.partition(v, lo, hi, d);
			this.tri(b.inf,b.sup,d+1);
			this.tri(lo, b.inf, d);
			this.tri(b.sup, hi, d);
		}
		}
		
	}

	public void tri() {
		tri(0, dict.size(), 0);
	}

	private int rang(String s, int lo, int hi) {
		// A completer (Exo 6c)
		int result = this.dict.compare(s, (lo+hi)/2);
		if((hi-lo)<=1 ){
			if(result ==0) return lo;
			else return -1;
		}
		else{ 
			if (result==0) return (lo+hi)/2;
			else if(result<0) return rang(s, lo,(lo+hi)/2);
			else return rang(s, (lo+hi)/2, hi);
		}
	}
	
	public int rang(String s) {
		return rang(s, 0, dict.size());
	}
}
