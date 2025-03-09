import java.util.Scanner;
public class main{
    public static void main(String [] args){
        double intype;
        double outtype;

        double bin = -1;
        double dec = -1;
        String hex = "";
        
        input kb = new input();
        bin binary = new bin();
        hex hexidec = new hex();

        gui myJFrame = new gui();

        System.out.printf("1. Decimal \n2. Binary \n3. Hexidecimal\n");

        intype = kb.validator("Input type: " , "Invalid choice entered" , 1 , 3);
        
        outtype = kb.validator("Output type: " , "Invalid choice entered" , 1 , 3);

        if (intype == 1){
            dec = kb.validator("Decimal value: " , "Invalid choice entered");
        }
        else if (intype == 2){
            bin = kb.validator("Binary value: " , "Invalid choice entered");
            dec = binary.binDec(bin);
        }
        else if (intype == 3){
            hex = kb.validator("Hexidecimal value: ");
            dec = hexidec.hexDec(hex);
        }

        if (outtype == 1){
            System.out.printf("Decimal value: %.0f\n" , dec);
        }
        else if (outtype == 2){
            bin = binary.decBin(dec);
            System.out.printf("Binary value: %.0f\n" , bin);
        }
        else if (outtype == 3){
            hex = hexidec.decHex(dec);
            System.out.printf("Hexidecimal value: %s" , hex);
        }

    }
}