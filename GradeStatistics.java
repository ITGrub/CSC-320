import java.util.Scanner;

public class GradeStatistics {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        float[] grades = new float[10];
        float sum = 0;
        float max = Float.MIN_VALUE;
        float min = Float.MAX_VALUE;
        
        // Loop to read 10 grades
        for (int i = 0; i < 10; i++) {
            System.out.print("Enter grade " + (i + 1) + ": ");
            // Ensure the user enters a valid floating-point number
            while (!scanner.hasNextFloat()) {
                System.out.println("Invalid input. Please enter a numeric grade.");
                scanner.next(); // Clear the invalid input
                System.out.print("Enter grade " + (i + 1) + ": ");
            }
            grades[i] = scanner.nextFloat();
            sum += grades[i];

            // Update max and min
            if (grades[i] > max) {
                max = grades[i];
            }
            if (grades[i] < min) {
                min = grades[i];
            }
        }

        // Calculate average
        float average = sum / 10;

        // Display results
        System.out.printf("Average grade: %.2f\n", average);
        System.out.printf("Maximum grade: %.2f\n", max);
        System.out.printf("Minimum grade: %.2f\n", min);

        scanner.close();
    }
}