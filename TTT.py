
board = list(range(1,10))

def draw_board(board):
   
   for i in range(3):
      print(board[0+i], " ", board[3+i], " ", board[6+i] )
      

def take_input(player):
   valid = False
   while not valid:
      player_answer = input("where you put X player " + player +"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("You should enter numbers only from 1 to 9")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player
            valid = True
         else:
            print("This cell is taken!")
      else:
        print("Wrong! Please enter number from 1 to 9")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "Wim!")
              win = True
              break
        if counter == 9:
            print("No winners here!")
            break
    draw_board(board)
main(board)

input("Press any key to exit!")
