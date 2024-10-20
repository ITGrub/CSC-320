import java.util.Scanner;

public class random_person_class {
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        
        
        System.out.print("Enter first name: ");
        String name1 = scanner.nextLine();
        
        
        System.out.print("Enter last name: ");
        String name2 = scanner.nextLine();
        
        
        System.out.print("Enter street address: ");
        String name3 = scanner.nextLine();
        
        System.out.print("Enter city: ");
        String name4 = scanner.nextLine();
        
        System.out.print("Enter zip code: ");
        String name5 = scanner.nextLine();
        
        // Print the gathered information
        System.out.println("The random person's first name is " + name1);
        System.out.println("The random person's last name is " + name2);
        System.out.println("The random person's address is " + name3);
        System.out.println("The random person is from " + name4);
        System.out.println("The random person's zip code is " + name5);
        // Close the scanner
        scanner.close();
    }
}