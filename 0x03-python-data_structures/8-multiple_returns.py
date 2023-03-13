#!/usr/bin/python3
def multiple_returns(sentence):
    sen_len = len(sentence)
    sen_first = ""
    if len(sentence) == 0:
        sen_first = None

    for i in range(len(sentence)):
        if i == 0:
            sen_first = sentence[0]
            break
    tuple_mult = (sen_len, sen_first)
    return tuple_mult


if __name__ == "__main__":
    multiple_returns()
