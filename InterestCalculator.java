import java.rmi.Remote;
import java.rmi.RemoteException;

public interface InterestCalculator extends Remote {
    double calculateSimpleInterest(double principal, double rate, int years) throws RemoteException;
}
