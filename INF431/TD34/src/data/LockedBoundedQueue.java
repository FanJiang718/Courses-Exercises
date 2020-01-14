package data;
import java.util.concurrent.locks.ReentrantLock;
import nodes.Node;

public class LockedBoundedQueue implements MessageQueue {

    private final Message[] queue;
    private final int bound;
    private int in, size;
    ReentrantLock mylock = new ReentrantLock();
    
    public LockedBoundedQueue(int max) {
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
    	mylock.lock();
    	try{
            if (this.isFull()) return false;
            this.queue[this.in] = msg;
            this.in = (this.in + 1) % this.bound;
            ++this.size;
            return true;
    	}
    	finally{
    		mylock.unlock();
    	}

    }

    @Override
    public boolean isEmpty() {
        return this.size == 0;
    }

    @Override
    public Message remove() {
    	mylock.lock();
    	try{
            while (true) {
                if (!this.isEmpty()) break;
                mylock.unlock();
                Node.sleepUninterruptibly(10);
                mylock.lock();
            }
            int out = (this.in + this.bound - this.size) % this.bound;
            Message thing = this.queue[out];
            this.queue[out] = null;
            --this.size;
            return thing;
    	}
    	finally{
    		mylock.unlock();
    	}

    }

}
