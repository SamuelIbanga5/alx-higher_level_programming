#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    else:
        sentence_length = len(sentence)
        first_character = sentence[0]
        return (sentence_length, first_character)

