#!/usr/bin/python3
# -*- coding: utf-8 -*-

class ErrorInSourceFile(Exception): pass

def inside(filename, encoding='utf-8'):
    People = {}
    with open(filename, 'rt', encoding=encoding) as src:
        for line in src:
            line = line.strip()
            name = line[1:]
            symbol = line[0]
            if symbol == '+':
                try:
                    People[name] += 1
                except KeyError:
                    People[name] = 1
            elif symbol == '-':
                try:
                    People[name] -= 1
                    if People[name] == 0:
                        del People[name]
                except KeyError as Err:
                    raise ErrorInSourceFile('Hole in perimeter') from Err
            else:
                raise ErrorInSourceFile('+ or expected')
    for name, count in People.items():
        if count != 1:
            raise ErrorInSourceFile('Entered twice')
        yield name


try:
    for name in inside('data.txt'):
        print(name)
except ErrorInSourceFile as Err:
    print(Err)
