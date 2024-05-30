# The game will consist of a simple console-based interface where a human can play against the AI.
""" script's components:
1. A function to initialize the game state.
2. A function to display the current game state to the player.
3. The Minimax algorithm with Alpha-Beta pruning to decide the AI's moves.
4. A main game loop where the human and AI take turns."""

# Import the random module to generate random numbers for initializing the game state
import random


def initialize_game(n_piles=3):
    """
    Initialize the game with a specified number of piles, each with a random number of objects.

    :param n_piles: The number of piles to initialize
    :return: List representing the game state with a random number of objects in each pile
    """
    # Create a list representing the game state with a random number of objects (1 to 7) in each pile
    return [random.randint(1, 7) for _ in range(n_piles)]


def display_state(state):
    """
    Display the current state of the game.

    :param state: The current state of the game as a list of integers
    """
    # Print a visual representation of each pile along with the numeric count of objects
    print("\nCurrent game state:")
    for i, pile in enumerate(state, start=1):
        print(f"Pile {i}: {'*' * pile} ({pile})")


def minimax(state, alpha, beta, maximizingPlayer):
    """
    Implement the Minimax algorithm with Alpha-Beta pruning to evaluate game states.

    :param state: The current game state as a list
    :param alpha: The alpha value for pruning, representing the best already explored option for the maximizer
    :param beta: The beta value for pruning, representing the best already explored option for the minimizer
    :param maximizingPlayer: Boolean flag indicating if it's the maximizer's (AI's) turn
    :return: The value of the game state
    """
    # Check if the game has ended (i.e., all piles are empty)
    if sum(state) == 0:
        # The last player to move wins, so return positive value for maximizer, negative for minimizer
        return 1 if maximizingPlayer else -1

    # If it's the AI's turn (maximizing player)
    if maximizingPlayer:
        maxEval = float("-inf")  # Worst-case initialization for maximizer
        # Check all possible moves in each pile
        for i in range(len(state)):
            if state[i] > 0:  # There are objects to remove
                for remove in range(1, state[i] + 1):  # Iterate over all possible moves
                    newState = state.copy()  # Copy the state to simulate the move
                    newState[i] -= remove  # Execute the move
                    # Recurse to evaluate this move, swapping to minimizing player
                    eval = minimax(newState, alpha, beta, False)
                    # Update maxEval if this move is better than previous best
                    maxEval = max(maxEval, eval)
                    alpha = max(alpha, eval)  # Update alpha
                    if beta <= alpha:  # Prune the remaining branches
                        break
                if beta <= alpha:  # Break if we've already pruned
                    break
        return maxEval  # Return the best evaluation found
    else:
        # Similar process for the minimizing player (human)
        minEval = float("inf")  # Worst-case initialization for minimizer
        for i in range(len(state)):
            if state[i] > 0:
                for remove in range(1, state[i] + 1):
                    newState = state.copy()
                    newState[i] -= remove
                    eval = minimax(newState, alpha, beta, True)
                    minEval = min(minEval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
                if beta <= alpha:
                    break
        return minEval  # Return the worst evaluation found


def ai_move(state):
    """
    Determine the AI's move using the Minimax algorithm with Alpha-Beta pruning.

    :param state: The current game state as a list
    """
    bestEval = float("-inf")  # Initialize best evaluation for AI
    bestMove = None  # Initialize best move

    # Evaluate all possible moves for the AI
    for i in range(len(state)):
        if state[i] > 0:  # Check only non-empty piles
            for remove in range(1, state[i] + 1):
                newState = state.copy()
                newState[i] -= remove
                # Use minimax to evaluate this move
                eval = minimax(newState, float("-inf"), float("inf"), False)
                # If this move is better than previous best, update bestMove
                if eval > bestEval:
                    bestEval = eval
                    bestMove = (i, remove)

    # Perform the best move
    state[bestMove[0]] -= bestMove[1]
    # Inform the player which move the AI made
    print(f"AI removes {bestMove[1]} object(s) from pile {bestMove[0] + 1}.")


def player_move(state):
    """
    Allow the player to make a move by choosing a pile and the number of objects to remove.

    :param state: The current game state as a list
    """
    # Player input for choosing a pile
    pile = int(input("Choose a pile: ")) - 1
    # Validate pile choice
    remove = int(input("How many to remove from the pile: "))
    # Execute player's move
    state[pile] -= remove


def game_loop():
    """
    The main game loop where the human and AI take turns playing the game.
    """
    state = initialize_game()  # Initialize the game

    # Main game loop, continues until the game is over (all piles are empty)
    while sum(state) > 0:
        display_state(state)  # Display the current state of the game
        player_move(state)  # Player makes a move
        if sum(state) == 0:  # Check if game is over after player's move
            print("Player loses!")  # Player loses if they take the last object
            break
        ai_move(state)  # AI makes a move
        if sum(state) == 0:  # Check if game is over after AI's move
            print("AI loses!")  # AI loses if it takes the last object
            break


if __name__ == "__main__":
    game_loop()
    print("Game over!")  # Game ends when the loop breaks


""" Summary Conclusion:
    This script executes the Game of Nim, showcasing an interaction between a human player and an AI opponent. 
    The AI's decision-making process is governed by the Minimax algorithm with Alpha-Beta pruning. 
    The game is initialized with a variable number of piles, each randomly assigned a number of objects (from 1 to 7), 
    thus setting the stage for a diverse range of game scenarios. The Minimax algorithm is applied to determine the optimal move for 
    the AI by simulating all possible outcomes and choosing the move that maximizes the AI's chance of winning. Alpha-Beta pruning enhances this 
    process by eliminating paths that will not influence the final decision, thereby improving the efficiency of the algorithm.
    Throughout the game loop, the state of the game is displayed, and turns are alternated between the AI and the player, 
    each making strategic decisions based on the current state. The game concludes when all objects have been removed, 
    demonstrating the effectiveness of the AI's strategic capabilities in this traditional strategic challenge. 
"""

""" Detailed Conclusion:
    Conclusion and Detailed Overview:
    This Python script encapsulates a complete implementation of the Game of Nim, a timeless strategic game. 
    The gameplay unfolds in a console-based interface, where a human player is pitted against an artificial intelligence (AI) opponent, 
    demonstrating the intricacies of strategic decision-making. 

    The initialization of the game creates a random and dynamic starting point for each match, 
    with a varying number of piles (n_piles) and a random distribution of objects within each pile. 
    This randomness ensures that no two games are the same, requiring the AI to evaluate the best course of action in each new scenario.

    As the game progresses, the current state is displayed to the players in a clear and understandable format, 
    indicating the number of objects remaining in each pile using both numeric and visual representations. 
    This allows players to make informed decisions based on the current layout of objects.

    The crux of the AI's decision-making process lies in the Minimax algorithm with Alpha-Beta pruning. 
    The Minimax algorithm is a recursive search strategy that explores possible moves and their consequences deep into the future rounds of the game. 
    It operates under the principle of minimizing the possible loss for a worst-case scenario, assuming the opponent is playing optimally. 
    To achieve victory, the AI calculates the value of each possible move, considering the likelihood of winning or losing in the resulting game state. 
    This decision is made under the guiding principle of either maximizing its chance of victory (when it is the AI's turn) 
    or minimizing the potential success of the human player (when it is the player's turn).

    Alpha-Beta pruning optimizes this process by cutting off branches in the search tree that cannot possibly influence the final decision. 
    This pruning occurs when it is determined that a move cannot produce a better outcome than previously examined moves. By disregarding these suboptimal branches, 
    the algorithm significantly reduces the number of possible game states it needs to examine, resulting in faster computation times without sacrificing accuracy in the AI's decision-making.

    The game loop is the orchestrator of this script, driving the game forward by alternating turns between the human player and the AI. During each turn, 
    the respective player removes any number of objects from a single pile of their choosing, with the end goal of being the last to take an object, or, 
    depending on the variant, forcing the opponent to take the last object.

    The game reaches its conclusion when all objects have been removed from all piles. Depending on the variant of Nim being played, 
    the player who takes the last object is either designated the winner or the loser. 
    This script declares the human player the loser if they remove the last object, aligning with the common "misère" version of Nim.

    Overall, the game serves as a showcase for the application of classic game theory and AI algorithms to solve a problem that is both ancient and modern.
    It provides a tangible demonstration of how abstract AI concepts like state space search, decision trees, 
    and optimization techniques can be applied to create an engaging and challenging game experience.
"""

