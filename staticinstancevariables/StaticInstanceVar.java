package clg.staticinstancevariables;

public class StaticInstanceVar {
	static int NoOfBooks; //static variables
	static int NoOfAuthors;
	String Name; // Instance variables

	public static void main(String[] args) {
		// TODO Auto-generated method stub
			
			String genre="Mathematical Fiction";//simple local variable. it is not instance and not static.
			StaticInstanceVar obj = new StaticInstanceVar();
			
			//Assigning to static variable and Accessing by classname.staticvaraiblename
			StaticInstanceVar.NoOfBooks = 10;
			System.out.println(StaticInstanceVar.NoOfBooks);
				
			//Assigning to static variables and Accessing by static variable  
			NoOfAuthors = 7;
			System.out.println(NoOfAuthors);
			
			//Assigning to instance variable
			obj.Name="Mathematics";
			System.out.println(obj.Name);
			
			//accessing local variable
			System.out.println(genre);
			

	}

}
