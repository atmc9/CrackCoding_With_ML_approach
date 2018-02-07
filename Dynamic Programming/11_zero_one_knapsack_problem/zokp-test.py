import zokp

# Test1 - expected result - [(3,4),(4,5)]
print(zokp.zero_one_knapsack(7, [(1,1),(3,4),(4,5),(5,7)]))

# Test2 - expected result - [(1,3),(3,9),(5,9)]
print(zokp.zero_one_knapsack(9, [(1,3),(2,4),(3,9),(4,5),(5,9)]))

# Test3 - expected result - []
print(zokp.zero_one_knapsack(0, [(1,3),(2,4),(3,9),(4,5),(5,9)]))
