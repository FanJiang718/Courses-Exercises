
public class Test {

	public static void main(String[] args) throws InterruptedException {
		Stack<Integer> stack = new SafeStackSimple<>();
		final int N = 100000;
		final int Nthreads = 20;
		
		long startTime = System.nanoTime();
		Thread[] threads = new Thread[Nthreads];
		for(int i=0;i<Nthreads;i++){
			threads[i]=new Thread(new Tester(stack,N));
			threads[i].start();
		}
		for(int i=0;i<Nthreads;i++){
				threads[i].join();
		}
		long stopTime = System.nanoTime();
		
		int i=0;
		while(stack.pop()!=null)i++;
		System.out.println("nb: "+i+" time: "+(stopTime-startTime)/1000000+"ms");
	}

}
