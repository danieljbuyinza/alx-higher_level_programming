#!/usr/bin/python3
for character in range(97, 123):
    if (chr(character) != 'e') and (chr(character) != 'q'):
        print(chr(character).format(character), end="")
