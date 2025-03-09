package pieces;
import javax.swing.ImageIcon;

public abstract class Piece {
    private boolean isWhite;
    private TYPE type;
    private ImageIcon icon;
    public Piece(boolean isWhite, TYPE type, ImageIcon icon){
        this.isWhite = isWhite;
    }
    public boolean isWhite(){
        return this.isWhite;
    }
    public TYPE getType(){
        return this.type;
    }
    public ImageIcon getIcon(){
        return this.icon;
    }
    public abstract boolean Move(int x, int y, int newX, int newY);
    public abstract boolean Capture(int x, int y, int newX, int newY);
    public abstract boolean validMoves(int x, int y, int newX, int newY);
}
