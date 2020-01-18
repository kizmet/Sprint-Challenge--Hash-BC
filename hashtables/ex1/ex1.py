#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_remove,
    hash_table_retrieve,
    hash_table_resize,
)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    # loop through array
    for i in range(len(weights)):
        # retrieve limit minus weight, if exists. if not
        if hash_table_retrieve(ht, limit - weights[i]) is not None:
            # if index is found, return
            return [i, hash_table_retrieve(ht, limit - weights[i])]
            # otherwise insert numer
        hash_table_insert(ht, weights[i], i)

    return None


answer = get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

    # ht.storage = {{weights[i]:  i} for i in range(0, length)}
    # [i.keys() for i in ht.storage]
    # x=list([i.values() for i in ht.storage])
