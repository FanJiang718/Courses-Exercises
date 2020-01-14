package trees;

import java.util.*;

import graph.*;

public class SpanningTree {
    
    public static Collection<Edge> kruskal(UnionFind u, EuclideanGraph g){
    	LinkedList<Edge> allEdges =  (LinkedList<Edge>) g.getAllEdges();
    	EdgeComparator edcomapre = new EdgeComparator();;
    	Collection<Edge> result = new LinkedList<Edge>();
    	Collections.sort(allEdges,edcomapre);
    	for(Edge e: allEdges){
    		Place v0 = e.source;
    		Place v1 = e.target;
    		if(!u.find(v0).equals(u.find(v1))){
    			result.add(e);
    			u.union(v0, v1);
    		}
    	}
    	return result;
    }
    
    public static Collection<Collection<Edge>> kruskal(EuclideanGraph g){
    	UnionFind u = new UnionFind();
    	HashMap<Place,Collection<Edge>> connectedTree = new HashMap<Place,Collection<Edge>>();
    	LinkedList<Edge> edges = (LinkedList<Edge>) SpanningTree.kruskal(u,g);
    	for(Edge e: edges){
    		Place v0 = e.target;
    		Place r0 = u.find(v0);
    		if(connectedTree.get(r0) == null){
    			connectedTree.put(r0, new LinkedList<Edge>());
    		}
    		connectedTree.get(r0).add(e);
    	}
    	return connectedTree.values();
    }
    
    public static Collection<Edge> primTree(HashSet<Place> nonVisited, Place start, EuclideanGraph g){
    	Collection<Edge> result = new LinkedList<Edge>();
    	EdgeComparator compareEdge = new EdgeComparator();
    	PriorityQueue<Edge> queue = new PriorityQueue<Edge>(11, compareEdge);
    	for(Edge e: g.edgesOut(start)){
    		queue.add(e);
    	}
    	nonVisited.remove(start);
    	while(!queue.isEmpty()){
    		Edge e = queue.poll();    		
    		Place target = e.target;
    		if(nonVisited.contains(target)){
    			for(Edge edge: g.edgesOut(target)){
    				queue.add(edge);
    			}
    			nonVisited.remove(target);
    			result.add(e);
    		}
    		
    	}
    	return result;
    }

    public static Collection<Collection<Edge>> primForest(EuclideanGraph g){
    	HashSet<Place> nonVisited = new HashSet<Place>();
    	for(Place v: g.places()){
    		nonVisited.add(v);
    	}
    	HashMap<Place,Collection<Edge>> connectedTree = new HashMap<Place,Collection<Edge>>();
    	while(!nonVisited.isEmpty()){
    		Place start = SpanningTree.getStartPlace(nonVisited);
    		Collection<Edge> tmp = SpanningTree.primTree(nonVisited, start, g);
    		if(!tmp.isEmpty()) connectedTree.put(start, tmp);
    	}
    	return connectedTree.values();
    }

    public static Place getStartPlace(HashSet<Place> set){
    	Place tmp = null;
    	for(Place v: set){
    		tmp = v;
    		break;
    	}
    	return tmp;
    }
    
}
