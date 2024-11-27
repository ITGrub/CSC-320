import java.io.FileWriter;
import java.io.IOException;

public class Automobile {
    private String make;
    private String model;
    private String color;
    private int year;
    private int mileage;

    // Default constructor
    public Automobile() {
        this.make = "";
        this.model = "";
        this.color = "";
        this.year = 0;
        this.mileage = 0;
    }

    // Parameterized constructor
    public Automobile(String make, String model, String color, int year, int mileage) {
        this.make = make;
        this.model = model;
        this.color = color;
        this.year = year;
        this.mileage = mileage;
    }

    // Add a new vehicle
    public String addNewVehicle(String make, String model, String color, int year, int mileage) {
        try {
            this.make = make;
            this.model = model;
            this.color = color;
            this.year = year;
            this.mileage = mileage;
            return "Vehicle added successfully!";
        } catch (Exception e) {
            return "Error adding vehicle: " + e.getMessage();
        }
    }

    // List vehicle information
    public String[] listVehicleInformation() {
        try {
            return new String[]{make, model, color, String.valueOf(year), String.valueOf(mileage)};
        } catch (Exception e) {
            return new String[]{"Error listing vehicle information: " + e.getMessage()};
        }
    }

    // Remove vehicle
    public String removeVehicle() {
        try {
            this.make = "";
            this.model = "";
            this.color = "";
            this.year = 0;
            this.mileage = 0;
            return "Vehicle removed successfully!";
        } catch (Exception e) {
            return "Error removing vehicle: " + e.getMessage();
        }
    }

    // Update vehicle attributes
    public String updateVehicle(String make, String model, String color, int year, int mileage) {
        try {
            this.make = make;
            this.model = model;
            this.color = color;
            this.year = year;
            this.mileage = mileage;
            return "Vehicle updated successfully!";
        } catch (Exception e) {
            return "Error updating vehicle: " + e.getMessage();
        }
    }

    // Write vehicle information to file
    public void printToFile(String[] vehicleInfo, String filePath) {
        try {
            FileWriter writer = new FileWriter(filePath);
            writer.write("Make: " + vehicleInfo[0] + "\n");
            writer.write("Model: " + vehicleInfo[1] + "\n");
            writer.write("Color: " + vehicleInfo[2] + "\n");
            writer.write("Year: " + vehicleInfo[3] + "\n");
            writer.write("Mileage: " + vehicleInfo[4] + "\n");
            writer.close();
            System.out.println("Vehicle information has been written to " + filePath);
        } catch (IOException e) {
            System.out.println("Error writing to file: " + e.getMessage());
        }
    }
}
