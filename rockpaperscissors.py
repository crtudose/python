from random import choice

class Game():

    # r = rock, p = paper, s = scissors
    OUTCOMES = {('s', 's'): 0, ('p', 'p'): 0, ('r', 'r'): 0, # tie
                ('r', 'p'): -1, ('p', 's'): -1, ('s', 'r'): -1, # human player loses
                ('p', 'r'): 1, ('s', 'p'): 1, ('r', 's'): 1} # human player wins

    def __init__(self, num_rounds):
        self.num_rounds = num_rounds
        self.human_player = HumanPlayer()
        self.comp_player = ComputerPlayer()

    def play(self):
        for i in range(self.num_rounds):
            self.play_round()
        self.summarise_score()
    
    def play_round(self):
        human_choice = self.human_player.choose()
        comp_choice = self.comp_player.choose()
        print('You:', human_choice, ' | Computer:', comp_choice)
        self.settle_round(human_choice, comp_choice)
    
    def settle_round(self, human_choice, comp_choice):
        outcome = self.OUTCOMES[(human_choice, comp_choice)]
        if outcome == 1:
            print('You won this round!\n')
            self.human_player.score += 1
        elif outcome == -1:
            print('You lost this round!\n')
            self.comp_player.score += 1
        else:
            print('This round is a tie\n')
    
    def summarise_score(self):
        print('[Game summary] Your points:', self.human_player.score, ' | Computer points:', self.comp_player.score)
        if self.human_player.score > self.comp_player.score:
            print ("You won.")
        elif self.human_player.score < self.comp_player.score:
            print ("Computer won.")
        else:
            print ("It was a tie.")
        
class Player():
    def __init__(self):
        self.score = 0
            
class HumanPlayer(Player):
    def choose(self):
        while True:
            user_choice = input('Rock, paper or scissors [r/p/s]? ')
            if user_choice in ['r', 'p', 's']:
                return user_choice

class ComputerPlayer(Player):
    def choose(self):
        return choice(['r', 'p', 's'])

if __name__ == '__main__':
    print('--- Rock Paper Scissors Game ---')
    while True:
        round_count = input('How many rounds would you like to play? ')
        if round_count.isnumeric():
            Game(int(round_count)).play()
            break

'''
Game Class:
This class represents a simple Rock-Paper-Scissors game.
Key Components:
OUTCOMES: A dictionary that maps tuples of player choices to outcomes (win, lose, or tie).
__init__(self, num_rounds): Initializes the game with a specified number of rounds.
play(self): Plays the game for the specified number of rounds.
play_round(self): Plays a single round.
settle_round(self, human_choice, comp_choice): Determines the outcome of a round.
summarise_score(self): Prints the final game summary.
Note:
The game assumes that the human player’s input is either ‘r’ (rock), ‘p’ (paper), or ‘s’ (scissors).
The outcome of each round is determined based on the predefined rules in the OUTCOMES dictionary.
    
Player Class:
Base class for both human and computer players.
Contains an attribute score to keep track of points.
    
HumanPlayer Class:
Inherits from Player.
Represents the human player.
Method choose(self): Asks the user for their choice (rock, paper, or scissors).
The loop ensures that the user’s input is valid.
    
ComputerPlayer Class:
Inherits from Player.
Represents the computer opponent.
Method choose(self): Generates a random choice (rock, paper, or scissors).
    
Game Flow:
The game starts by creating an instance of the Game class with a specified number of rounds.
For each round, the human player and computer player make their choices.
The outcome of the round is determined using the OUTCOMES dictionary.
The game continues until all rounds are played.
Finally, the game summary (including points and winner) is displayed.
Overall, this code snippet provides a basic implementation of the Rock-Paper-Scissors game, allowing a human player to compete against the computer. The outcome of each round is based on the predefined rules, and the winner is determined after all rounds are completed.
'''
