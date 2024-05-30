# GoNim: AI for the Game of Nim

## Overview

This project applies the Minimax Algorithm with Alpha-Beta Pruning to create an AI capable of playing the Game of Nim. The game, a classic example of combinatorial strategy, is used to demonstrate the effectiveness of traditional AI algorithms in decision-making scenarios.

## Table of Contents

1. [Introduction](#introduction)
2. [Background](#background)
3. [Methodology](#methodology)
4. [Experiments and Outcomes](#experiments-and-outcomes)
5. [Analysis](#analysis)
6. [Conclusion](#conclusion)
7. [Usage](#usage)
8. [References](#references)

## Introduction

The Game of Nim is a two-player, turn-based strategy game. Players take turns removing items from piles, with the goal of being the last to perform a valid move.
This project leverages the Minimax Algorithm with Alpha-Beta Pruning to enhance the AI's decision-making capabilities, making it a formidable opponent against human players.

## Background

The Game of Nim is a well-studied problem in combinatorial game theory. 
The AI developed for this project employs several key concepts from artificial intelligence, including:

- **Minimax Algorithm**: Evaluates all possible moves and outcomes to minimize the possible loss in a worst-case scenario.
- **Alpha-Beta Pruning**: Optimizes the Minimax Algorithm by eliminating the need to explore moves that won't affect the final decision.

## Methodology

The development of the AI involved several key steps:

1. **Game Initialization**: Randomly assigns a quantity of objects to a variable number of piles.
2. **Game State Display**: Shows the current game state to both players.
3. **Decision Making**: Utilizes the Minimax Algorithm with Alpha-Beta Pruning to determine the optimal move.
4. **AI and Player Moves**: Handles move execution for both the AI and human player.
5. **Game Loop**: Alternates turns between the AI and human player until the game concludes.

## Experiments and Outcomes

The AI was tested against human opponents, consistently demonstrating strong strategic abilities. 
The results highlight the practical value of the Minimax Algorithm with Alpha-Beta Pruning in strategic decision-making.

## Analysis

The AI's performance was analyzed in multiple games, showing its ability to make smart strategic choices. 
However, the unpredictability of human players posed challenges, underscoring the importance of adaptability in AI strategies.

## Conclusion

The project successfully developed an AI that excels in the Game of Nim, demonstrating the power of traditional AI algorithms. 
The findings suggest pathways for future research in AI and game theory, particularly in handling human unpredictability.

## References

- BasuMallick, C. (2022). What is Dynamic Programming? [Spiceworks](https://www.spiceworks.com/tech/devops/articles/what-is-dynamic-programming/)
- Brennan, A. (2023). Minimax algorithm and alpha-beta pruning. [Medium](https://medium.com/@aaronbrennan.brennan/minimax-algorithm-and-alpha-beta-pruning-646beb01566c)
- Elliott, E. (2019). Normative Decision Theory. [ANALYSIS](https://academic.oup.com/analysis/article-abstract/79/4/755/5570297?redirectedFrom=fulltext)
- geeksForgeeks. (n.d.). Combinatorial Game Theory | Set 2 (Game of Nim). [GeeksforGeeks](https://www.geeksforgeeks.org/combinatorial-game-theory-set-2-game-nim/)
- Julian, R. (n.d.). The Game of Nim. [wikimath](https://wiki.math.wisc.edu/images/Nim_sol.pdf)
- Singh, N. (2023). State Space Search in Artificial Intelligence. [Scaler](https://www.scaler.com/topics/artificial-intelligence-tutorial/state-space-search-in-artificial-intelligence/)
- TURING. (n.d.). An Overview of Bayesian Networks in AI. [TURING](https://www.turing.com/kb/an-overview-of-bayesian-networks-in-ai)
