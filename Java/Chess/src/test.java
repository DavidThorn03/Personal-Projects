import javax.swing.*;
import java.awt.*;

public class test extends JFrame {
    public test (){
        JPanel mainPanel = new JPanel();
        Icon image = new ImageIcon("Images/free-images.jpg");
        JLabel label = new JLabel();
        label.setIcon(image);
        mainPanel.add(label);
        add(mainPanel);
        setSize(600, 600);
        setVisible(true);
    }
}
