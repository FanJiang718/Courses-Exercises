
public class Paire {

	public int a, b;
	 
    public Paire(){

      }
    
    public Paire(int x, int y){
      this.a = x;
      this.b = y;
    }
    
    public static Paire remplir_7(Paire p, int x, int y){
        p.a = x;
        p.b = y;
        return p;
      } 
    
    public static Paire remplir_9(Paire p, int x, int y){
        p = new Paire();
        p.a = x;
        p.b = y;
        return p;
      } 
    
    public static Paire creer(int x, int y){
        Paire p = new Paire();
        p.a = x;
        p.b = y;
        return p;
      }
    
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Paire p = remplir_9(null, 1, 2);
	    Paire q = remplir_9(p, 3, 5);
	    System.out.println(p.a + " " + p.b + " " + q.a + " " + q.b); 
	 
	}

}
