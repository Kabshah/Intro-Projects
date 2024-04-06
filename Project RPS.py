from random import randint

# Available moves
moves = ["rock", "paper", "scissors"]

# Function to record the score in a file
def record_score(player_wins, computer_wins, is_tie=False):
    try:
        with open("score.txt", "a") as file:
            # Check if it's a tie game
            if is_tie:
                # Write a message for tie games in txt file
                file.write("Game " + str(games_played) + " It's a tie!\n")
            else:
                # Write scores for non-tie games in txt file
                file.write("Game " + str(games_played) + " Computer:" + str(computer_wins) + ", User:" + str(player_wins) + "\n")
    except FileExistsError:
        # If the file already exists, open it and append the score
        with open("score.txt", "a") as file:
            # Check if it's a tie game
            if is_tie:
                # Write a message for tie game in txt file
                file.write("Game " + str(games_played) + " It's a tie!\n")
            else:
                # Write scores for non-tie games in txt file
                file.write("Game " + str(games_played) + " Computer:" + str(computer_wins) + ", User:" + str(player_wins) + "\n")

# Initializing the game counter
games_played = 0

while True:
    # Incrementing the game counter
    games_played += 1
    
    # Computer selects a moves randomly
    computer = moves[randint(0, 2)]
    
    # Player inputs their move and remove whitespaces if any
    player_move = input("Enter Rock, Paper, or Scissors (or 'exit' to quit): ").strip().lower()
    
    # Checking user inputs
    
    if player_move == 'exit':
        # If user decides to exit game print a message on console
        print("Thanks for playing!")
        break
    
    elif player_move not in moves:
        # If user's input is not a valid move, prompt them to enter a valid one
        print("Invalid move. Please enter Rock, Paper, or Scissors.")
    else:
        # Displaying the moves of both players on console
        print("Your move: ", player_move.title())
        print("Computer's move:", computer.title())
        
        # Game result
        if player_move == computer:
            # If it's a tie
            print("It's a tie!")
            record_score(0, 0, is_tie=True)  # Record tie game
            
            # game logic based on the rules of RPS
        elif (player_move == "rock" and computer == "scissors") or \
             (player_move == "paper" and computer == "rock") or \
             (player_move == "scissors" and computer == "paper"):
            # If the player wins print a message
            print("You win!", player_move.title(), "beats", computer.title(),".")
            record_score(1, 0)  # Record player win
        else:
            # If the computer wins
            print("Computer wins!", computer.title(), "beats", player_move.title(), ".")
            record_score(0, 1)  # Record computer win