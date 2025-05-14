#!/usr/bin/env python3

def return_evens(num_list):
    even = []
    for n in num_list:
        if n % 2 == 0:
            even.append(n)
            print(even)
    return even

def make_exclamation(sentence_list):
    result = []
    for sentence in sentence_list:
        result.append(sentence + "!")
    return(result)