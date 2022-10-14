import random

from bke import MLAgent, is_winner, opponent, RandomAgent, train_and_plot, EvaluationAgent, start, train, save


class MyRandomAgent(EvaluationAgent):

    def evaluate(self, board, my_symbol, opponent_symbol):
        return random.randint(1, 500)


class MyAgent(MLAgent):

    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
        my_agent = MyAgent()
       


def TrainenEnPlotten():
  random.seed(1)

  my_agent = MyAgent()
  random_agent = RandomAgent()


  train_and_plot(agent=my_agent,
                 validation_agent=random_agent,
                 iterations=50,
                 trainings=100,
                 validations=1000)


def print_menu():  
    print(30 * "-", "MENU", 30 * "-")
    print("1. Player vs Player")
    print("2. Player vs Noob bot")
    print("3. Bot trainen")
    print("4. Player vs Smart bot")
    print("5. validatie grafieken plotten")
    print(67 * "-")


loop = True

while loop:  
    print_menu()  
    choice = int(input("Enter your choice [1-5]: "))

    if choice == 1:
        print("Player vs Player has been selected")
        start()
    elif choice == 2:
        print("Player vs Noob bot has been selected")
        my_random_agent = MyRandomAgent()
        start(player_o=my_random_agent, player_x=my_random_agent)
    elif choice == 3:
        print("Bot trainen has been selected")
        my_agent = MyAgent()
        train(my_agent, 3000)
 
        save(my_agent, 'MyAgent_3000')
    elif choice == 4:
        print("Player vs Smart bot has been selected")
        start(player_o= 'MyAgent_3000')
    elif choice == 5:
        print("validatie grafieken plotten has been selected")
        TrainenEnPlotten()
    else:
        
        print("Wrong option selection. Enter any key to try again..")

random.seed(1)

my_agent = MyAgent()
random_agent = RandomAgent()

