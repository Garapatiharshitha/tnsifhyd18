package clg.encapsulation;

public class WithGetSetMethod {
	int TotalScore = 140;
	int Wickets=9;
	private int Target=158;
	private int Overs=20;
	
	public int getTarget() {
		return Target;
	}
	public void setTarget(int target) {
		Target = target;
	}
	public int getOvers() {
		return Overs;
	}
	public void setOvers(int overs) {
		Overs = overs;
	}	
	public void check() {
		if((TotalScore<=Target) & Overs==20) {
		System.out.println("lost the match");
	}
	else {
		System.out.println("won the match");
	}
	}
}
