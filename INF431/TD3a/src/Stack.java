public class Stack<E>{
	private Element head;
	
	private class Element{
		private E content;
		private Element next;
		
		private Element(E content, Element next){
			this.content = content;
			this.next = next;
		}
	}
	
	public E pop(){
		if(head==null) return null;
		E content = head.content;
		head = head.next;
		return content;
	}
	
	public void push(E el){
		Element e = new Element(el, head);
		head = e;
	}
}