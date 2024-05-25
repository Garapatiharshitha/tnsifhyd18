package clg.staticinstancevariables;

class A{
	static void display1() {
		System.out.println("parent method");
	}
}
class B extends A {
	static void display1() {
		System.out.println("child method");
	}
}
public class OverridingStatic {
		
		public static void main(String[] args) {
			// TODO Auto-generated method stub
			B obj = new B();
			obj.display1();

		}
}
