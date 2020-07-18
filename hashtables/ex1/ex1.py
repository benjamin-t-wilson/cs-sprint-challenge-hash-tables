#input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
#output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
#```

### Hints
 
#* A brute-force solution would involve two nested loops, yielding a
#  quadratic-runtime solution. How can we use a hash table in order to
#  implement a solution with a better runtime?

#* Think about what we can store in the hash table in order to help us to
#  solve this problem more efficiently. 

#* What if we store each weight in the input list as keys? What would be
#  a useful thing to store as the value for each key? 

#* If we store each weight's list index as its value, we can then check
#  to see if the hash table contains an entry for `limit - weight`. If it
#  does, then we've found the two items whose weights sum up to the
#  `limit`!

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    dupe_check = False
    dupes = {}

    for i in range(0, length):

        current = weights[i]
        cache[current] = i
        target = limit - current

        if target in cache:
            if current > target or current < target:
                return (i, cache[target])

            elif target == current:
                if dupe_check is False:
                    dupe_check = True
                    dupes[current] = i

                elif dupe_check is True:
                    return (i, dupes[current])

    return None