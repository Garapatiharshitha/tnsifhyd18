package clg.staticinstancevariables;

class Parents{
	void display() {
		System.out.println("parent method");
	}
}
class Childs {
	int display() {
		return 10;
	}
}
public class OverloadingInstance {
	public static void main(String[] args) {
		Childs obj=new Childs();
		System.out.println(obj.display());
	}
	
}
