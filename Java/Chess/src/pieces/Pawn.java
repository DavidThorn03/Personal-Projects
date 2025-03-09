package pieces;

import javax.swing.*;

public class Pawn extends Piece{
    public Pawn(boolean isWhite){
        super(isWhite, TYPE.PAWN, new ImageIcon("Images/BlackPawn.png"));
    }
    public boolean Move(int x, int y, int newX, int newY){
        if(this.isWhite()){
            if(newX == x && newY == y + 1){
                return true;
            }
        }else{
            if(newX == x && newY == y - 1){
                return true;
            }
        }
        return false;
    }
    public boolean Capture(int x, int y, int newX, int newY){
        if(this.isWhite()){
            if(newX == x + 1 && (newY == y + 1 || newY == y - 1)){
                return true;
            }
        }else{
            if(newX == x - 1 && (newY == y + 1 || newY == y - 1)){
                return true;
            }
        }
        return false;
    }
    public boolean validMoves(int x, int y, int newX, int newY){
        if(this.isWhite()){
            if(newX == x && newY == y + 1){
            }
        }else{
            if(newX == x && newY == y - 1){
                return true;
            }
        }
        return false;
    }
}
