public class Fibon extends Thread {
    private final int x;
    int result;

    public Fibon(int x) {
    	this.x = x;
    }
    

    public void run() {
    	if(x==0){
    		result = 1;
    	}
    	else if(x==1){
    		result =1;
    	}
    	else{
    		Fibon t1 = new Fibon(x-1);
    		Fibon t2 = new Fibon(x-2);
    		t1.start();
    		t2.start();
    		try {
				t1.join();
				t2.join();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
    		result = t1.result + t2.result;
    		
    	}
    }
    public static void main(String[] args){
    	int n =14;
    	int[] results = new int[n+1];
    	Fibon[] fibs = new Fibon[n+1];
    	for(int i =0; i<=n; i++){
    		fibs[i] = new Fibon(i);
    	}
    	for(int i =0; i<=n; i++){
    		fibs[i].start();
    	}
    	for(int i =0; i<=n; i++){
    		try {
				fibs[i].join();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
    	}
    	for(int i =0; i<=n; i++){
    		results[i] = fibs[i].result;
    		System.out.println(results[i]);
    	}
    }
}