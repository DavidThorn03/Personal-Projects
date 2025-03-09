import java.util.ArrayList;

public class Primes {
    public static ArrayList<Double> primesLessThan(double n) {
        ArrayList<Double> primes = new ArrayList<Double>();
        for (double i = 2; i <= n; i++) {
            if (IsPrime.isPrime(i)) {
                primes.add(i);
            }
        }
        return primes;
    }

    public static ArrayList<Double> primesWithSaved(double n){
        ArrayList<Double> primes = new ArrayList<Double>();
        IO io = new IO();
        primes = io.getPrimes(n);
        if(primes.get(primes.size() - 1) == -1.0){
            primes.remove(primes.size() - 1);
            return primes;
        }
        ArrayList<Double> newPrimes = new ArrayList<Double>();
        for(double i = primes.get(primes.size() - 1); i <= n; i++){
            if(IsPrime.isPrime(i)){
                newPrimes.add(i);
                primes.add(i);
            }
        }
        io.addPrimes(newPrimes);
        return primes;
    }
}
