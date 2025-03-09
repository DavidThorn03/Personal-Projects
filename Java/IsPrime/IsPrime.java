import java.util.ArrayList;


public class IsPrime {
    public static void main(String[] args) {
        double n = 1000;
        ArrayList<Double> primes = new ArrayList<Double>();
        primes = isPrime(n);
        for(int i = 0; i < primes.size(); i++) {
            System.out.println(primes.get(i));
        }
    }
    public static boolean isPrime(double n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
