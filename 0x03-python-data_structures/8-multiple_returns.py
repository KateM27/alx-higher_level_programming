#!/usr/bin/python3
def multiple_returns(sentence):
    sen = len(sentence)

    if sen > 0:
        new_tuple = (sen, sentence[0])
        return new_tuple
    else:
        return (sen, None)
