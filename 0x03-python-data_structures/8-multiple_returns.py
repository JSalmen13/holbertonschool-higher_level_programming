#!/usr/bin/python3
def multiple_returns(sentence):
    L = len(sentence)
    if L == 0:
        new = (L, None)
    else:
        new = (L, sentence[0])
    return new
