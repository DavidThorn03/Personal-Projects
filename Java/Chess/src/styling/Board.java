package styling;
import pieces.Piece;
import javax.swing.*;
import java.awt.*;

public class Board extends JFrame{
    private Tile[][] board;
    private boolean isWhite;
    private JPanel mainPanel = new JPanel();
    public Board(){
        super("Chess");
        this.mainPanel.setLayout(new GridLayout(8,8));
        this.board = new Tile[8][8];

        this.isWhite = true;

        for(int i = 0; i < 8; i++){
            for(int j = 0; j < 8; j++){
                this.board[i][j] = new Tile(this.isWhite);
                this.isWhite = !this.isWhite;
            }
            this.isWhite = !this.isWhite;
        }
        this.board[0][1].setBackground(null);

        this.board[0][1].setPiece(new pieces.Pawn(true));

        for(int i = 0; i < 8; i++){
            for(int j = 0; j < 8; j++){
                this.mainPanel.add(this.board[i][j]);
            }
        }
        add(this.mainPanel);
        setSize(600, 600);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public void setPiece(int x, int y, Piece piece){
        this.board[x][y].setPiece(piece);
    }

    public void removePiece(int x, int y){
        this.board[x][y].removePiece();
    }

    public boolean isOccupied(int x, int y){
        return this.board[x][y].isOccupied();
    }

    public Piece getPiece(int x, int y){
        return this.board[x][y].getPiece();
    }
}
