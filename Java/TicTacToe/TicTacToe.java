import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class TicTacToe extends JFrame implements MouseListener{
    JPanel mainPanel = new JPanel();
    JPanel panels [] = new JPanel[9];
    JLabel labels[] = new JLabel[9];

    Icon blankIcon = new ImageIcon("blank.png");
    Icon xIcon = new ImageIcon("x.png");
    Icon oIcon = new ImageIcon("o.png");

    boolean xTurn = true;
    int turnCount = 9;

    public TicTacToe(){
        super("Tic Tac Toe");
        mainPanel.setLayout(new GridLayout(3,3));

        for(int i = 0; i < 9; i++){
            panels[i] = new JPanel();
            labels[i] = new JLabel(blankIcon);
            panels[i].add(labels[i]);
            labels[i].addMouseListener(this);
            mainPanel.add(panels[i]);
        }

        add(mainPanel);
        setSize(600, 600);
        setVisible(true);
    }

    public void mouseClicked(MouseEvent e){
        for(int i = 0; i < 9; i++){
            if(e.getSource() == labels[i] && labels[i].getIcon() == blankIcon){
                turnCount--;
                if(xTurn){
                    labels[i].setIcon(xIcon);
                    checkWin(xIcon);
                    xTurn = false;
                }
                else{
                    labels[i].setIcon(oIcon);
                    checkWin(oIcon);
                    xTurn = true;
                }
            }
        }
    }

    public void checkWin(Icon Icon){
        String winMessage = "";
        if(xTurn){
            winMessage = "X wins!";
        }
        else{
            winMessage = "O wins!";
        }
        //horizontal
        for(int i = 0; i < 3; i++){
            if(labels[(i * 3)].getIcon() == Icon && labels[1 + (i*3)].getIcon() == Icon && labels[2 + (i*3)].getIcon() == Icon) {
                JOptionPane.showMessageDialog(null, winMessage);
                resetBoard();
            }
        }
        //vertical
        for(int i = 0; i < 3; i++){
            if(labels[i].getIcon() == Icon && labels[i + 3].getIcon() == Icon && labels[i + 6].getIcon() == Icon) {
                JOptionPane.showMessageDialog(null, winMessage);
                resetBoard();
            }
        }
        //diagonal
        if(labels[0].getIcon() == Icon && labels[4].getIcon() == Icon && labels[8].getIcon() == Icon) {
            JOptionPane.showMessageDialog(null, winMessage);
            resetBoard();
        }
        if(labels[2].getIcon() == Icon && labels[4].getIcon() == Icon && labels[6].getIcon() == Icon) {
            JOptionPane.showMessageDialog(null, winMessage);
            resetBoard();
        }
        if(turnCount == 0){
            JOptionPane.showMessageDialog(null, "It's a draw!");
            resetBoard();
        }
    }

    public void resetBoard(){
        for(int i = 0; i < 9; i++){
            labels[i].setIcon(blankIcon);
        }
        this.turnCount = 9;
    }

    public void mousePressed(MouseEvent e){}
    public void mouseReleased(MouseEvent e){}
    public void mouseEntered(MouseEvent e){}
    public void mouseExited(MouseEvent e){}
    public static void main(String[] args){
        TicTacToe t = new TicTacToe();
        t.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}