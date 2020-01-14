package nodes;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import data.MessageProcessor;
import data.MessageQueue;
import data.Message;

public class ProcessorPool extends Processor {
    private final ExecutorService exec;

    public ProcessorPool(int concur, MessageQueue q, MessageProcessor p, String name) {
        super(q, p, name);
        this.exec = Executors.newFixedThreadPool(10);
    }

    @Override
    public void run() {
        while (true) {
            Message msg = this.queue.remove();
            this.exec.execute(new Runnable(){
            	@Override
            	public void run() {
            		processMessage(msg);
            	}
            });
        }
    }
}