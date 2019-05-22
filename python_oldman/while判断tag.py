#!/usr/bin/python
# -*- coding: utf-8 -*-

tag = True
while tag:
    print('level1')
    choice = input("level>>: ").strip()
    if choice == 'quit': break
    if choice == 'quit_all': tag = False
    while tag:
        print('level2')
        choice = input("leve2>>: ").strip()
        if choice == 'quit': break
        if choice == 'quit_all': tag = False
        while tag:
            print('level3')
            choice = input("leve3>>: ").strip()
            if choice == 'quit': break
            if choice == 'quit_all': tag = False