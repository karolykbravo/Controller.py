#!/usr/bin/env python3

# Replace the functions below with your implementation as described in the assignment


def is_rhyme(word1, word2, nb_letters):

 if len(word1) < nb_letters or len(word2) < nb_letters:
     return False
 if word1[-nb_letters:] == word2[-nb_letters:]:
    return True
    return False
