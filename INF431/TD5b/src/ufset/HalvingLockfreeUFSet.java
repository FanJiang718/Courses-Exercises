package ufset;

import java.util.concurrent.atomic.AtomicIntegerArray;

public class HalvingLockfreeUFSet implements UFSet {
	 
	  private final AtomicIntegerArray parent;
	  private final AtomicIntegerArray rank;
	  
	  public final int size;

	  
	  public int getSize() {
		  return size;
	  }
	  
	  public HalvingLockfreeUFSet(int count) {
		this.size = count;	
	    this.parent = new AtomicIntegerArray(count);
	    this.rank = new AtomicIntegerArray(count);
	    for (int i = 0; i < count; i++) {
	      this.parent.set(i,i);
	    }
	  }

	  /**
	   * Find the canonical representative of the equivalence class of a given
	   * element by going up in the 'parent' relationship. Along the way, make any
	   * node traversed point to it's parent's parent, if the link did not change.
	   */
	  public int find(int x) {
	    while(x!=this.parent.get(x)) {
	    	int t = this.parent.get(x);
	    	this.parent.compareAndSet(x, t, this.parent.get(t));
	    	x = this.parent.get(x);
	    }
	    return x;
	  }
	
	  public boolean isSame(int x, int y) {
	    while (true) {
	      x = this.find(x);
	      y = this.find(y);
	      if (x == y)
	        return true;
	      if (this.parent.get(x) == x)
	        return false;
	    }
	  }

	  /**
	   *  We also need to modify link to avoid problems with concurrent union(x,y) and
	   *  union(y,x). In practice this proves even more efficient than ranks.
	   */
	  private boolean link(int x, int y) {
		  if(x<y) return this.parent.compareAndSet(x, x, y);
		  else return this.parent.compareAndSet(y,y,x);
	  }
	 
	  public void union(int x, int y) {
	    do {
	      do {
	        x = this.find(x);
	        y = this.find(y);
	        if (x == y)
	          return;
	      } while (!(x == this.parent.get(x) && y == this.parent.get(y)));
	    } while (!this.link(x, y));
	  }
}
