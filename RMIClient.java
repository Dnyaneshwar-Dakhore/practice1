import java.rmi.Naming;
import java.util.Scanner;

public class RMIClient {
    public static void main(String[] args) {
        try {
            InterestCalculator interestCalculator = (InterestCalculator) Naming.lookup("rmi://localhost/InterestCalculator");
            Scanner scanner = new Scanner(System.in);

            while (true) {
                System.out.print("Enter principal (or 'exit' to quit): ");
                String input = scanner.nextLine();

                if (input.equalsIgnoreCase("exit")) {
                    break;
                }

                double principal = Double.parseDouble(input);
                System.out.print("Enter rate: ");
                double rate = Double.parseDouble(scanner.nextLine());
                System.out.print("Enter years: ");
                int years = Integer.parseInt(scanner.nextLine());

                double result = interestCalculator.calculateSimpleInterest(principal, rate, years);
                System.out.println("Simple Interest: " + result);
            }

            scanner.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
