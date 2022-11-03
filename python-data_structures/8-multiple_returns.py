#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        set_length = len(sentence)
        first_letter = sentence[0]
    else:
        set_length = 0
        first_letter = None

    return tuple((set_length, first_letter))
