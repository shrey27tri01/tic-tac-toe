## Tic Tac Toe

An AI to play tic-tac-toe, implemented using the minimax algorithm.  

The minimax algorithm is an adversarial brute force recursive search algorithm, where there are two players, one of which is trying to maximize a score, and the other is trying to minimize the score. The algorithm tries to optimize a player's move after considering all the possible states that the game can go through from that point onwards.  

In the case of tic-tac-toe, the algorithm tries to maximize the score for 'X', and tries to minimize the score for 'O'. 

Alpha-Beta pruning is a method to optimize the runtime of the minimax algorithm by terminating the evaluation of a move when it makes sure that it is worse than a previously examined move.   When added to the simple minimax algorithm, it gives the same output, but cuts off certain branches that can't possibly affect the final decision, hence dramatically improving the perfomance. 


### Usage:

It is recommended to create a python virtual environment first.

```
pip install -r requirements.txt
python runner.py
```

### Resources:

Some good resources to learn more about the minimax algorithm and alpha-beta pruning are:

1. [This](https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python) StackAbuse article by Mina Krivokuća
2. Cornell CS's [post](https://www.cs.cornell.edu/courses/cs312/2002sp/lectures/rec21.htm) on Minimax search
3. [This](https://www.youtube.com/watch?v=l-hh51ncgDI) awesome video by Sebastian Lague
4. [Another](https://www.youtube.com/watch?v=trKjYdBASyQ) awesome video by Daniel Shiffman on The Coding Train