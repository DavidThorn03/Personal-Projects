public class hex {
    public double hexDec(String Hex){
        double dec = 0;
        for(int i = 0; i <= Hex.length() - 1; i++){
            if(Hex.charAt(i) >= 48 && Hex.charAt(i) <= 57 ){
                dec = dec + (Hex.charAt(i) - 48) * (int)Math.pow(16 , Hex.length() - i - 1);
            }//end of if
            else if(Hex.charAt(i) >= 65 && Hex.charAt(i) <= 70 ){
                dec = dec + (Hex.charAt(i) - 55) * (int)Math.pow(16 , Hex.length() - i - 1);
            }//emd of else if 
        }//end of for 
        return dec;
    }//end of hexDec
    public String decHex(double dec){
        double num = dec;
        String hex = "";
        int place = 0;
        boolean valid = true;

        while(valid){
            if(num / 16 >= 1){
                place = place + 1;
            }//end of if
            else{
                valid = false;
            }//end of else 
            num = (int)(num / 16);
        }//end of while
        
        for(place = place; place >= 0; place--){
            if(dec%16 >= 0 && dec%16 <= 9){
                hex = (char)(dec%16 + 48) + hex;
            }//end of if

            if(dec%16 >= 10 && dec%16 <= 16){
                hex = (char)(dec%16 + 55) + hex;
            }//end of if
            dec = (int)(dec / 16);
        }//end of for
        return hex;
    }//end of decHex
}//end of class hex

