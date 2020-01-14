package trees;

import graph.Place;

import java.util.HashMap;

// Q1

public class UnionFind {
	//parent relation, parent.put(src,dst) indicates that src points to dst
    private HashMap<Place,Place> parent;
    
    public UnionFind( ){
        this.parent = new HashMap<Place,Place>();
    }
    
    public Place find( Place src ){
    	if(this.parent.get(src)==null) this.parent.put(src,src);
    	if(src.equals(this.parent.get(src)))
    		return src;
    	else{
    		Place parent = find(this.parent.get(src));
    		this.parent.put(src, parent);
    		return parent;
    	}
    }
    
    public void union( Place v0, Place v1 ){
    	if(this.parent.get(v0)==null) this.parent.put(v0, v0);
    	if(this.parent.get(v1)==null) this.parent.put(v1, v1);
    	this.parent.put(find(v0), find(v1));
    	return;
    }
}
