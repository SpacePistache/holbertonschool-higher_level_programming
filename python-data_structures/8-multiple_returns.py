#!/usr/bin/python3
def multiple_returns(sentence):
    # Check if the sentence is empty
    if sentence == "":
        return (0, None)
    else:
        return (len(sentence), sentence[0])
