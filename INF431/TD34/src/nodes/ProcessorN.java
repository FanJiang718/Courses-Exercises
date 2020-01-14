package nodes;

import data.MessageProcessor;
import data.MessageQueue;

public class ProcessorN extends Processor {

	int numThreads;
    public ProcessorN(int numThreads, MessageQueue q, MessageProcessor p,
            String name) {
        super(q, p, name);
        this.numThreads = numThreads;
        
    }

    @Override
    public void init() {
        // your code here
    	Thread[] threads = new Thread[this.numThreads];
    	for(int i=0; i < this.numThreads; i++) {
    		threads[i] = new Thread(this);
    		threads[i].start();
    	}
    }
}
