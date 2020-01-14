package search;

import java.util.concurrent.LinkedBlockingQueue;

public class Printer extends Thread {
    LinkedBlockingQueue<String> in;
    final int num;
    int items = 0;

    public Printer (LinkedBlockingQueue<String> in) {
        this.in = in;
        this.num = 0;
    }

    public Printer (LinkedBlockingQueue<String> in, int num) {
        this.in = in;
        this.num = num;
    }

    public void printStatus() {
        System.out.format("Thread %s processed %d items.\n",
                          this.getName(), this.items);
    }

    @Override
    public void run() {
        while (true) {
            if (this.items >= this.num) return;
            try {
                String s = in.take();
                if (s.equals(Searcher.EOF)) return;
                this.items ++;
                System.out.println(s);
            } catch (InterruptedException e) { return; }
        }
    }
}
