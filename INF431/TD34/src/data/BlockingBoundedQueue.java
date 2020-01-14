package data;
import  java.util.concurrent.locks.*;
import nodes.Node;

public class BlockingBoundedQueue implements MessageQueue {
	 	private final Message[] queue;
	    private final int bound;
	    private int in, size;
	    private final Lock lock = new ReentrantLock();
	    private final Condition notEmpty = lock.newCondition(); 
	    private final Condition notFull = lock.newCondition(); 

	    public BlockingBoundedQueue(int max) {
	        this.queue = new Message[max];
	        this.bound = max;
	        this.in = 0;
	        this.size = 0;
	    }

	    public boolean isFull() {
	        return this.size >= this.bound;
	    }

	    @Override
	    public boolean add(Message msg) {
	    	lock.lock();
	    	try
	    	{
	    		while(this.isFull())
		    		notFull.awaitUninterruptibly();
		    	Boolean wasEmpty = this.isEmpty();
		        this.queue[this.in] = msg;
		        this.in = (this.in + 1) % this.bound;
		        ++this.size;
		        if(wasEmpty)
		        	notEmpty.signalAll();
		        return true;
	    	}
	    	finally
	    	{
	    		lock.unlock();
	    	}
	    	
	    }

	    @Override
	    public boolean isEmpty() {
	        return this.size == 0;
	    }

	    @Override
	    public Message remove() {
	    	lock.lock();
	    	try
	    	{
	    		while (this.isEmpty())
	    			notEmpty.awaitUninterruptibly();
	    		Boolean wasFull = this.isFull();  
		        int out = (this.in + this.bound - this.size) % this.bound;
		        Message thing = this.queue[out];
		        this.queue[out] = null;
		        --this.size;
		        if(wasFull)
		        	notFull.signalAll();
		        return thing;
	    	}
	    	finally
	    	{
	    		lock.unlock();
	    	}
	    	
	        
	    }

}
