package clg.staticinstancevariables;
class C{
	static void display() {
		System.out.println("parent method");
	}
}
class D {
	static int display() {
		return 10;
	}
}
public class OverloadingStatic {
		public static void main(String[] args) {
			D obj=new D();
			System.out.println(D.display());
		}
		
	}
