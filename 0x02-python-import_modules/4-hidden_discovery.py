#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    prefix = '_'
    for name in dir(hidden_4):
        if (name[0] != prefix) and (name[1] != prefix):
            print(name)
