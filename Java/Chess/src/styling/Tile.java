package styling;
import pieces.*;
import javax.swing.*;
import java.awt.*;

public class Tile extends Panel {
    private boolean isOccupied;
    private Piece piece;

    public Tile(boolean isWhite) {
        setColor(isWhite);
        this.isOccupied = false;
        this.piece = null;
    }

    public void setPiece(Piece piece) {
        this.piece = piece;
        this.add(new JLabel(new ImageIcon("../Images/BlackPawn.png")));
        this.isOccupied = true;
    }

    public void removePiece() {
        this.piece = null;
        this.isOccupied = false;
    }

    public boolean isOccupied() {
        return this.isOccupied;
    }

    public Piece getPiece() {
        return this.piece;
    }
    public void setColor(boolean white){
        if(white){
            this.setBackground(Color.WHITE);
        }else{
            this.setBackground(Color.BLACK);
        }
    }
    public void highlight(){
        this.setBackground(Color.YELLOW);
    }
}
