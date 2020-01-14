package search;
import java.io.BufferedReader;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.*;

public class Manager {
    public static LinkedBlockingQueue<String> simpleSearch(BufferedReader data, String query, int num)
        throws InterruptedException{
        LinkedBlockingQueue<String> result = new LinkedBlockingQueue<>();
        Searcher s = new Searcher(data,query,result);
        s.setName("searcher");
        s.start();
        Thread.sleep(100);
        s.printStatus();
        return result;
    }

    public static LinkedBlockingQueue<String> pollingSearch(BufferedReader data, String query, int num)
        throws InterruptedException{
        LinkedBlockingQueue<String> result = new LinkedBlockingQueue<>();
        Searcher s = new Searcher(data,query,result);
        s.setName("searcher");
        s.start();
        do {
            Thread.sleep(100);
            s.printStatus();
        } while (s.isAlive ()) ;
        return result;
    }

    public static LinkedBlockingQueue<String> waitingSearch(BufferedReader data, String query, int num)
        throws InterruptedException{
        LinkedBlockingQueue<String> result = new LinkedBlockingQueue<>();
        Searcher s = new Searcher(data,query,result);
        s.setName("searcher");
        s.start();
        s.join();
        s.printStatus();
        return result;
    }

    public static LinkedBlockingQueue<String> pipelinedSearch(BufferedReader data, String query, int num)
        throws InterruptedException{
        LinkedBlockingQueue<String> result = new LinkedBlockingQueue<>();
        Searcher s = new Searcher(data,query,result);
        Printer p = new Printer(result);
        s.setName("searcher"); s.start();
        p.setName("printer"); p.start();
        s.join();
        s.printStatus();
        p.join();
        p.printStatus();
        return result;
    }

    public static LinkedBlockingQueue<String> interruptingSearch(BufferedReader data, String query, int num)
        throws InterruptedException{
        LinkedBlockingQueue<String> result = new LinkedBlockingQueue<>();
        Searcher s = new Searcher(data,query,result);
        Printer p = new Printer(result,num);
        s.setName("searcher"); s.start();
        p.setName("printer"); p.start();
        p.join();
        s.interrupt();
        s.join();
        s.printStatus();
        p.printStatus();
        return result;
    }

    public static LinkedBlockingQueue<String> concurrentSearch(BufferedReader data, String query, int num)
        throws InterruptedException{
        LinkedBlockingQueue<String> result = new LinkedBlockingQueue<>();
        Searcher s1 = new Searcher(data,query,result);
        Searcher s2 = new Searcher(data,query,result);
        Printer p = new Printer(result,num);
        s1.setName("searcher1"); s1.start();
        s2.setName("searcher2"); s2.start();
        p.setName("printer"); p.start();
        p.join();
        s1.interrupt(); s2.interrupt();
        s1.join(); s1.printStatus();
        s2.join(); s2.printStatus();
        p.printStatus();
        return result;
    }

    public static LinkedBlockingQueue<String> search(BufferedReader data, String query, int num){
        try{
            return concurrentSearch(data,query,num);
        }
        catch (InterruptedException e){
            System.out.println("Search interrupted.");
            throw new RuntimeException("Unexpected search interruption");
        }
    }

    public static Map<String,Integer> count(BufferedReader data, String[] queries) {
        try {
            LinkedBlockingQueue<String> result = new LinkedBlockingQueue<>();
            int nProcs = java.lang.Runtime.getRuntime().availableProcessors();
            MapFrequency[] maps = new MapFrequency[nProcs];
            for (int i = 0 ; i < maps.length ; i ++) {
                maps[i] = new MapFrequency(data, queries, result);
                maps[i].setName("map" + (i + 1));
            }
            ReduceFrequency red = new ReduceFrequency(result);
            for (MapFrequency m : maps) m.start();
            red.setName("reduce"); red.start();
            for (MapFrequency m : maps) {
                m.join();
                m.printStatus();
            }
            red.interrupt();
            red.join();
            red.printStatus();
            return red.count;
        } catch (InterruptedException e) {
            System.out.println("Count interrupted.");
            throw new RuntimeException("Unexpected count interruption");
        }
    }
}
