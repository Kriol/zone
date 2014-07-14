#!/usr/bin/python3
# -*- coding: utf-8 -*-
People = {}
with open('data.txt', 'rt', encoding='utf-8') as src:
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
            People[name] -= 1
            if People[name] == 0:
                del People[name]
            else:
                print('Ошипка')
