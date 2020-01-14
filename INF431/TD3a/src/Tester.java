public class Tester implements Runnable{
	final Stack<Integer> s;
	final int N;
	public Tester(Stack<Integer> s, int N){
		this.N=N;
		this.s=s;
	}
	public void run(){
		for(int i=0;i<N;i++)
			this.s.push(i);
	}

}
