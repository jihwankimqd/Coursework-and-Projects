# d1 = 0.040865259001783
# d2 = 0.0015264881939962944
# d3 = 0.002303666643682771

# d2 and d3 are closer to each other realtive to d1. This may be because of the difference in
# the sampling method of the calculations. d1 involved direct sampling of non-uniform random variables,
# and therefore it is natural for it to have a larger error. However, d2 and d3 involved carefully
# selected importance sampling, and hence it is natural for it to show smaller errors. The results
# agree with this prediction.