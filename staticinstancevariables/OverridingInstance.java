package clg.staticinstancevariables;

class Parent{
	void display() {
		System.out.println("parent method");
	}
}
class Child extends Parent {
	void display() {
		System.out.println("child method");
	}
}
public class OverridingInstance {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Child obj = new Child();
		obj.display();

	}

}
