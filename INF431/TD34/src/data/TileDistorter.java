package data;
import util.PixelBuffer;

import java.util.Collection;
import java.util.LinkedList;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveAction;

public class TileDistorter implements MessageProcessor {
    private final PixelDistorter distorter;
    private final int threshold;
    ForkJoinPool pool;
    
    private class Computation extends RecursiveAction{
    	PixelBuffer buf;
    	int x,y,w,h;
    	int[] pixels;
    	
    	
    	public Computation(PixelBuffer buf, int x,int y,int w,int h, int[] pixels) {
    		this.buf = buf;
    		this.x= x;
    		this.y = y;
    		this.w = w;
    		this.h = h;
    		this.pixels = pixels;
    	}
    	
    	public void compute(){
    		if((this.w*this.h) < threshold){
    	    	for(int i=x; i< x+w; i++) {
    	    		for(int j= y; j< y+h;j++) {
    	    			pixels[j*w+i] = distorter.process(buf, i, j);
    	    		}
    	    	}
    	    	return;
    		}
    		else{
    			Collection<Computation> subproblems = new LinkedList<Computation>();
    			int n =8;
    			int tmp_y = y;
    			for(int i =0; i< n-1; i++){
    				subproblems.add(new Computation(buf,x,tmp_y,w,h/n,pixels));
    				tmp_y+=h/n;
    			}
    			subproblems.add(new Computation(buf,x,tmp_y,w,h-tmp_y,pixels));
    			invokeAll(subproblems);
    		}
    			
    	}
    }

    public TileDistorter(int parallelism, PixelDistorter distorter,
            int threshold) {
        this.distorter = distorter;
        this.threshold = threshold;
        pool = new ForkJoinPool(parallelism);
    }

    public TileDistorter(int parallelism, PixelDistorter distorter) {
        this(parallelism, distorter, 64);
    }

    private Message processTile(TileMessage msg) {
        // replace this with your code
    	int[] pixel = new int[msg.buf.pixels.length]; 
    			//msg.buf.pixels.clone();
    	Computation computs = new Computation(msg.buf,msg.x,msg.y,msg.w,msg.h,pixel);

    	pool.invoke(computs);

    	while(!pool.isTerminated()){
    		System.out.println(pool.getPoolSize());
    		System.out.println("not finished");
    	}
    	
    	PixelBuffer newbuf = new PixelBuffer(pixel,msg.w,msg.h);
    	TileMessage newmsg = new TileMessage(msg.channel,newbuf ,msg.x,msg.y,msg.w,msg.h);
        return newmsg;
    }

    @Override
    public Message process(Message msg) {
        if (msg instanceof TileMessage)
            return this.processTile((TileMessage) msg);
        else {
            throw new IllegalArgumentException("TileDistorter: invalid message");
        }
    }

}
