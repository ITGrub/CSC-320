import java.util.Scanner;

public class AutomobileInventory {
    public static void main(String[] args) {
        try {
            // Create a new automobile object using the parameterized constructor
            Automobile vehicle1 = new Automobile("Toyota", "Supra", "Red", 2020, 15000);

            // List the vehicle information
            String[] vehicleInfo = vehicle1.listVehicleInformation();
            System.out.println("Vehicle Information:");
            for (String info : vehicleInfo) {
                System.out.println(info);
            }

            // Remove the vehicle
            System.out.println(vehicle1.removeVehicle());

            // Add a new vehicle
            System.out.println(vehicle1.addNewVehicle("Honda", "Civic", "Blue", 2022, 5000));

            // List the new vehicle's information
            vehicleInfo = vehicle1.listVehicleInformation();
            System.out.println("New Vehicle Information:");
            for (String info : vehicleInfo) {
                System.out.println(info);
            }

            // Update vehicle information
            System.out.println(vehicle1.updateVehicle("Subaru", "WRX", "Black", 2023, 1800));

            // List the updated vehicle's information
            vehicleInfo = vehicle1.listVehicleInformation();
            System.out.println("Updated Vehicle Information:");
            for (String info : vehicleInfo) {
                System.out.println(info);
            }

            // Ask user if they want to print to a file
            Scanner scanner = new Scanner(System.in);
            System.out.print("Would you like to print the vehicle information to a file (Y/N)? ");
            String response = scanner.nextLine();

            if (response.equalsIgnoreCase("Y")) {
                String filePath = "C:\\Printed\\Form.txt";
                vehicle1.printToFile(vehicleInfo, filePath);
            } else {
                System.out.println("The vehicle information will not be printed to a file.");
            }

        } catch (Exception e) {
            System.out.println("Error in the program: " + e.getMessage());
        }
    }
}