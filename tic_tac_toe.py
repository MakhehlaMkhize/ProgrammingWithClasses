def main():
    
    play_game = True
    players_turn= [1, 2, 3, 4, 5, 6, 7, 8, 9] 
    board_numbering = board_numbers()
 
    while play_game:
        print("Tic-Tac-Toe is a game in which two players seek in alternate turns to \ncomplete a row, a column, or a diagonal with either three x's or three o's \ndrawn in the spaces of a grid of nine squares.")    
        for i in players_turn:
            if i== 1 or i==3 or i==5 or i==7 or i==9:
                while ValueError or IndexError:
                    try:
                        print(f"\n{board(board_numbering)}") 
                        userInput1=int(input("\nX's turn to choose a square (1-9):"))
                        board_numbering[userInput1-1]= "X"
                    except ValueError:
                        print("Incorrect value input. Enter a number between (1-9)")
                    except IndexError:
                        print("Incorrect value input. Enter a number between (1-9)")
                    else:
                        break        
            elif i==2 or i==4 or i==6 or i==8:
                while ValueError or IndexError:
                    try:
                        print(board(board_numbering)) 
                        userInput2=int(input("\nO's turn to choose a square (1-9):"))
                        board_numbering[userInput2-1]="O" 
                    except ValueError:
                        print("Incorrect value input. Enter a number between (1-9)")
                    except IndexError:
                        print("Incorrect value input. Enter a number between (1-9)")
                    else:
                        break

            if player_x_wins(board_numbering)==True:
                print(board(board_numbering)) 
                print("Player X wins. Good game!")
                play_again= input("Would you like to play again (Y/N)? ")
                if play_again=="Y" or play_again=="y":
                    board_numbering= board_numbers()
                    play_game
                elif play_again=="n" or play_again=="N":
                    print("See you next time.")
                    play_game = False
                    break
                

            elif player_o_wins(board_numbering)==True:
                print(board(board_numbering)) 
                print("Player O wins. Good game!")
                play_again= input("Would you like to play again (Y/N)? ")
                if play_again=="Y" or play_again=="y":
                    board_numbering= board_numbers()
                    play_game
                    
                elif play_again=="n" or play_again=="N":
                    print("See you next time.")
                    play_game = False
                    break
            
            elif board_numbering.count("X")== 5:
                print(board(board_numbering)) 
                print("\nDraw!. Good game!")
                play_again= input("Would you like to play again (Y/N)? ")
                if play_again=="Y" or play_again=="y":
                    board_numbering= board_numbers() 
                    play_game
                elif play_again=="n" or play_again=="N":
                    print("See you next time.")
                    play_game = False
                    break
                
def board_numbers():
    board_numbering=[]
    for i in range(1,10):
        board_numbering.append(i)
    return board_numbering
      
def board(board_numbering):

    return(f"{board_numbering[0]}|{board_numbering[1]}|{board_numbering[2]}\n-+-+-\n{board_numbering[3]}|{board_numbering[4]}|{board_numbering[5]}\n-+-+-\n{board_numbering[6]}|{board_numbering[7]}|{board_numbering[8]}")
    
def no_winner(board_numbering):
    if player_o_wins(board_numbering)==False and player_x_wins(board_numbering)==False:
        return True


def player_x_wins(board_numbering):
    if board_numbering[0]== "X" and board_numbering[1]== "X" and board_numbering[2]== "X":
        return True
    elif board_numbering[0]== "X" and board_numbering[3]== "X" and board_numbering[6]== "X":
        return True
    elif board_numbering[0]== "X" and board_numbering[4]== "X" and board_numbering[8]== "X":
        return True
    elif board_numbering[1]== "X" and board_numbering[4]== "X" and board_numbering[7]== "X":
        return True
    elif board_numbering[2]== "X"and board_numbering[4]== "X" and board_numbering[6]== "X":
        return True
    elif board_numbering[2]== "X"and board_numbering[5]== "X" and board_numbering[8]== "X":
        return True
    elif board_numbering[3]== "X" and board_numbering[4]== "X" and board_numbering[5]== "X":
        return True
    elif board_numbering[6]== "X" and board_numbering[7]== "X"  and board_numbering[8]== "X":
        return True
  
def player_o_wins(board_numbering):
    if board_numbering[0]== "O" and board_numbering[1]== "O" and board_numbering[2]== "O":
        return True
    elif board_numbering[0]== "O" and board_numbering[3]== "O" and board_numbering[6]== "O":
        return True
    elif board_numbering[0]== "O" and board_numbering[4]== "O" and board_numbering[8]== "O":
        return True
    elif board_numbering[1]== "O" and board_numbering[4]== "O" and board_numbering[7]== "O":
        return True
    elif board_numbering[2]== "O" and board_numbering[4]== "O" and board_numbering[6]== "O":
        return True
    elif board_numbering[2]== "O" and board_numbering[5]== "O" and board_numbering[8]== "O":
        return True
    elif board_numbering[3]== "O" and board_numbering[4]== "O" and board_numbering[5]== "O":
        return True
    elif board_numbering[6]== "O" and board_numbering[7]== "O" and board_numbering[8]== "O":
        return True

if __name__ == "__main__":
    main()