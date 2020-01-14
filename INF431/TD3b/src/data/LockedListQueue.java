package data;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

import nodes.Node;

public class LockedListQueue implements MessageQueue {
    private static class Cell {
        public Message data;
        public Cell next;

        public Cell(Message data) {
            this.data = data;
            this.next = null;
        }
    }

    private Cell head, tail;
    private int length;

    private Lock modifyLock = new ReentrantLock();

    public LockedListQueue() {
        Cell sentinel = new Cell(null);
        this.head = this.tail = sentinel;
        this.length = 0;
    }

    @Override
    public boolean add(Message msg) {
        Cell newTail = new Cell(msg);
        modifyLock.lock();
        try {
            this.tail.next = newTail;
            this.tail = newTail;
            this.length++;
            return true;
        } finally {
            modifyLock.unlock();
        }
    }

    @Override
    public boolean isEmpty() {
        return this.length == 0;
    }

    @Override
    public Message remove() {
        while (true) {
            boolean retry = false;
            modifyLock.lock();
            try {
                Cell next = this.head.next;
                if (null == next) {
                    retry = true;
                    continue;
                }
                this.head = next;
                Message ret = next.data;
                next.data = null;
                this.length--;
                return ret;
            } finally {
                modifyLock.unlock();
                if (retry)
                    Node.sleepUninterruptibly(10);
            }
        }
    }
}
