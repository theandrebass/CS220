#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
int global=0;
void tromino(int board_size,int x_missing,int y_missin,int x_board, int y_board,int size, int (*array)[size]);
int getRandomNumber(int minimum, int maximum){ // generating the random number
	int i;
	i = rand()%(maximum-minimum)+minimum;
	return i;
}
void printMatrix(int coloumn, int (*ptr_arr)[coloumn]){ // printing the matrix
	int i,j; 
	
	for (i = 0; i < coloumn; ++i)
	{
		for ( j = 0; j < coloumn; ++j)
			{	
				if(ptr_arr[i][j]==(-1)){
					printf("X\t");
				}else{
					printf("%d\t",ptr_arr[i][j]);
				}
				
			}
		printf("\n");		
	}
	printf("\n");
}
int main(int argc, char *args[]){
	srand( (unsigned)time( NULL ) );
	if(atoi(args[1])<1){ // checking the size of tromino board, board size less than 2*2 is not valid
		printf("Tromino doesn't support board less than 2*2 \n");
	}else{
		int board_size=pow(2,atoi(args[1]));

		int i,j,x,y;
		global=0;
	  	x=getRandomNumber(0,board_size); 
	  	y=getRandomNumber(0,board_size);
	
		int array[board_size][board_size];
		for ( i = 0; i < board_size; ++i){

			for ( j = 0; j < board_size; ++j){
				array[i][j]=0;
			}
		}
		array[x][y]=-1; // adding the random hole into the matrix
		//printMatrix(board_size,array);
		tromino(board_size,x,y,0,0,board_size,array); // calling the tromino function
		printMatrix(board_size,array); 
	}
	

	return 0;
}

void tromino(int board_size,int x_missing,int y_missing,int x_board, int y_board,int size, int (*array)[size]){ // tromino implemenation
	//printf("Board Size %d, missing (%d,%d) board (%d,%d)\n",board_size,x_missing,y_missing,x_board,y_board);
	if(board_size==2){
		global++;
		int i,j;
		//printf("Missing (%d,%d) and board (%d,%d)\n",x_missing,y_missing,x_board,y_board);
		for ( i = x_board; i < (x_board+board_size); ++i)
		{
			for ( j = y_board; j< (y_board+board_size); ++j)
			{
				if(!(i==x_missing && j==y_missing)){
					array[i][j]=global;
				}
			}
		}
		return;

	}
	global++;
	int half_size=board_size/2,x_center,y_center;
	int x_upper_right,y_upper_right,  x_upper_left,y_upper_left, x_lower_right,y_lower_right,  x_lower_left,y_lower_left;
	x_center=x_board+half_size;
	y_center=y_board+half_size;
	
	if(x_missing<x_center && y_missing< y_center){ // checking that hole in the first quad, if yes than put tromino in center opposite quad.
		//printf("First qua\n");
		array[x_center-1][y_center]=array[x_center][y_center-1]=array[x_center][y_center]=global;
		
		x_upper_left=x_missing;y_upper_left=y_missing;

		x_upper_right=x_center-1; y_upper_right=y_center;

		x_lower_left=x_center; y_lower_left=y_center-1;

		x_lower_right=x_center; y_lower_right=y_center;

	}else if(x_missing<x_center && y_missing>=y_center){ // checking that hole in the second quad, if yes than put tromino in center opposite quad.
		//printf("Second qua\n");
		array[x_center-1][y_center-1]=array[x_center][y_center-1]=array[x_center][y_center]=global;

		x_upper_left=x_center-1; y_upper_left=y_center-1;

		x_upper_right=x_missing; y_upper_right=y_missing;

		x_lower_left=x_center; y_lower_left= y_center-1;

		x_lower_right = x_center ; y_lower_right = y_center;


	}else if(x_missing>=x_center && y_missing<y_center){ // checking that hole in the third quad, if yes than put tromino in center opposite quad.
		//printf("Third Qua\n");
		array[x_center-1][y_center-1]=array[x_center-1][y_center]=array[x_center][y_center]=global;

		x_upper_left=x_center-1;y_upper_left=y_center-1;

		x_upper_right=x_center-1; y_upper_right=y_center;

		x_lower_left=x_missing; y_lower_left=y_missing;

		x_lower_right=x_center; y_lower_right=y_center;


	}else if(x_missing>=x_center && y_missing>=y_center){ // checking that hole in the fourth quad, if yes than put tromino in center opposite quad.
		//printf("Fourth Qua\n");
		array[x_center-1][y_center-1]=array[x_center-1][y_center]=array[x_center][y_center-1]=global;

		x_upper_left=x_center-1;y_upper_left=y_center-1;

		x_upper_right=x_center-1; y_upper_right=y_center;

		x_lower_left=x_center; y_lower_left=y_center-1;

		x_lower_right=x_missing; y_lower_right=y_missing;

	}

	//printf("Rec-1 size: %d hole(%d,%d), board(%d,%d)\n",half_size,x_upper_left,y_upper_left,x_board,y_board);
	//printMatrix(size,array);
	tromino(half_size,x_upper_left, y_upper_left, x_board,y_board       ,size,array); // recursive call to the first qua

	//printf("Rec-2 size: %d hole(%d,%d), board(%d,%d)\n",half_size,x_upper_right,y_upper_right,x_board,y_board+half_size);
	//printMatrix(size,array);
	tromino(half_size,x_upper_right, y_upper_right, x_board,y_board+half_size       ,size,array); // recursive call to the second qua

	//printf("Rec-3 size: %d hole(%d,%d), board(%d,%d)\n",half_size,x_lower_left,y_lower_left,x_board+half_size,y_board);
	//printMatrix(size,array);
	tromino(half_size,x_lower_left, y_lower_left, x_board+half_size,y_board      ,size,array); // recursive call to the third qua

	//printf("Rec-4 size: %d hole(%d,%d), board(%d,%d)\n",half_size,x_lower_right,y_lower_right,x_board+half_size,y_board+half_size);
	//printMatrix(size,array);
	tromino(half_size,x_lower_right, y_lower_right, x_board+half_size,y_board+half_size     ,size,array); // recursive call to the fourth qua

}
