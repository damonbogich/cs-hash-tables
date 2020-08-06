#what is the birthday paradox?
##sharing a common birthday is suprisingly likely
## if 20 people: 20/365 == 2/36 == 1/18 --> 5%
## if 20 people: odds actually close to 50%
##60/365 --> at least 2 collisions

#similarly collisions are suprisingly likely
##making array bigger will help but not solve this

import random
import hashlib


def our_hashing_function(random_key):
    return int(hashlib.sha3_256(f"{random_key}".encode(), 16)


def how_many_before_collision(length_of_list):

    all_indices = set()
    collision = False
    indices_made = 0

    while not collision:
        #make a bunch of random keys
        random_key = random.random()
        #hash them, modulo them, and keep track of these indices 
        hashed_key = our_hashing_function(random_key)

        new_index = hashed_key % length_of_list

        if new_index in all_indices:
            #see how far we got before we have a collision 
            collision = True

   
        all_indices.add(new_index)
        indices_made += 1 

    print(f'hashes before collision: , {indices_made}')

    how_many_before_collision(8)
