import java.util.ArrayList;
import java.io.*;

public class IO {
    public addPrimes(ArrayList<Double> primes) {
        try{
            for(double num : primes){
   
            FileWriter fw = new FileWriter("./nums.txt", true);
            PrintWriter pw = new PrintWriter(fw);
    
            pw.print(num + " ");
    
            pw.close();
            }
        }
    
        catch(IOException e){
            System.out.printf("Cannot write to nums file\n" );
        }
    }
    public ArrayList<Double> getPrimes(double n) {
        ArrayList<Double> primes = new ArrayList<Double>();
        String[] tokens;
        try{
            FileReader fr = new FileReader("./nums.txt");
            BufferedReader br = new BufferedReader(fr);
            String line;
    
            while((line = br.readLine()) != null){
                tokens = line.split(" ");
            }
            fr.close();
            for(String token : tokens){
                if(Double.parseDouble(token) <= n){
                    primes.add(Double.parseDouble(token));
                }
                else{
                    primes.add(-1.0);
                    break;
                }
            }
        }
        catch(IOException e){
            System.out.printf("Error: Cannot read from file nums\n");
        }
    }
}