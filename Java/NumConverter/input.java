import java.util.Scanner; //import scanner function
class input {
//for user input with high and low values
    public double validator(String prompt, String errorMsg, int low , int high){
        Scanner in = new Scanner(System.in);
        double num = 0;
        String userInput;
        boolean valid = false;

        while(valid == false){//to repeat till valid entry is recieved

//prompt user input
            System.out.print(prompt);
            userInput = in.nextLine();

            try{//if input is a number
                num = Double.parseDouble(userInput);

                if(num <= high && num >= low){//if input is within range
                    valid = true;
                }//end of if

                else{//if input is out of range
                    System.out.println(errorMsg);
                }//end of else 
            }//end of try

            catch(NumberFormatException e){//if input isnt a number
                System.out.println(errorMsg);
            
            }//end of catch
        }//end of while
        return num;

    }//end of validator

//for user input of double
    public double validator(String prompt, String errorMsg){
        Scanner in = new Scanner(System.in);
        double num = 0;
        String userInput;
        boolean valid = false;

        while(valid == false){//to repeat till valid entry is recieved

//prompt user input
            System.out.print(prompt);
            userInput = in.nextLine();

            try{//if input is a number
                num = Integer.parseInt(userInput); 
                valid = true;
            }//end of try

            catch(NumberFormatException e){//if input isnt a number
                System.out.println(errorMsg);
            }//end of catch
        }//end of while
        return num;
    }//end of validator


    public static String validator(String prompt){
        Scanner in = new Scanner(System.in);
        String num;
        String userInput = "";
        boolean valid = false;

        while(valid == false){//to repeat till valid entry is recieved
//prompt user input
            System.out.print(prompt);
            userInput = in.nextLine();
            for(int i = 0; i < userInput.length(); i++){
                char j = userInput.charAt(i);
                valid = false;
                if(!((j >= 48 && j <= 57) || (j >= 65 && j <= 70))){
                    valid = false;
                    System.out.println("Invalid choice entered");
                }//end of if
                else{
                    valid = true;
                }
            }//end of for
        }//end of while
        return userInput;
    }//end of validator
}//end of class

