import java.util.concurrent.locks.ReentrantLock;


public class SafeStack<E> implements Stack<E> {
	private StackNode<E> head;
	private ReentrantLock lock;
	
	
	public SafeStack() {
		head = null;
		lock = new ReentrantLock();
	}
	public void push(E e) {
				StackNode<E> n= new StackNode<E>(e);
				lock.lock();
				try{
					n.next = head;
					head = n;
				}
				finally {
					lock.unlock(); 
				}
				
	}

	public E pop() {
		 StackNode<E> n = null;
		 if (head == null )
			return null;
		 else {
			 lock.lock();
			 try{
			 	n = head;
			 	head = head.next;
			 }
			 finally{
				 lock.unlock();
			 }
			 return n.item;
	}
	}


}
