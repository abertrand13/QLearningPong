# THINKING THROUGH STATES

In their original incarnation, the state variables were:
- Whether the ball was to the left or right of the paddle (left indicating that you had 'lost')
- Whether the ball was moving up or down
- Whether the ball was moving left or right

Combinations of these binary variables formed the states, while 'move up' and 'move down' comprised the actions. There was a large negative reward for all action/state combinations which included the ball being to the left of the paddle.

This approach had a few issues, namely:
- The paddle skitters.  It never stays still.
- An entire half of the state/action Q matrix is left untouched (the half for which the ball position state is 'to the right of the paddle' [still in play]).  It is not entirely clear if this is actually a problem, but it seems kind of weird to be only using half your resources.
- The paddle doesn't actually seek out the ball in any apparent matter.

Performance seemed to go up a touch (the paddle displayed some semblance of logic) by changing the 'ball moving up or down' state to 'ball above or below the paddle'.  Still left the issue of half the matrix not being used, though


Note: All this is based on the current implementation of the Q-learning algorithm.  It's probably wrong, so there's that...
		
