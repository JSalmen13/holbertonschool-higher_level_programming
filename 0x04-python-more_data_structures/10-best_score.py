#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        a = list(a_dictionary.keys())[0]
        for key in a_dictionary:
            if a_dictionary[key] > a_dictionary[a]:
                a = key
        return a
    return None
