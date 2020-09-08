#!/usr/bin/python3
def multiple_returns(sentence):
    _len = len(sentence)
    if sentence:
        char = sentence[0]
    else:
        char = None
    return _len, char
