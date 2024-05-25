package clg.encapsulation;

public class AccessWithGetSetMethod {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		WithGetSetMethod obj=new WithGetSetMethod();
		System.out.println(obj.TotalScore);
		System.out.println(obj.Wickets);
		System.out.println(obj.getOvers());
		obj.setOvers(15);
		System.out.println("after using set():"+obj.getOvers());
        obj.check();
	}

}
