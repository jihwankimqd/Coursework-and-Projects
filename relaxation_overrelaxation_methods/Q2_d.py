# Using (-1) for the question gave the fastest number of iterations (2).
# This may be because the equation in the over-relaxation method
#           x_ = (1 + w) * f(x[-1]) - w * x[-1]
# at w=(-1), naturally becomes
#           x_ =  x[-1]
# this means that the solution with converge within two tries
# because the same value will be used. But this does not (always) lead to a solution
# and is hence not very useful, but should be minded to avoid mistakes.

