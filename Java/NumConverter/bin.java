import java.lang.Math;
public class bin {
    public double binDec(double bin){
        double num = bin;
        double dec = 0;
        int place = 0;

        for(num = num;  num >= 1; num = num / 10){
            if(num%10 == 1){
                dec = dec + (int)Math.pow(2 , place);
                num = num - 1;
            }//end of if
            place = place + 1;
        }//end of for 
        return dec;
    }//end of binDec

    public double decBin(double dec){
        double num = dec;
        double bin = 0;
        int place = 0;
        boolean valid = true;

        while(valid){
            if(num / 2 >= 1){
                place = place + 1;
            }//end of if
            else{
                valid = false;
            }//end of else 
            num = (int)(num / 2);
        }//end of while

        for(int i = place; i >= 0; i--){
            if(dec%2 == 1){
                bin = bin + 1*(int)Math.pow(10 , place - i);
            }//end of if 
            dec = (int)(dec / 2);
        }//end of for
        return bin;
    }//end of decBin
}//end of class bin
