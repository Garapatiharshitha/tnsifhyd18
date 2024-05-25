package clg.encapsulation;

public class AccessWithGetSet {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		WithGetSet obj=new WithGetSet();
		System.out.println(obj.TotalScore);
		System.out.println(obj.Wickets);
		System.out.println(obj.getOvers());
		obj.setOvers(15);
		System.out.println("after using set():"+obj.getOvers());

	}

}
