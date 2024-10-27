import java.util.Scanner;

public class TaxCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Input weekly income
        System.out.print("Enter the weekly income: ");
        double weeklyIncome = scanner.nextDouble();
        
        // Determine the tax rate based on income brackets
        double taxRate;
        if (weeklyIncome < 500) {
            taxRate = 0.10;
        } else if (weeklyIncome >= 500 && weeklyIncome < 1500) {
            taxRate = 0.15;
        } else if (weeklyIncome >= 1500 && weeklyIncome < 2500) {
            taxRate = 0.20;
        } else {
            taxRate = 0.30;
        }
        
        // Calculate the tax withholding
        double taxWithholding = weeklyIncome * taxRate;
        
        // Display the tax withholding
        System.out.printf("The weekly tax withholding for an income of $%.2f is $%.2f%n", weeklyIncome, taxWithholding);
        
        
        scanner.close();
    }
}
