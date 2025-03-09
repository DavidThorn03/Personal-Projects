import java.awt.*;
import java.util.ArrayList;
import java.util.Random;
import javax.swing.*;

public class Main extends JFrame{
    Random rand = new Random();
    ArrayList<String> europeanCountries;
    boolean isComplete = false;
    public Main(){
        setTitle("Random European Countries");

        JPanel panel = new JPanel(new BorderLayout());
        ArrayList<String> countries = fillArray();

        JLabel label = new JLabel(countries.get(0));
        label.setFont(new Font("San serif", Font.BOLD, 20));
        label.setHorizontalAlignment(SwingConstants.CENTER);
        panel.add(label, BorderLayout.CENTER);

        JButton button = new JButton("Next");
        button.addActionListener(e -> {
            if(isComplete){
                this.dispose();
            }
            if(countries.size() > 1){
                countries.remove(0);
                label.setText(countries.get(0));
            }else{
                label.setText("Europe is complete!");
                isComplete = true;
            }
        });
        panel.add(button, BorderLayout.SOUTH);

        add(panel);
        setSize(400, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }

    public ArrayList fillArray(){
        europeanCountries = new ArrayList<>();
        ArrayList<String> countries = new ArrayList<>();

        europeanCountries.add("Albania");
        europeanCountries.add("Andorra");
        europeanCountries.add("Austria");
        europeanCountries.add("Belarus");
        europeanCountries.add("Belgium");
        europeanCountries.add("Bosnia and Herzegovina");
        europeanCountries.add("Bulgaria");
        europeanCountries.add("Croatia");
        europeanCountries.add("Cyprus");
        europeanCountries.add("Czech Republic");
        europeanCountries.add("Denmark");
        europeanCountries.add("Estonia");
        europeanCountries.add("Finland");
        europeanCountries.add("France");
        europeanCountries.add("Germany");
        europeanCountries.add("Greece");
        europeanCountries.add("Hungary");
        europeanCountries.add("Iceland");
        europeanCountries.add("Ireland");
        europeanCountries.add("Italy");
        europeanCountries.add("Kosovo");
        europeanCountries.add("Latvia");
        europeanCountries.add("Liechtenstein");
        europeanCountries.add("Lithuania");
        europeanCountries.add("Luxembourg");
        europeanCountries.add("Malta");
        europeanCountries.add("Moldova");
        europeanCountries.add("Monaco");
        europeanCountries.add("Montenegro");
        europeanCountries.add("Netherlands");
        europeanCountries.add("North Macedonia");
        europeanCountries.add("Norway");
        europeanCountries.add("Poland");
        europeanCountries.add("Portugal");
        europeanCountries.add("Romania");
        europeanCountries.add("Russia");
        europeanCountries.add("San Marino");
        europeanCountries.add("Serbia");
        europeanCountries.add("Slovakia");
        europeanCountries.add("Slovenia");
        europeanCountries.add("Spain");
        europeanCountries.add("Sweden");
        europeanCountries.add("Switzerland");
        europeanCountries.add("Turkey");
        europeanCountries.add("Ukraine");
        europeanCountries.add("United Kingdom");
        europeanCountries.add("Vatican City");

        for(int i = europeanCountries.size(); i > 0; i--){
            int num = rand.nextInt(i);
            europeanCountries.get(num);
            countries.add(europeanCountries.get(num));
            europeanCountries.remove(num);
        }
        return countries;
    }

    public static void main(String[] args) {
        new Main();
    }
}