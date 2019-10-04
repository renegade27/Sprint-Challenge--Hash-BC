#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for ticket in tickets:
        # Add all tickets to hashtable
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    # Retrieve our initial starting point as the value (destination) will be None
    route[0] = hash_table_retrieve(hashtable, 'NONE')
    # Iterate through and add next ticket destination to route
    for i in range(1, length):
        route[i] = hash_table_retrieve(hashtable, route[i - 1])
    # return our new route
    return route
