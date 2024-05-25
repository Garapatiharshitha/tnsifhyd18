package clg.encapsulation;

public class AccessingVar {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		WithVariables obj=new WithVariables();
		System.out.println(obj.TotalScore);
		System.out.println(obj.Wickets);
		//it will give an error when trying to access private variable
	//	System.out.println(obj.Overs);
	}
}