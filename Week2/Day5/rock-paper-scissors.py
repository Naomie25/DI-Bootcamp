from game import Game

def get_user_menu_choice():
     print("\nMenu:")
     print("1. Play a new game")
     print("2. Show scores")
     print("3. Quit")
     
     valid_choices = {'1': 'Play a new game', '2': 'Show scores', '3': 'Quit'}

     while True:
        choice = input("Choose an option (1/2/3): ").strip()
        if choice in valid_choices:
            return valid_choices[choice]
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def print_results(results):
    print("\nGame Results:")
    for key, value in results.items():
        print(f"{key.capitalize()}: {value}")
    print("Thank you for playing!")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == "Play a new game":
            game = Game()
            result = game.play()  # should return "win", "loss", or "draw"
            if result in results:
                results[result] += 1

        elif choice == "Show scores":
            print_results(results)

        elif choice == "Quit":
            print_results(results)
            break


if __name__ == "__main__":
    main()
    