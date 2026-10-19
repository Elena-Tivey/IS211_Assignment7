import random
import argparse

random.seed(0)

class Player:
    """Represent a player in the Pig game."""

    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_points(self, points):
        """Add points to the player's total score."""
        self.score += points

    def reset_score(self):
        """Reset the player's score for a new game."""
        self.score = 0

class Die:
    """Represent a six-sided die."""

    def roll(self):
        """Return a random number from 1 to 6."""
        return random.randint(1, 6)

class PigGame:
    """Manage the Pig game for multiple human players."""

    def __init__(self, num_players):
        self.num_players = num_players
        self.players = []

        # Create the requested number of players.
        for number in range(1, num_players + 1):
            player = Player(f"Player {number}")
            self.players.append(player)

        self.die = Die()
        self.current_player_index = 0
        self.winning_score = 100

    def switch_player(self):
        """Move to the next player."""
        self.current_player_index = (
            self.current_player_index + 1
        ) % self.num_players

    def reset_game(self):
        """Reset all scores and game state for a new game."""
        for player in self.players:
            player.reset_score()

        self.current_player_index = 0

    def play(self):
        """Play until one player reaches 100 points."""

        print("\nWelcome to the Pig Game!")
        print(f"Number of players: {self.num_players}")
        print("The first player to reach 100 points wins.")
        print("Enter 'r' to roll or 'h' to hold.")

        while True:
            player = self.players[self.current_player_index]
            turn_total = 0

            print(f"\n--- {player.name}'s turn ---")

            while True:
                # Display the current scores before the decision.
                print(f"Current score for this turn so far: {turn_total} "
                      f"| Total game score: {player.score}")

                decision = input(
                    "\nRoll or hold? (r/h): "
                ).lower().strip()

                if decision == "r":
                    roll = self.die.roll()
                    print(f"{player.name} rolled: {roll}")

                    if roll == 1:
                        print("You rolled a 1! Your turn total is lost.")
                        print(f"Your score remains {player.score}.")
                        break

                    turn_total += roll

                elif decision == "h":
                    player.add_points(turn_total)

                    print(f"{player.name} holds.")
                    print(f"Points earned this turn: {turn_total} | New total game score: {player.score}")

                    break

                else:
                    print("Invalid choice. Please enter 'r' or 'h'.")

            # Check whether the current player has won.
            if player.score >= self.winning_score:
                print("\nGame over!")
                print(f"{player.name} wins!")
                print(f"Final score: {player.score}")

                # Display every player's final score.
                print("\nFinal scores:")
                for current_player in self.players:
                    print(
                        f"{current_player.name}: "
                        f"{current_player.score}"
                    )

                return

            self.switch_player()

def main():
    """Read command-line arguments and manage multiple games."""

    parser = argparse.ArgumentParser(
        description="Play the Pig dice game."
    )

    parser.add_argument(
        "--numPlayers",
        type=int,
        default=2,
        help="Number of players (default: 2)"
    )

    args = parser.parse_args()

    if args.numPlayers < 2:
        parser.error("--numPlayers must be at least 2.")

    # Create the game with the requested number of players.
    game = PigGame(args.numPlayers)

    while True:
        game.play()

        # Ask whether the players want to start another game.
        while True:
            answer = input(
                "\nWould you like to play another game? (y/n): "
            ).lower().strip()

            if answer == "y":
                game.reset_game()
                print("\nStarting a new game. All scores are reset.")
                break

            elif answer == "n":
                print("Thanks for playing Pig!")
                return

            else:
                print("Invalid choice. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
    
