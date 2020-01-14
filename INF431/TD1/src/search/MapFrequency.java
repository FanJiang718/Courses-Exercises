package search;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.concurrent.LinkedBlockingQueue;

public class MapFrequency extends Thread {
    private final BufferedReader data;
    private final String[] queries;
    private final LinkedBlockingQueue<String> result;
    int processedItems;
    int matchesFound;

    public MapFrequency(BufferedReader data, String[] queries, LinkedBlockingQueue<String> result) {
        this.data = data;
        this.queries = queries;
        this.result = result;
        this.processedItems = 0;
        this.matchesFound = 0;
    }

    public void printStatus() {
        System.out.format("Thread \"%s\" processed %d items and found %d matching results.\n",
                          this.getName(), this.processedItems, this.matchesFound);
    }

    @Override
    public void run() {
        while (true) {
            String line = null;
            try { line = this.data.readLine(); }
            catch (IOException e) { }

            if (null == line) {
                this.result.add (Searcher.EOF);
                return;
            }

            this.processedItems ++;

            for (String q : queries) {
                if (line.indexOf(q) >= 0) {
                    this.result.add(q);
                    this.matchesFound ++;
                }
            }

            if (Thread.interrupted()) return;
        }
    }
}
