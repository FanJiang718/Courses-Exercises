package search;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.concurrent.LinkedBlockingQueue;

public class Searcher extends Thread {
    public static final String EOF = "--EOF--";
    private final BufferedReader data;
    private final String query;
    private final LinkedBlockingQueue<String> result;
    private int processedItems = 0;
    private int matchesFound = 0;

    public Searcher(BufferedReader data,
                    String query,
                    LinkedBlockingQueue<String> result){
        this.data = data;
        this.query = query;
        this.result = result;
    }

    public int getProcessedItems() {
        return this.processedItems;
    }

    public int getMatchesFound() {
        return this.matchesFound;
    }

    public void printStatus() {
        System.out.format("Thread %s processed %d items and found %d matching results.\n",
                          this.getName(), this.processedItems, this.matchesFound);
    }

    @Override
    public void run() {
        String current;
        while (true) {
            try { current = data.readLine(); }
            catch (IOException e) {
                current = null;
            }
            if (null == current) {
                this.result.add(Searcher.EOF);
                return;
            }
            this.processedItems ++;
            if (current.indexOf(query) >= 0) {
                this.matchesFound ++;
                this.result.add(current);
            }
            if (Thread.interrupted ()) return;
        }
    }

}
