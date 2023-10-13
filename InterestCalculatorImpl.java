import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class InterestCalculatorImpl extends UnicastRemoteObject implements InterestCalculator {

    public InterestCalculatorImpl() throws RemoteException {
        super();
    }

    @Override
    public double calculateSimpleInterest(double principal, double rate, int years) throws RemoteException {
        return (principal * rate * years) / 100;
    }
}
