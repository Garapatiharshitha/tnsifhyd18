package clg.encapsulation;

public class WithGetSet {
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
	
	
}
