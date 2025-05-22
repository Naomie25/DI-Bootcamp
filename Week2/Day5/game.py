import random
class Game:
    def __init__(self):
        pass
    def get_user_item(self):
        item= input("Select an item (rock/paper/scissors)").lower().strip()
        return item
    
    def get_computer_item(self):
        options = ['rock', 'paper', 'scissors']
        return random.choice(options)
    

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (
            (user_item == "rock" and computer_item == "scissors") or
            (user_item == "scissors" and computer_item == "paper") or
            (user_item == "paper" and computer_item == "rock")
        ):
            return "win"
        else:
            return "loss"
        
    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result=self.get_game_result(user_item, computer_item)
        print(f"User's item: {user_item}, Computer's item: {computer_item} and the result is: {result}")
        return result


