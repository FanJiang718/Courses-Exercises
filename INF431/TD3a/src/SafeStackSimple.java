
public class SafeStackSimple<E> extends Stack<E> {
	private VerySimpleLock lock = new VerySimpleLock();

	public E pop() {
		E r;
		lock.lock();
		try {
			r = super.pop();
		} finally {
			lock.unlock();

		}
		return r;
	}

	public void push(E el) {
		lock.lock();
		try{
			super.push(el);
		}finally{
			lock.unlock();
		}
	}
}
