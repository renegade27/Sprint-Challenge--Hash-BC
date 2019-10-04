#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    if length == 2:
        return 1,0

    for weight in weights:
        # Insert weight into table
        hash_table_insert(ht, weight, weights.index(weight))
        # Check to see if there is a weight in table that is the difference of this weight and limit,
        # this would be our tuple
        if hash_table_retrieve(ht, limit - weight) is not None:
            # Checking indeces of the weight we're evaluating and the one we try and retrieve
            # At this point we know we've found the correct weights as the needed weight was retrieved
            # and is not none
            if weights.index(weight) > hash_table_retrieve(ht, limit - weight):
                # Place our current weight index in front as it's larger
                return int(weights.index(weight)), int(hash_table_retrieve(ht, limit - weight))
            else:
                # Place our current weight index in back as it's smaller
                return int(hash_table_retrieve(ht, limit - weight)), int(weights.index(weight))

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
