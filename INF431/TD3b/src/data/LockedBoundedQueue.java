package data;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class LockedBoundedQueue implements MessageQueue {

    private final Message[] queue;
    private int in, size;

    private final Lock modifyLock = new ReentrantLock();

    public LockedBoundedQueue(int max) {
        this.queue = new Message[max];
        this.in = 0;
        this.size = 0;
    }

    public boolean isFull() {
        return this.size >= this.queue.length;
    }

    @Override
    public boolean add(Message msg) {
        modifyLock.lock();
        try {
            if (this.isFull()) return false;
            this.queue[this.in] = msg;
            this.in = (this.in + 1) % this.queue.length;
            ++this.size;
            return true;
        } finally {
            modifyLock.unlock();
        }
    }

    @Override
    public boolean isEmpty() {
        return this.size == 0;
    }

    @Override
    public Message remove() {
        while (true) {
            modifyLock.lock();
            try {
                if (this.isEmpty()) continue;
                int out = (this.in + this.queue.length - this.size)
                        % this.queue.length;
                Message thing = this.queue[out];
                this.queue[out] = null;
                --this.size;
                return thing;
            } finally {
                modifyLock.unlock();
            }
        }
    }
}
