package differentpackages;
//Importing necessary built-in packages
	import java.util.ArrayList; // For using the ArrayList class
	import java.util.Collections; // For using utility methods like sorting
	import java.util.Scanner; //reading input from keyboard

public class BasicBuiltinPack {
           public static void main(String[] args) {
	        // Create an ArrayList to store numbers
	        ArrayList<Integer> numbers = new ArrayList<>();
	        
	        // Add some numbers to the list
	        numbers.add(10);
	        numbers.add(5);
	        numbers.add(15);
	        numbers.add(20);

	        // Print the original list
	        System.out.println("Original list: " + numbers);

	        // Sort the list using Collections.sort() method
	        Collections.sort(numbers);
	        
	        // Print the sorted list
	        System.out.println("Sorted list: " + numbers);

	        // Reverse the list using Collections.reverse() method
	        Collections.reverse(numbers);
	        
	        // Print the reversed list
	        System.out.println("Reversed list: " + numbers);

	        // Reading input from the user
	        System.out.println("Enter some text:");
	        try (Scanner sc = new Scanner(System.in)) {
				// Read a line of text from the user
				String userInput = sc.nextLine();
				
				// Print the user's input
				System.out.println("You entered: " + userInput);
			}
	    }
	}
