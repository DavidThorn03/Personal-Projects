import javax.swing.*;
import java.awt.*;
import java.awt.event.*;


public class gui extends JFrame implements ActionListener{
    public JButton hexToBin = new JButton("Hexidemical to Binary");
    public JButton hexToDec = new JButton("Hexidemical to Decimal");
    public JButton binToHex = new JButton("Binary to Hexidemical");
    public JButton binToDec = new JButton("Binary to Decimal");
    public JButton decToHex = new JButton("Decimal to Hexidemical");
    public JButton decToBin = new JButton("Decimal to Binary");

    public JTextField input = new JTextField(10);
    public JTextField output = new JTextField(10);

    public gui(){
        super("Number Converter");
        JPanel buttonPanel = new JPanel(new GridLayout(2, 3, 10, 10));

        hexToBin.addActionListener(this);
        hexToDec.addActionListener(this);
        binToHex.addActionListener(this);
        binToDec.addActionListener(this);
        decToHex.addActionListener(this);
        decToBin.addActionListener(this);

        buttonPanel.add(hexToBin);
        buttonPanel.add(hexToDec);
        buttonPanel.add(binToHex);
        buttonPanel.add(binToDec);
        buttonPanel.add(decToHex);
        buttonPanel.add(decToBin);

        getContentPane().add(buttonPanel);

        setSize(600, 500);
        setVisible(true);
    }//end of gui

    public void actionPerformed(ActionEvent e){
        
    }//end of action performed
}//end of class gui
