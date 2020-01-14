package search;

import java.util.*;
import java.util.concurrent.*;
import java.io.*;

public class ReduceFrequency extends Thread {
    private final LinkedBlockingQueue<String> in;
    public final Map<String,Integer> count;
    private int items;

    public ReduceFrequency (LinkedBlockingQueue<String> in) {
        this.in = in ;
        this.items = 0 ;
        this.count = new HashMap<>() ;
    }

    public void printStatus() {
        System.out.format("Thread \"%s\" processed %d items.\n",
                          this.getName(), this.items);
    }

    @Override
    public void run() {
        while (true) {
            try {
                String line = in.take();
                if (line.equals(Searcher.EOF)) return;
                this.items ++;
                Integer oldCount = this.count.get(line);
                this.count.put(line, null == oldCount ? 1 : oldCount + 1);
                if (Thread.interrupted()) return;
            } catch (InterruptedException e) { return; }
        }
    }
}
