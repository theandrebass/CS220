import java.util.*;

public class tromino {
	
	private int[][] grid;
	private int currentNum;
	
	// Pre-condition: size must be a perfect power of 2 and 0<=x<size, 0<=y<size
	// Post-condition: creates an empty tromino object with dimensions size x size.
	public tromino(int size, int x, int y) {
		
		int actualsize = 1;
		while (actualsize < size) actualsize*=2;
		
		// Make sure the grid size is a perfect power of 2.
		grid = new int[actualsize][actualsize];
		currentNum = 1;
		
		// Fill in the grid with all empty squares.
		for (int i=0; i<actualsize; i++) {
			for (int j=0; j<actualsize; j++) {
				grid[i][j] = 0;
			}
		}
		
		// This represents the original hole in the tromino.
		grid[x][y] = -1;
	}
	
	// Wrapper call for recursive method.
	public void tile() {
		tileRec(grid.length, 0, 0);
	}
	
	private void tileRec(int size, int topx, int topy) {
		
		// No recursive case needed here, just fill in your one tromino...
		if (size == 2) {
		
			// Fill in the one necessary tromino. The hole is identified by a
			// non-zero number, so don't fill in that one square.	
			for (int i=0; i<size; i++) 
				for (int j=0; j<size; j++)
					if (grid[topx+i][topy+j] == 0)
						grid[topx+i][topy+j] = currentNum;
		
			// Advance to the next tromino.
			currentNum++;
		}
		
		// Recursive case...
		else {
			
			// Find coordinates of missing hole
			int savex=topx, savey=topy;
			
			for (int x=topx; x<topx+size; x++) 
				for (int y=topy; y<topy+size; y++)
					if (grid[x][y] != 0) {
						savex = x;
						savey = y;
					}
				
			// Hole in upper left quadrant.		
			if (savex < topx + size/2 && savey < topy + size/2) {
				
				// Recursively tile upper left quadrant.
				tileRec(size/2, topx, topy);
				
				// Fill in middle tromino
				grid[topx+size/2][topy+size/2-1] = currentNum;
				grid[topx+size/2][topy+size/2] = currentNum;
				grid[topx+size/2-1][topy+size/2] = currentNum;
				
				// Advance to the next tromino
				currentNum++;
				
				// Now we can make our three other recursive calls.
				tileRec(size/2, topx, topy+size/2);
				tileRec(size/2, topx+size/2, topy);
				tileRec(size/2, topx+size/2, topy+size/2);
				
			}
			
			// Hole in upper right quadrant
			else if (savex < topx + size/2 && savey >= topy + size/2) {
				
				// Recursively tile upper right quadrant.
				tileRec(size/2, topx, topy+size/2);
				
				// Fill in middle tromino
				grid[topx+size/2][topy+size/2-1] = currentNum;
				grid[topx+size/2][topy+size/2] = currentNum;
				grid[topx+size/2-1][topy+size/2-1] = currentNum;
				
				// Advance to the next tromino
				currentNum++;
				
				// Now we can make our three other recursive calls.
				tileRec(size/2, topx, topy);
				tileRec(size/2, topx+size/2, topy);
				tileRec(size/2, topx+size/2, topy+size/2);
				
			}
			
			// Hole in bottom left quadrant
			else if (savex >= topx + size/2 && savey < topy + size/2) {
				
				// Recursively tile bottom left quadrant.
				tileRec(size/2, topx+size/2, topy);
				
				// Fill in middle tromino
				grid[topx+size/2-1][topy+size/2] = currentNum;
				grid[topx+size/2][topy+size/2] = currentNum;
				grid[topx+size/2-1][topy+size/2-1] = currentNum;
				
				// Advance to the next tromino
				currentNum++;
				
				// Now we can make our three other recursive calls.
				tileRec(size/2, topx, topy);
				tileRec(size/2, topx, topy+size/2);
				tileRec(size/2, topx+size/2, topy+size/2);
			}
			else {
				
				// Recursively tile bottom right quadrant.
				tileRec(size/2, topx+size/2, topy+size/2);
				
				// Fill in middle tromino
				grid[topx+size/2-1][topy+size/2] = currentNum;
				grid[topx+size/2][topy+size/2-1] = currentNum;
				grid[topx+size/2-1][topy+size/2-1] = currentNum;
				
				// Advance to the next tromino
				currentNum++;
				
				// Now we can make our three other recursive calls.
				tileRec(size/2, topx+size/2, topy);
				tileRec(size/2, topx, topy+size/2);
				tileRec(size/2, topx, topy);
			}
			
		} // end large if-else
		
	} // end tileRec
	
	
	// Prints out the current object.
	public void print() {
		
		for (int i=0; i<grid.length; i++) {
			for (int j=0; j<grid[i].length; j++)
				System.out.print(grid[i][j] + "\t");
			System.out.println();
		}
	}
	
	public static void main(String[] args) {
		
		Scanner stdin = new Scanner(System.in);
		
		// Get user input...
		System.out.println("How big do you want your Tromino grid?");
		System.out.println("Please enter a perfect power of 2.");
		int size = stdin.nextInt();
		
		System.out.println("Where do you want the hole?");
		System.out.println("Answer with an x and y coordinate separated by spaces.");
		int x = stdin.nextInt();
		int y = stdin.nextInt();
		
		// Create our object and tile it!
		tromino thisguy = new tromino(size, x, y);
		thisguy.tile();
		
		// Print out the trominoed grid.
		System.out.println("Here's your final grid:\n");
		thisguy.print();
		
	}
}
