import java.util.ArrayList;
import java.util.Scanner;

public class WeeklyTemperatureTracker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> days = new ArrayList<>();
        ArrayList<Double> temperatures = new ArrayList<>();
        
        // Days of the week array for reference
        String[] weekDays = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};

        System.out.println("Enter the average temperature for each day of the week.");
        System.out.println("Type 'week' to display all temperatures and the weekly average.");
        
        // Collect temperatures for each day
        for (String day : weekDays) {
            System.out.print("Enter temperature for " + day + " (or type 'week' to end early): ");
            String input = scanner.nextLine();
            
            // Check if user wants to end early and display the weekly report
            if (input.equalsIgnoreCase("week")) {
                break;
            }
            
            try {
                // Parse temperature input and store day and temperature
                double temperature = Double.parseDouble(input);
                days.add(day);
                temperatures.add(temperature);
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a numerical temperature.");
            }
        }
        
        // Display temperatures and calculate weekly average
        if (!days.isEmpty()) {
            double totalTemp = 0;
            System.out.println("\nTemperatures for the week:");
            for (int i = 0; i < days.size(); i++) {
                System.out.println(days.get(i) + ": " + temperatures.get(i) + "°F");
                totalTemp += temperatures.get(i);
            }
            
            // Calculate and display weekly average temperature
            double weeklyAverage = totalTemp / days.size();
            System.out.printf("Weekly Average Temperature: %.2f°F\n", weeklyAverage);
        } else {
            System.out.println("No temperatures recorded.");
        }

        scanner.close();
    }
}