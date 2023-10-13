import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;
import java.util.Scanner;

public class RMIServer {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            InterestCalculator interestCalculator = new InterestCalculatorImpl();
            LocateRegistry.createRegistry(1099);
            Naming.rebind("InterestCalculator", interestCalculator);
            System.out.println("Server is ready.");

            // Server can continue running while waiting for user input
            System.out.println("Press Enter to exit the server.");
            scanner.nextLine();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // Close the scanner to prevent resource leak
            if (scanner != null) {
                scanner.close();
            }
        }
    }
}
